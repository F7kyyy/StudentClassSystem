import pymysql

class student(object):

    def __init__(self,sid,sname,code):
        self.SID=sid
        self.SNAME=sname
        self.CODE=code


    def changecode(self,old,new):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from student where SID = %s and CODE=%s "
        result = cur.execute(sqlSearch, (self.SID,old))
        if result > 0:
            sql="update student set CODE=%s where SID=%s"
            cur.execute(sql,(new,self.SID))
            con.commit()
            print("修改成功")
        else:
            print("原密码不正确")#error  
        cur.close()
        con.close()

    def deletedate(self):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where CID=%s"
        result = cur.execute(sqlSearch, self.SID)
        if result > 0:
            sql="delete from class where CID=%s"
            cur.execute(sql,self.SID )
            con.commit()
            print("删除预约成功")
        else:
            print("无预约记录")
        cur.close()
        con.close()

    def searchclass(self,cname):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem', charset='utf8')
        cur = con.cursor()
        sqlSearch = "select  * from class where CNAME like '%%%%%s%%%%' and CNAME<>'预约' order by CID "
        sqlSearch = sqlSearch % (cname)
        result = cur.execute(sqlSearch)
        if result>0:
            cur.execute(sqlSearch)
            lst=cur.fetchall()
            for detailrow in lst:
                cid = detailrow[0]
                cname = detailrow[1]
                teacher = detailrow[2]
                room = detailrow[3]
                start = detailrow[4]
                end = detailrow[5]
                mon = detailrow[6]
                tue = detailrow[7]
                wed = detailrow[8]
                thu = detailrow[9]
                fri = detailrow[10]
                sat = detailrow[11]
                sun = detailrow[12]
                print("%s %s %s %s %s ~ %s 周上 %s  %s %s %s %s %s %s" % (cid, cname, teacher, room, start, end, mon, tue, wed, thu, fri, sat, sun))
        else:
            print("not exist")#error
        cur.close()
        con.close()

    def searchteacher(self,tname):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where TEACHER like '%%%%%s%%%%' and CNAME<>'预约' order by CID"
        sqlSearch = sqlSearch % (tname)
        result = cur.execute(sqlSearch)
        if result > 0:
            cur.execute(sqlSearch)
            lst = cur.fetchall()
            for detailrow in lst:
                cid = detailrow[0]
                cname = detailrow[1]
                teacher = detailrow[2]
                room = detailrow[3]
                start = detailrow[4]
                end = detailrow[5]
                mon = detailrow[6]
                tue = detailrow[7]
                wed = detailrow[8]
                thu = detailrow[9]
                fri = detailrow[10]
                sat = detailrow[11]
                sun = detailrow[12]
                print("%s %s %s %s %s %s %s %s %s %s %s %s %s" % (cid, cname, teacher, room, start, end, mon, tue, wed, thu, fri, sat, sun))
        else:
            print("not exist")  # error
        cur.close()
        con.close()

    def searchroom(self,week,day,section):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        if day=='1':
            sql1="create table room1 as select ROOM from class where START<=%s and END>=%s and MON=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql="select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2="drop table room1"
            cur.execute(sql2)
            con.commit()

        if day=='2':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and TUE=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        if day=='3':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and WED=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        if day=='4':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and THU=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        if day=='5':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and FRI=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        if day=='6':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and SAT=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        if day=='7':
            sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and SUN=%s"
            cur.execute(sql1, (week, week, section))
            con.commit()
            sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
            cur.execute(sql)
            lst = cur.fetchall()
            for detailrow in lst:
                room = detailrow[0]
                print("%s" % room)
            sql2 = "drop table room1"
            cur.execute(sql2)
            con.commit()
        cur.close()
        con.close()

    def dateroom(self,week,day,room,section):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where CID = %s "
        result = cur.execute(sqlSearch, self.SID)
        if result > 0:
            print("已预约了一个教室")#error
        else:
            if day=='1':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and MON=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,%s,0,0,0,0,0,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='2':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and TUE=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,%s,0,0,0,0,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='3':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and WED=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,0,%s,0,0,0,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='4':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,%s,0,0,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='5':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and FRI=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,%s,0,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='6':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,0,%s,0)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            if day=='7':
                sqlSearch="select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
                result=cur.execute(sqlSearch,(week,week,room,section))
                if result>0:
                    print("not available")#error
                else:
                    sql="insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,0,0,%s)"
                    cur.execute(sql,(self.SID,self.SNAME,room,week,week,section))
                    print("done")#success
            con.commit()
            cur.close()
            con.close()


