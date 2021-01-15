import pymysql


class administrator(object):
    def __init__(self, m_user_ID, m_password):
        self.administrator_ID = m_user_ID
        self.password = m_password

    # 更改密码
    def changePassword(self, old, new):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where administrator_ID = %s and password=%s"
        result = cur.execute(sqlSearch, (self.administrator_ID, old))
        if result > 0:
            sql = "update administrator set password=%s where administrator_ID=%s"
            cur.execute(sql, (new, self.administrator_ID))
            con.commit()
            print("修改成功")
        else:
            print("帐户或密码错误")
        cur.close()
        con.close()

    # 更改名字
    def changeName(self, new):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where administrator_ID = %s"
        result = cur.execute(sqlSearch, (self.administrator_ID))
        if result > 0:
            sql = "update administrator set name=%s where administrator_ID=%s"
            cur.execute(sql, (new, self.administrator_ID))
            con.commit()
            print("修改成功")
        cur.close()
        con.close()

    # 查看所有用户
    def outputallstudents(self):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "select user_ID,name,department,telephone,sign from user group by user_ID"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            userID = detailrow[0]
            name = detailrow[2]
            department = detailrow[5]
            telephone = detailrow[6]
            sign = detailrow[7]
            print("%s %s %s %s %s " % (
                userID, name, department, telephone, sign))

        cur.close()
        con.close()
   #某个用户的详细信息
    def searchUser(self, userID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlsearch = "select * from user where user_ID =%s"
        cur.execute(sqlsearch, userID)
        lst = cur.fetchall()
        for detailrow in lst:
            userID = detailrow[0]
            password = detailrow[1]
            name = detailrow[2]
            sex = detailrow[3]
            grade = detailrow[4]
            department = detailrow[5]
            telephone = detailrow[6]
            sign = detailrow[7]
            latest_landing_time = detailrow[8]
            print("%s %s %s %s %s %s %s %s %s" % (
                userID, password, name, sex, grade, department, telephone, sign, latest_landing_time))
        cur.close()
        con.close()

    # 封禁
    def blockAccount(self, userID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "update user set sign= 'N' where user_ID= %s"
        askAgain = input('是否封禁该用户账号：Y or N:')

        if askAgain == 'Y':
            cur.execute(sql, userID)
            con.commit()
            print("已封禁，他将无法执行任何操作")

        cur.close()
        con.close()

    # 解封
    def unblockAccount(self, userID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "update user set sign= 'Y' where user_ID= %s"
        askAgain = input('是否解封该用户账号：Y or N:')

        if askAgain == 'Y':
            cur.execute(sql, userID)
            con.commit()
            print("已解封，账号将恢复正常")

        cur.close()
        con.close()



    def outputalltask(self):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "select * from task order by time desc"
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
            print("%s %s %s %s %s %s %s %s %s" % (
                task_ID, user_ID, title, content, opening_time, finish_time, status, payment, time))

        cur.close()
        con.close()

    def deletetask(self, taskID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "delete from task where task_ID=%s"
        askAgain = input('确定删除帖子：Y or N:')
        if askAgain == 'Y':
            cur.execute(sql, taskID)
            con.commit()
            print("已删除")
        cur.close()
        con.close()


class login(object):
    def adm(self, id):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='FZKfzk0057', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where administrator_ID=%s "
        result = cur.execute(sqlSearch, id)
        if result > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                administrator_ID = detailrow[0]
                password = detailrow[2]
                s = administrator(id, password)
                c = input("密码:")
                if c == s.password:
                    # s.blockAccount(2019)
                    s.outputallstudents()


op = input('账号:')
a = login()
a.adm(op)
