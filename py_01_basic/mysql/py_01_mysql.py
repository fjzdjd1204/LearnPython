import pymysql
from pymysql import connect


class JD(object):
  def __init__(self):
    self.connection = pymysql.connect(host='localhost', user='root', password='password', db='jing_dong',
                                      charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    self.cursor = self.connection.cursor()

  def __del__(self):
    self.cursor.close()
    self.connection.close()

  def execute_sql(self, sql):
    self.cursor.execute(sql)
    for temp in self.cursor.fetchall():
      print(temp)

  def show_all_items(self):
    sql = "select * from goods;"
    self.execute_sql(sql)

  def show_cates(self):
    sql = "select cate_name from goods"
    self.execute_sql(sql)

  def show_brands(self):
    sql = "select brand_name from goods"
    self.execute_sql(sql)

  @staticmethod
  def print_menu():
    print('--JD--')
    print('1: all the products')
    print('2: all the type of products')
    print('3: all the brands of products')
    return input('please input the function number:')

  def run(self):
    while True:
      num = self.print_menu()
      if num == "1":
        self.show_all_items()
        pass
      elif num == "2":
        self.show_cates()
        pass
      elif num == "3":
        self.show_brands()
        pass
      else:
        print("please enter again, check your input content")


def main():
  jd = JD()
  jd.run()


if __name__ == "__main__":
  main()
