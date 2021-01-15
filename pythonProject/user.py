import pymysql
from datetime import datetime as dt
import itertools

number = 0


def register():
    con = pymysql.connect(host='localhost', user='root',
                          password='123456', database='jobbing', charset='utf8')
                        
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


class administrator(object):
    def __init__(self, m_user_ID, m_password):
        self.administrator_ID = m_user_ID
        self.password = m_password

    # 更改密码
    def changePassword(self, old, new):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "select user_ID,name,department,telephone,sign from user group by user_ID"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            userID = detailrow[0]
            name = detailrow[1]
            department = detailrow[3]
            telephone = detailrow[4]
            sign = detailrow[5]
            print("%s %s %s %s %s " % (
                userID, name, department, telephone, sign))

        cur.close()
        con.close()

    # 某个用户的详细信息
    def searchUser(self, userID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlsearch = "select * from user where user_ID =%s"
        cur.execute(sqlsearch, userID)
        lst = cur.fetchall()
        for detailrow in lst:
            userID = detailrow[0]
            password = detailrow[1]
            name = detailrow[2]
            sex = detailrow[3]
            grade = detailrow[5]
            department = detailrow[6]
            telephone = detailrow[7]
            sign = detailrow[8]
            latest_landing_time = detailrow[4]
            print("%s %s %s %s %s %s %s %s %s" % (
                userID, password, name, sex, grade, department, telephone, sign, latest_landing_time))
        cur.close()
        con.close()

    # 封禁
    def blockAccount(self, userID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "update user set sign= 'Y' where user_ID= %s"
        askAgain = input('是否解封该用户账号：Y or N:')

        if askAgain == 'Y':
            cur.execute(sql, userID)
            con.commit()
            print("已解封，账号将恢复正常")

        cur.close()
        con.close()

    # 查看所有的task
    def outputalltask(self):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
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

    # 删除task
    def deletetask(self, taskID):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "delete from task where task_ID=%s"
        askAgain = input('确定删除帖子：Y or N:')
        if askAgain == 'Y':
            cur.execute(sql, taskID)
            con.commit()
            print("已删除")
        cur.close()
        con.close()




class user(object):
    def __init__(self, m_user_ID, m_password):
        self.user_ID = m_user_ID
        self.password = m_password

    # 更改密码

    def changePassword(self, old, new):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
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
                              password='longge1998', database='jobbing', charset='utf8')
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
                              password='123456', database='books', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
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
                              password='123456', database='jobbing', charset='utf8')
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
    def publicTask(self, task_ID, title, content, opening_time, finish_time, payment):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        status = 'N'
        last_landing_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            "insert into task(task_ID,user_ID,title,content,openinng_time,finish_time,status,payment,time) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
            (task_ID, self.user_ID, title, content, opening_time, finish_time, status, payment, last_landing_time))
        con.commit()
        print('发布成功')
        con.close()
        cur.close()

    # 查看帖子
    def checkTask(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
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
            print(" %s %s %s %s %f " % (user_ID, title, content, status, payment))
        cur.close()
        con.close()

    # 查看我发布的帖子
    def checkmyTask(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "select * from task where user_ID =%s"
        cur.execute(sql, (self.user_ID))
        con.commit()
        lst = cur.fetchall()
        for detailrow in lst:
            task_ID = detailrow[0]
            user_id = detailrow[1]
            title = detailrow[2]
            content = detailrow[3]
            opening_time = detailrow[4]
            finish_time = detailrow[5]
            status = detailrow[6]
            payment = detailrow[7]
            time = detailrow[8]
            print(" %s %s %s %f " % (title, content, status, payment))

    # 查看我接受的帖子
    def myacceptTask(self):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sql = "select * from task_receive where user_ID =%s"
        cur.execute(sql, (self.user_ID))
        con.commit()
        lst = cur.fetchall()
        for detailrow in lst:
            task_id = detailrow[0]
            sql = "select * from task where task_ID =%s"
            cur.execute(sql, (task_id))
            con.commit()
            lst = cur.fetchall()
            for detailrow in lst:
                user_id = detailrow[1]
                title = detailrow[2]
                content = detailrow[3]
                opening_time = detailrow[4]
                finish_time = detailrow[5]
                status = detailrow[6]
                payment = detailrow[7]
                time = detailrow[8]
                print(" %s %s %s %f " % (title, content, status, payment))

    # 接受帖子
    def receiveTask(self, task_id):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from task where task_ID=%s"
        cur.execute(sqlSearch, task_id)
        lst = cur.fetchall()
        for detailrow in lst:
            task_id = detailrow[0]
        con.commit()
        sql = "insert into task_receive (task_receiver_ID, user_ID) values (%s,%s)"
        cur.execute(sql, (task_id, self.user_ID))
        con.commit()
        sql = "update task set status=%s where task_ID =%s"
        cur.execute(sql, (1, task_id))
        con.commit()
        print("已接受任务")
        cur.close()
        con.close()

    # 删除帖子
    def deleteTask(self, task_ID):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where task_ID=%s "
        result = cur.execute(sqlSearch, (task_ID))
        if result > 0:
            sql = "delete from class where task_ID=%s"
            cur.execute(sql, (task_ID))
            con.commit()
            print("已删除")
        else:
            print("不存在该任务")
        cur.close()
        con.close()

    # 更新帖子
    def updateTask(self, task_id, user_id, title, content, time1, time2, payment):
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where task_ID=%s"
        result = cur.execute(sqlSearch, task_id)
        if result > 0:
            sql = "update class set user_ID=%s, title=%s,content=%s,time1=%s,time2=%s,payment=%f where task_ID=%s"
            cur.execute(sql, (user_id, title, content, time1, time2, payment))
            con.commit()
            print("已修改")  # completed
        else:
            print("不存在该任务")  # error
        cur.close()
        con.close()


class login(object):
    def user(self, id):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
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
                        num = input('0:修改信息，1：发布任务,2:查看任务,3:删除任务，4：修改任务,5.接受任务,6.查看我发布的任务,7.查看我接受的帖子')
                        if num == '0':
                            while 1:
                                op = input('0：更改密码，1：更改姓名，2：更改性别，3：更改年级，5：更改院系，6：更改电话，7：退出')
                                if op == '0':
                                    old = input('旧密码: ')
                                    new = input('新密码: ')
                                    s.changePassword(old, new)
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
                                if op == '6':
                                    new = input('电话：')
                                    s.changeTelephone(new)
                                if op == '7':
                                    return
                        if num == '1':
                            task_ID=input('任务编号:')
                            title1 = input('分类: ')
                            content1 = input('内容: ')
                            year = int(input('年:'))
                            month = int(input('月:'))
                            day = int(input('日:'))
                            hour = int(input('时:'))
                            minute = int(input('分:'))
                            second = int(input('秒:'))
                            t1 = dt(year, month, day, hour=hour, minute=minute, second=second)
                            year2 = int(input('年:'))
                            month2 = int(input('月:'))
                            day2 = int(input('日:'))
                            hour2 = int(input('时:'))
                            minute2 = int(input('分:'))
                            second2 = int(input('秒:'))
                            t2 = dt(year2, month2, day2, hour=hour2, minute=minute2, second=second2)
                            t1 = t1.strftime("%Y-%m-%d %H:%M:%S")
                            t2 = t2.strftime("%Y-%m-%d %H:%M:%S")
                            payment = input('报酬: ')
                            s.publicTask(task_ID, title1, content1, t1, t2, payment)
                        if num == '2':
                            s.checkTask()
                        if num == '3':
                            taskid = input('任务编号：')
                            s.deleteTask(taskid)
                        if num == '4':
                            taskid = input('任务编号：')
                            userid = input('用户id：')
                            title1 = input('分类: ')
                            content1 = input('内容: ')
                            year = int(input('年:'))
                            month = int(input('月:'))
                            day = int(input('日:'))
                            hour = int(input('时:'))
                            minute = int(input('分:'))
                            second = int(input('秒:'))
                            t1 = dt(year, month, day, hour=hour, minute=minute, second=second)
                            year2 = int(input('年:'))
                            month2 = int(input('月:'))
                            day2 = int(input('日:'))
                            hour2 = int(input('时:'))
                            minute2 = int(input('分:'))
                            second2 = int(input('秒:'))
                            t2 = dt(year2, month2, day2, hour=hour2, minute=minute2, second=second2)
                            payment = input('报酬: ')
                            s.updateTask(taskid, userid, title1, content1, t1, t2, payment)
                        if num == '5':
                            taskid = input('任务编号：')
                            s.receiveTask(taskid)
                        if num == '6':
                            s.checkmyTask()
                        if num == '7':
                            s.myacceptTask()


    def adm(self, id):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='123456', database='jobbing', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where administrator_ID=%s "
        result = cur.execute(sqlSearch, id)
        if result > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                user_ID = detailrow[0]
                password = detailrow[2]
                s = administrator(id, password)
                c = input("密码:")
                if c == s.password:
                    while 1:
                        num = input('0:修改信息 1.查看所有用户 2:查看所有任务  3:查看用户详细信息 4：封禁用户  5.解封用户  6.删除task')
                        if num == '0':
                            op = input('0：更改密码，1：更改姓名')
                            if op == '0':
                                if op == '0':
                                    old = input('旧密码: ')
                                    new = input('新密码: ')
                                    s.changePassword(old, new)
                            if op == '1':
                                new = input('名字：')
                                s.changeName(new)
                        if num == '1':
                            s.outputallstudents()
                        if num == '2':
                            s.outputalltask()
                        if num == '3':
                            op = input('请输入用户ID：')
                            s.searchUser(op)
                        if num == '4':
                            op = input('请输入用户ID：')
                            s.blockAccount(op)
                        if num == '5':
                            op = input('请输入用户ID：')
                            s.unblockAccount(op)
                        if num == '6':
                            op = input('请输入任务ID：')
                            s.deletetask(op)
while 1:
    op=input('1：管理员，2：学生,3:注册，4.退出')
    if op=='1':
        did=input('输入账号')
        a=login()
        a.adm(did)
    if op=='2':
        sid=input('输入账号')
        a = login()
        a.user(sid)
    if op == '3':
        register()
    if op=='4':
        break