class administrator(object):

    def __init__(self,did,dcode):
        self.DID=did
        self.DCODE=dcode

    def changecode(self,old,new):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where DID = %s and DCODE=%s "
        result = cur.execute(sqlSearch, (self.DID,old))
        if result > 0:
            sql="update administrator set DCODE=%s where DID=%s"
            cur.execute(sql,(new,self.DID))
            con.commit()
            print("修改成功")
        else:
            print("原密码不正确")#error
        cur.close()
        con.close()

    def input(self,cid,cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun):
        if cid=="" or cname=="" or teacher=="" or room=="" \
                or start=="" or end=="" or mon=="" or tue==""\
                 or wed=="" or thu=="" or fri=="" or sat=="" or sun=="":
            print("信息不完整")#error
        else:
            con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
            cur = con.cursor()

            flag=0
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s and MON=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,mon,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and TUE=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,tue,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and WED=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,wed,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and THU=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,thu,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and FRI=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,fri,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and SAT=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,sat,room,cid))
                if result>0:
                    flag=1
            if flag!=1:
                sql1="select ROOM from class where START>=%s and END<=%s  and SUN=%s and ROOM=%s and CID<>%s"
                result=cur.execute(sql1, (start,end,sun,room,cid))
                if result>0:
                    flag=1
            if flag==1:
                print("与已有课教室冲突")
            else:
                sql="insert into class values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(sql,(cid,cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun))
                con.commit()
            cur.close()
            con.close()

    def deletedate(self,week):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch="select * from class where END<%s and END=START"
        result=cur.execute(sqlSearch,week)
        if result>0:
            sql="delete from class where end<%s and end=start"
            cur.execute(sql,week)
            con.commit()
            print("done")#completed
        else:
            print("无可删除的预约")#error
        cur.close()
        con.close()

    def deleteclass(self,cid,cname):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where CID=%s and CNAME=%s"
        result = cur.execute(sqlSearch, (cid,cname))
        if result>0:
            sql = "delete from class where CID=%s and CNAME=%s"
            cur.execute(sql, (cid,cname))
            con.commit()
            print("done")  # completed
        else:
            print("not exist")#error
        cur.close()
        con.close()

    def updateclass(self,cid,cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from class where CID=%s"
        result=cur.execute(sqlSearch,cid)
        if result>0:
            sql="update class set CNAME=%s, TEACHER=%s,ROOM=%s,START=%s," \
                "END=%s,MON=%s,TUE=%s,WED=%s,THU=%s,FRI=%s,SAT=%s,SUN=%s where CID=%s"
            cur.execute(sql, (cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun,cid))
            con.commit()
            print("done")  # completed
        else:
            print("该课序号的课不存在")#error
        cur.close()
        con.close()

    def inputstudent(self,sid,sname):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch="select * from student where SID = %s "
        result=cur.execute(sqlSearch,sid)
        if result>0:
            print("该学生账号已存在")#error
        else:
            sql="insert into student values(%s,%s,%s)"
            cur.execute(sql,(sid,sname,sid))
            con.commit()
            print("done")
        cur.close()
        con.close()

    def deletestudent(self,sid):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from student where SID=%s"
        result = cur.execute(sqlSearch, sid)
        if result>0:
            sql = "delete from student where SID=%s"
            cur.execute(sql, sid)
            con.commit()
            print("done")  # completed
        else:
            print("not exist")#error
        cur.close()
        con.close()

    def outputall(self):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sql="select * from class order by CID"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            cid= detailrow[0]
            cname= detailrow[1]
            teacher= detailrow[2]
            room= detailrow[3]
            start= detailrow[4]
            end= detailrow[5]
            mon= detailrow[6]
            tue= detailrow[7]
            wed= detailrow[8]
            thu= detailrow[9]
            fri= detailrow[10]
            sat= detailrow[11]
            sun= detailrow[12]
            print("%s %s %s %s %s %s %s %s %s %s %s %s %s" % (cid,cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun))
        cur.close()
        con.close()

    def outputallstudents(self):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sql="select * from student"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            sid= detailrow[0]
            sname= detailrow[1]
            code= detailrow[2]
            print("%s %s %s" % (sid,sname,code))
        cur.close()
        con.close()


class login(object):

    def stu(self,sid):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from student where SID=%s"
        result = cur.execute(sqlSearch, sid)
        if result > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                sid=detailrow[0]
                sname=detailrow[1]
                code=detailrow[2]
                s=student(sid,sname,code)
                c=input('密码:')
                if c==s.CODE:
                    while 1:
                        op=input('1：改密码，2：查老师，3：查课，4：查空教室，5：预约,6:删除预约，7:退出')
                        if op=='1':
                            old=input('旧密码')
                            new=input('新密码')
                            s.changecode(old,new)
                        if op=='2':
                            tname=input('老师姓名')
                            s.searchteacher(tname)
                        if op=='3':
                            cname=input('课名')
                            s.searchclass(cname)
                        if op=='4':
                            week=input('周次')
                            day=input('星期几')
                            section=input('第几节')
                            s.searchroom(week,day,section)
                        if op=='5':
                            week = input('周次')
                            day = input('星期几')
                            room=input('教室')
                            section = input('第几节')
                            s.dateroom(week,day,room,section)
                        if op=='6':
                            s.deletedate()
                        if op=='7':
                            return
                else:
                    print("密码错误")
                    return
        else:
            print("账号不存在")

    def adm(self,did):
        con = pymysql.connect(host='123.57.228.221', user='admin', password='mqc201348', database='roomsystem',charset='utf8')
        cur = con.cursor()
        sqlSearch = "select * from administrator where DID=%s"
        result = cur.execute(sqlSearch, did)
        if result > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                did = detailrow[0]
                code = detailrow[1]
                s = administrator(did, code)
                c = input('密码:')
                if c == s.DCODE:
                    while 1:
                        op = input('0：改密码，1：录课，2：删除预约，3：删课，5：查看全部课，6：添加学生账号，7：查看全部学生账号，8：删除学生账号，9：退出')
                        if op=='0':
                            old=input('旧密码')
                            new=input('新密码')
                            s.changecode(old,new)

                        if op == '1':
                            cid=input('id')
                            cname=input('classname')
                            teacher=input('teacher')
                            room=input('room')
                            start=input('start')
                            end=input('end')
                            mon=input('mon')
                            tue=input('tue')
                            wed=input('wed')
                            thu=input('thu')
                            fri=input('fri')
                            sat=input('sat')

                            sun=input('sun')
                            s.input(cid,cname,teacher,room,start,end,mon,tue,wed,thu,fri,sat,sun)
                        if op == '2':
                            week=input('第几周前')
                            s.deletedate(week)
                        if op == '3':
                            cid=input('课序号')
                            cname=input('课名')
                            s.deleteclass(cid,cname)
                        if op == '5':
                            s.outputall()
                        if op=='6':
                            sid=input('输入学生账号')
                            sname = input('输入学生姓名')
                            s.inputstudent(sid,sname)
                        if op=='7':
                            s.outputallstudents()
                        if op == '8':
                            sid=input('学生账号')
                            s.deletestudent(sid)
                        if op == '9':
                            return
                else:
                    print("密码错误")
                    return
        else:
            print("管理员账号不存在")


while 1:
    op=input('1：管理员，2：学生,3:退出')
    if op=='1':
        did=input('输入账号')
        a=login()
        a.adm(did)
    if op=='2':
        sid=input('输入账号')
        a = login()
        a.stu(sid)
    if op=='3':
        break


'''
    pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象
'''

