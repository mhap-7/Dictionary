# یک هسته ی کلی برای تمام نرم افزار های دیکشنری یعنی دیکشنری گرافیکی و کامندی ساخته ایم
# کتابخانه های مورد نیاز را وارد کردیم
import re
import sqlite3


if __name__ == '__main__':
    exit()

# یک کلاس برای کار با دیتا بیس و کانکت شدن به ان ساختیم
class Database:
    def __init__(self):  # فانکشن اینیت را مخصوص کانکت شدن به دیتابیس Data.db که در فولدر برنامه قرار دارد ساختیم
        self.sql = sqlite3.connect('Data.db')  # کانکت شدن به دیتابیس
        self.cur = self.sql.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS dic ("id" , "English" , "Persian");')  # ساخت یک تیبل در پایگاه داده با دو ستون پارسی و انگلسی برای دیکشنری

    def List(self):
        # برای توسعه ی بیشتر نیاز به ریختن اطلاعات در یک دیکشنری یا لیست احساس میشد پس به وسیله ی این تابع اطلاعات دیتابیس را ئارد لیست کردیم
        ALl_Words = self.cur.execute('SELECT * FROM dic')  # گرفتن اطلاعات از db

        for  id, English,Persian in ALl_Words:# دسته بندی به سه دسته
            words_list = (id, English, Persian)
            if words_list != []:
                yield words_list


          # بر گرداندن دیکشنری حاصل

    def search(self, char, db, advance='0'):
        # برای سرچ کردن کلمات گرفته شده از کاربر ساخته شده است و اینگونه کار میکند
        # end = core_dic.Database()
        # end.search(inp, end.List())
        # و به عنوان ورودی خروجی تابع لیست را دریافت می کند
        if advance=='0':
            for i in db:
                regex = re.findall(r'^%s$' % char, i[1])

                if regex == []:
                    del i
                else:
                    yield 'id -%s-              [ %s ] = [ %s ] ' % (i[0], i[1] , i[2])
        elif advance=='1':
            for i in db:
                regex = re.findall(r'%s' % char, i[1])

                if regex == []:
                    del i
                else:
                    yield 'id -%s-              [ %s ] = [ %s ] ' % (i[0], i[1] , i[2])



    def delete(self, id):
        self.cur.execute('DELETE FROM dic WHERE id = %s' % (id))
        # TODO: This section will be complete

    def add(self,en,fa):
        self.cur.execute('INSERT INTO dic VALUES(  );' % (id))
        # TODO: This section will be complete
