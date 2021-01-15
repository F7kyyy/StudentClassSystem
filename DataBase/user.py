import pymysql
from datetime import datetime as dt
import itertools
number = 0


def register():
    con = pymysql.connect(host='localhost', user='root',
                          password='FZKfzk0057', database='jobbing', charset='utf8')
    cur = con.cursor()
    print('       开始注册')
    user_ID1 = (input('账号：'))
    password1 = (input('密码：'))
    name1 = (input('姓名： '))
    sex1 = (input('性别： '))
    grade1 = (input('年级：'))
    department1 = (input('院系：'))
    telephone1 = (input('电话： '))
    sql = "select * from user where user_ID = %s"
    aa = cur.execute(sql, user_ID1)
    con.commit()

    if aa == 1:
        print("用户已存在，请重新注册")
    else:
        sql = "insert into user(user_ID,password,name,sex,grade,department,telephone,lastest_landing_time) values (%s,%s,%s,%s,%s,%s,%s,now())"
        cur.executemany(
            sql, [(user_ID1, password1, name1, sex1, grade1, department1, telephone1)])
        con.commit()
        print('注册成功')
    con.close()
    cur.close()


class user(object):
    def __init__(self, m_user_ID, m_password):
        self.user_ID = m_user_ID
        self.password = m_password
    # 更改密码

    def changePassword(self, old, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s and password=%s"
        result = cur.execute(sqlSearch, (self.user_ID, old))
        if result > 0:
            sql = "update user set password=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        else:
            print("帐户或密码错误")
        cur.close()
        con.close()
    # 更改名字

    def changeName(self, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s"
        result = cur.execute(sqlSearch, (self.user_ID))
        if result > 0:
            sql = "update user set name=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()
    # 更改性别

    def changeSex(self, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s"
        result = cur.execute(sqlSearch, (self.user_ID))
        if result > 0:
            sql = "update user set sex=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()
    # 更改年级

    def changeGrade(self, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='longge1998', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s"
        result = cur.execute(sqlSearch, (self.user_ID))
        if result > 0:
            sql = "update user set grade=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()
    # 更改院系

    def changeDepartment(self, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s"
        result = cur.execute(sqlSearch, (self.user_ID))
        if result > 0:
            sql = "update user set department=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()
    
    # 更改电话
    def changeTelephone(self, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID = %s"
        result = cur.execute(sqlSearch, (self.user_ID))
        if result > 0:
            sql = "update user set telephone=%s where user_ID=%s"
            cur.execute(sql, (new, self.user_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()

    # 发帖
    def publicTask(self, title, content, opening_time, finish_time, payment):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "insert into task(user_ID,title,content,opening_time,finish_time,payment) values (%s,%s,%s,%s,%s,%s,%s)"
        cur.executemany(sql, [(self.user_ID, title, content, opening_time, finish_time, payment)])
        con.commit()
        print('发布成功')
        con.close()
        cur.close()
    
    #查看帖子
    def checkTask(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='FZKfzk0057', database='books', charset='utf8')
        cur = con.cursor()
        sql = "select * from task order by task_ID"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            task_ID = detailrow[0]
            user_ID = detailrow[1]
            title = detailrow[2]
            content = detailrow[3]
            opening_time = detailrow[4]
            finish_time = detailrow[5]
            status = detailrow[6]
            payment = detailrow[7]
            time = detailrow[8]
            print("%s %s %s %s %s %f " %
                  (task_ID, user_ID, title, content, status, payment))
        cur.close()
        con.close()


    # 接受帖子
    # def receiveTask(self):
    #     con = pymysql.connect(host='localhost', user='root',
    #                           password='longge1998', database='books', charset='utf8')
    #     cur = con.cursor()
    #     sql = "select * from task order by task_ID"
    #     cur.execute(sql)
    #     lst = cur.fetchall()
    #     for detailrow in lst:
    #         task_ID = detailrow[0]
    #         user_ID = detailrow[1]
    #         title = detailrow[2]
    #         content = detailrow[3]
    #         opening_time = detailrow[4]
    #         finish_time = detailrow[5]
    #         status = detailrow[6]
    #         payment = detailrow[7]
    #         time = detailrow[8]
    #         print("%s %s %s %s %s %f " %
    #               (task_ID, user_ID, title, content, status, payment))
    #     cur.close()
    #     con.close()

    


class login(object):
    def use(self, id):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from user where user_ID=%s "
        result = cur.execute(sqlSearch, id)
        if result > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                user_ID = detailrow[0]
                password = detailrow[1]
                s = user(id, password)
                c = input("密码:")
                if c == s.password:
                    while 1:
                        num = input('0:修改信息，1：发布任务,2:查看任务')
                        if num=='0':
                            while 1:
                                op = input('0：更改密码，1：更改姓名，2：更改性别，3：更改年级，5：更改院系，6：更改电话，7：退出')
                                if op=='0':
                                    old = input('旧密码: ')
                                    new = input('新密码: ')
                                    s.changePassword(old,new)
                                if op == '1':
                                    new = input('名字：')    
                                    s.changeName(new)
                                if op == '2':
                                    new = input('性别：')    
                                    s.changeSex(new)
                                if op == '3':
                                    new = input('年级：')    
                                    s.changeGrade(new)
                                if op == '5':
                                    new = input('院系：')    
                                    s.changeDepartment(new)
                                if op=='6':
                                    new = input('电话：')    
                                    s.changeTelephone(new)
                                if op=='7':
                                    return
                        if num=='1':
                            title1 = input('分类: ')
                            content1 = input('内容: ')
                            year=int(input("年:"))
                            month=int(input("月:"))
                            day=int(input("日:"))
                            hour=int(input("时:"))
                            minute=int(input("分:"))
                            second=int(input("秒:"))
                            t1=dt(year,month,day,hour=hour,minute=minute,second=second)
                                                    
                            month=input('月:')
                            day=input('日:')
                            hour=input("时")
                            minute=input('分:')
                            second=input("秒:")
                            t2 = dt(year, month, day, hour=hour, minute=minute, second=second)
                            
                            payment = input('报酬: ')
                            s.publicTask(title1,content1,t1,t2,payment)
                        # if num=='2':
                        #     s.checkTask()

id=input('账号:')
a = login()
a.use(id)
# register()
