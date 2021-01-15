from flask import Flask, jsonify, request
# 跨域请求
from flask_cors import CORS
# 唯一标识
import pymysql

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'orgins': '*'}})


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        post_data = request.get_json()
        number = post_data.get('account')
        code = post_data.get('password')
        con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                              charset='utf8')
        cur = con.cursor()
        sqlSearch1 = "select * from student where SID=%s"
        result1 = cur.execute(sqlSearch1, number)
        if result1 > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                scode = detailrow[2]
                sname = detailrow[1]
                ssid = detailrow[0]
                if code == scode:
                    cur.close()
                    con.close()
                    return jsonify({"who": '1', "success": '1',"name":sname ,'sid':ssid,'code':scode})
                else:
                    cur.close()
                    con.close()
                    return jsonify({"who": '1', "success": '0', })
        con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                              charset='utf8')
        cur = con.cursor()
        sqlSearch2 = "select * from administrator where DID=%s"
        result2 = cur.execute(sqlSearch2, number)
        if result2 > 0:
            lst = cur.fetchall()
            for detailrow in lst:
                dcode = detailrow[1]
                dsid = detailrow[0]
                if code == dcode:
                    cur.close()
                    con.close()
                    return jsonify({"who": '2', "success": '1',"code":dcode,"sid":dsid })
                else:
                    cur.close()
                    con.close()
                    return jsonify({"who": '2', "success": '0', })

        return jsonify({"who": '0', "success": '0', })

@app.route('/api/studentCode', methods=['POST'])
def StudentChangeCode():
    post_data = request.get_json()
    new = post_data.get('new')
    old = post_data.get('old')
    sid = post_data.get('sid')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from student where SID = %s and CODE=%s "
    result = cur.execute(sqlSearch, (sid, old))
    if result > 0:
        sql = "update student set CODE=%s where SID=%s"
        cur.execute(sql, (new, sid))
        con.commit()
        cur.close()
        con.close()
        return jsonify({"success": '1'})  # 学生修改密码成功
    else:
        cur.close()
        con.close()
        return jsonify({"success": '0'})  # 学生原密码不正确


@app.route('/api/studentDeleteDate', methods=['POST'])
def StudentDeleteDate():
    post_data = request.get_json()
    sid = post_data.get('sid')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from class where CID=%s"
    result = cur.execute(sqlSearch, sid)
    if result > 0:
        sql = "delete from class where CID=%s"
        cur.execute(sql, sid)
        con.commit()
        # success="删除预约成功"
        cur.close()
        con.close()
        return jsonify({"success": '1'})
    else:
        # error="无预约记录"
        cur.close()
        con.close()
        return jsonify({"success": '0'})


@app.route('/api/studentsearchroom', methods=['POST'])
def StudentSearchRoom():
    ROOM = []
    post_data = request.get_json()
    week = post_data.get('week')
    day = post_data.get('day')
    section = post_data.get('section')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    if day == '1':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and MON=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})

    if day == '2':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and TUE=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    if day == '3':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and WED=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    if day == '4':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and THU=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    if day == '5':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and FRI=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    if day == '6':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and SAT=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    if day == '7':
        sql1 = "create table room1 as select ROOM from class where START<=%s and END>=%s and SUN=%s"
        cur.execute(sql1, (week, week, section))
        con.commit()
        sql = "select distinct ROOM from class where ROOM not in (select * from room1) group by ROOM"
        cur.execute(sql)
        lst = cur.fetchall()
        for detailrow in lst:
            room = detailrow[0]
            ROOM.append({'roomname': room})
        sql2 = "drop table room1"
        cur.execute(sql2)
        con.commit()
        return jsonify({'allroom': ROOM})
    cur.close()
    con.close()


@app.route('/api/studentdateroom', methods=['POST'])
def StudentDateRoom():

    global err1,err1,succ
    err1 = '0'
    err2 = '0'
    succ = '0'
    post_data = request.get_json()
    sid = post_data.get('sid')
    day = post_data.get('day')
    room = post_data.get('room')
    section = post_data.get('section')
    week = post_data.get('week')

    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from class where CID = %s "
    result = cur.execute(sqlSearch, sid)

    if result > 0:
        # error1 = "已预约了一个教室"
        err1 = '1'
    else:
        if day == '1':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and MON=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,%s,0,0,0,0,0,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        if day == '2':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and TUE=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,%s,0,0,0,0,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        if day == '3':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and WED=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,0,%s,0,0,0,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        if day == '4':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,%s,0,0,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        if day == '5':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and FRI=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,%s,0,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        if day == '6':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,0,%s,0)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                #success = "预约成功"
                succ = '1'

        if day == '7':
            sqlSearch = "select * from class where start<=%s and end>=%s and ROOM=%s and THU=%s"
            result = cur.execute(sqlSearch, (week, week, room, section))
            if result > 0:
                # error2 = "教室不可用"
                err2 = '1'
            else:
                sql = "insert into class values(%s,'预约',%s,%s,%s,%s,0,0,0,0,0,0,%s)"
                cur.execute(sql, (sid, '学生', room, week, week, section))
                # success = "预约成功"
                succ = '1'
        con.commit()
        cur.close()
        con.close()
    return jsonify(
        {
            "success": succ,
            "error1": err1,
            "error2": err2
        }
    )


@app.route('/api/studentsearchclass', methods=['POST'])
def StudentSearchClass():
    post_data = request.get_json()
    cname = post_data.get('cname')
    CLASSES = []

    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select  * from class where CNAME like '%%%%%s%%%%' and CNAME<>'预约' order by CID "
    sqlSearch = sqlSearch % (cname)
    result = cur.execute(sqlSearch)
    global length
    length = 0
    if result > 0:
        cur.execute(sqlSearch)
        lst = cur.fetchall()
        length = len(lst)
        global sscid, ssmon, sstue, sswed, ssthu, ssfri, sssat, sssun, ssroom, ssteacher, ssstart, ssend, sscname
        sscid = '0'
        ssmon = '0'
        sstue = '0'
        sswed = '0'
        ssthu = '0'
        ssfri = '0'
        sssat = '0'
        sssun = '0'
        ssroom = '0'
        ssteacher = '0'
        ssstart = '0'
        ssend = '0'
        sscname = '0'
        global i
        i = 1
        for detailrow in lst:
            if i == 1:
                sscid = str(detailrow[0])
                sscname = str(detailrow[1])
                ssteacher = str(detailrow[2])
                ssroom = str(detailrow[3])
                ssstart = str(detailrow[4])
                ssend = str(detailrow[5])
                ssmon = str(detailrow[6])
                sstue = str(detailrow[7])
                sswed = str(detailrow[8])
                ssthu = str(detailrow[9])
                ssfri = str(detailrow[10])
                sssat = str(detailrow[11])
                sssun = str(detailrow[12])
            elif 1 < i < length:
                if str(detailrow[0]) == sscid:
                    if ssmon != str(detailrow[6]):
                        ssmon = ssmon + '、' + str(detailrow[6])
                    if sstue != str(detailrow[7]):
                        sstue = sstue + '、' + str(detailrow[7])
                    if sswed != str(detailrow[8]):
                        sswed = sswed + '、' + str(detailrow[8])
                    if ssthu != str(detailrow[9]):
                        ssthu = ssthu + '、' + str(detailrow[9])
                    if ssfri != str(detailrow[10]):
                        ssfri = ssfri + '、' + str(detailrow[10])
                    if sssat != str(detailrow[11]):
                        sssat = sssat + '、' + str(detailrow[11])
                    if sssun != str(detailrow[12]):
                        sssun = sssun + '、' + str(detailrow[12])
                else:
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    sscid = str(detailrow[0])
                    sscname = str(detailrow[1])
                    ssteacher = str(detailrow[2])
                    ssroom = str(detailrow[3])
                    ssstart = str(detailrow[4])
                    ssend = str(detailrow[5])
                    ssmon = str(detailrow[6])
                    sstue = str(detailrow[7])
                    sswed = str(detailrow[8])
                    ssthu = str(detailrow[9])
                    ssfri = str(detailrow[10])
                    sssat = str(detailrow[11])
                    sssun = str(detailrow[12])
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
            elif i == length:
                if str(detailrow[0]) == sscid:
                    if ssmon != str(detailrow[6]):
                        ssmon = ssmon + '、' + str(detailrow[6])
                    if sstue != str(detailrow[7]):
                        sstue = sstue + '、' + str(detailrow[7])
                    if sswed != str(detailrow[8]):
                        sswed = sswed + '、' + str(detailrow[8])
                    if ssthu != str(detailrow[9]):
                        ssthu = ssthu + '、' + str(detailrow[9])
                    if ssfri != str(detailrow[10]):
                        ssfri = ssfri + '、' + str(detailrow[10])
                    if sssat != str(detailrow[11]):
                        sssat = sssat + '、' + str(detailrow[11])
                    if sssun != str(detailrow[12]):
                        sssun = sssun + '、' + str(detailrow[12])
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
                else:
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
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
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
            i = i + 1

    cur.close()
    con.close()
    return jsonify({'allclass': CLASSES, 'length': length})


@app.route('/api/studentsearchteacher', methods=['POST'])
def StudentSearchTeacher():
    post_data = request.get_json()
    tname = post_data.get('tname')
    CLASSES = []

    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select  * from class where TEACHER like '%%%%%s%%%%' and CNAME<>'预约' order by CID "
    sqlSearch = sqlSearch % (tname)
    result = cur.execute(sqlSearch)
    global length
    length = 0
    if result > 0:
        cur.execute(sqlSearch)
        lst = cur.fetchall()
        length = len(lst)
        global sscid, ssmon, sstue, sswed, ssthu, ssfri, sssat, sssun, ssroom, ssteacher, ssstart, ssend, sscname
        sscid = '0'
        ssmon = '0'
        sstue = '0'
        sswed = '0'
        ssthu = '0'
        ssfri = '0'
        sssat = '0'
        sssun = '0'
        ssroom = '0'
        ssteacher = '0'
        ssstart = '0'
        ssend = '0'
        sscname = '0'
        global i
        i = 1
        for detailrow in lst:
            if i == 1:
                sscid = str(detailrow[0])
                sscname = str(detailrow[1])
                ssteacher = str(detailrow[2])
                ssroom = str(detailrow[3])
                ssstart = str(detailrow[4])
                ssend = str(detailrow[5])
                ssmon = str(detailrow[6])
                sstue = str(detailrow[7])
                sswed = str(detailrow[8])
                ssthu = str(detailrow[9])
                ssfri = str(detailrow[10])
                sssat = str(detailrow[11])
                sssun = str(detailrow[12])
            elif 1 < i < length:
                if str(detailrow[0]) == sscid:
                    if ssmon != str(detailrow[6]):
                        ssmon = ssmon + '、' + str(detailrow[6])
                    if sstue != str(detailrow[7]):
                        sstue = sstue + '、' + str(detailrow[7])
                    if sswed != str(detailrow[8]):
                        sswed = sswed + '、' + str(detailrow[8])
                    if ssthu != str(detailrow[9]):
                        ssthu = ssthu + '、' + str(detailrow[9])
                    if ssfri != str(detailrow[10]):
                        ssfri = ssfri + '、' + str(detailrow[10])
                    if sssat != str(detailrow[11]):
                        sssat = sssat + '、' + str(detailrow[11])
                    if sssun != str(detailrow[12]):
                        sssun = sssun + '、' + str(detailrow[12])
                else:
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    sscid = str(detailrow[0])
                    sscname = str(detailrow[1])
                    ssteacher = str(detailrow[2])
                    ssroom = str(detailrow[3])
                    ssstart = str(detailrow[4])
                    ssend = str(detailrow[5])
                    ssmon = str(detailrow[6])
                    sstue = str(detailrow[7])
                    sswed = str(detailrow[8])
                    ssthu = str(detailrow[9])
                    ssfri = str(detailrow[10])
                    sssat = str(detailrow[11])
                    sssun = str(detailrow[12])
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
            elif i == length:
                if str(detailrow[0]) == sscid:
                    if ssmon != str(detailrow[6]):
                        ssmon = ssmon + '、' + str(detailrow[6])
                    if sstue != str(detailrow[7]):
                        sstue = sstue + '、' + str(detailrow[7])
                    if sswed != str(detailrow[8]):
                        sswed = sswed + '、' + str(detailrow[8])
                    if ssthu != str(detailrow[9]):
                        ssthu = ssthu + '、' + str(detailrow[9])
                    if ssfri != str(detailrow[10]):
                        ssfri = ssfri + '、' + str(detailrow[10])
                    if sssat != str(detailrow[11]):
                        sssat = sssat + '、' + str(detailrow[11])
                    if sssun != str(detailrow[12]):
                        sssun = sssun + '、' + str(detailrow[12])
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
                else:
                    cid = sscid
                    cname = sscname
                    teacher = ssteacher
                    room = ssroom
                    start = ssstart
                    end = ssend
                    mon = ssmon
                    tue = sstue
                    wed = sswed
                    thu = ssthu
                    fri = ssfri
                    sat = sssat
                    sun = sssun
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
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
                    CLASSES.append({
                        'cid': cid,
                        'cname': cname,
                        'teacher': teacher,
                        'room': room,
                        'start': start,
                        'end': end,
                        'mon': mon,
                        'tue': tue,
                        'wed': wed,
                        'thu': thu,
                        'fri': fri,
                        'sat': sat,
                        'sun': sun
                    })
            i = i + 1

    cur.close()
    con.close()
    return jsonify({'allclass': CLASSES, 'length': length})

@app.route('/api/adminCode', methods=['POST'])
def AdminChangeCode():
    post_data = request.get_json()
    new = post_data.get('new')
    old = post_data.get('old')
    did = post_data.get('did')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    s = "select * from administrator where DID = %s and DCODE=%s "
    sqlSearch = s
    result = cur.execute(sqlSearch, (did, old))
    if result > 0:
        sql = "update administrator set DCODE=%s where DID=%s"
        cur.execute(sql, (new, did))
        con.commit()
        cur.close()
        con.close()
        return jsonify({"success": '1'})  # 管理员修改密码成功
    else:
        cur.close()
        con.close()
        return jsonify({"success": '0'})  # 管理员原密码不正确


@app.route('/api/admininputclass', methods=['POST'])
def AdminInputClass():
    post_data = request.get_json()
    cid = post_data.get('cid')
    cname = post_data.get('old')
    teacher = post_data.get('teacher')
    room = post_data.get('room')
    start = post_data.get('start')
    end = post_data.get('end')
    mon = post_data.get('mon')
    tue = post_data.get('tue')
    wed = post_data.get('wed')
    thu = post_data.get('thu')
    fri = post_data.get('fri')
    sat = post_data.get('sat')
    sun = post_data.get('sun')

    if cid == "" or cname == "" or teacher == "" or room == "" \
            or start == "" or end == "" or mon == "" or tue == "" \
            or wed == "" or thu == "" or fri == "" or sat == "" or sun == "":
        # miss = "信息不完整"
        return jsonify(
            {
                "success": '0',
                "error1": '1',
                "error2": '0'
            }
        )
    else:
        con = pymysql.connect(host='localhost', user='admin', password='000000', database='roomSystem',
                              charset='utf8')
        cur = con.cursor()

        flag = 0
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s and MON=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, mon, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and TUE=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, tue, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and WED=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, wed, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and THU=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, thu, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and FRI=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, fri, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and SAT=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, sat, room, cid))
            if result > 0:
                flag = 1
        if flag != 1:
            sql1 = "select ROOM from class where START>=%s and END<=%s  and SUN=%s and ROOM=%s and CID<>%s"
            result = cur.execute(sql1, (start, end, sun, room, cid))
            if result > 0:
                flag = 1
        if flag == 1:
            # classerror = "与已有课程教室冲突"
            cur.close()
            con.close()
            return jsonify(
                {
                    "success": '0',
                    "error1": '0',
                    "error2": '1'
                }
            )
        else:
            sql = "insert into class values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, (cid, cname, teacher, room, start, end, mon, tue, wed, thu, fri, sat, sun))
            con.commit()
            # success = "录入成功"
            cur.close()
            con.close()
            return jsonify(
                {
                    "success": '1',
                    "error1": '0',
                    "error2": '0'
                }
            )


@app.route('/api/admindeletedate', methods=['POST'])
def AdminDeleteDate():
    post_data = request.get_json()
    week = post_data.get('week')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from class where END<%s and END=START"
    result = cur.execute(sqlSearch, week)
    if result > 0:
        sql = "delete from class where end<%s and end=start"
        cur.execute(sql, week)
        con.commit()
        # success = "删除完成"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '1',
            }
        )
    else:
        # error = "无可删除的预约"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '0',
            }
        )


@app.route('/api/AdminDeleteClass', methods=['POST'])
def AdminDeleteClass():
    post_data = request.get_json()
    cid = post_data.get('cid')
    cname = post_data.get('cname')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from class where CID=%s and CNAME=%s"
    result = cur.execute(sqlSearch, (cid, cname))
    if result > 0:
        sql = "delete from class where CID=%s and CNAME=%s"
        cur.execute(sql, (cid, cname))
        con.commit()
        # done = "删除成功"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '1',
            }
        )
    else:
        # error = "课不存在"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '0',
            }
        )


@app.route('/api/AdminInputStudent', methods=['POST'])
def AdminInputStudent():
    post_data = request.get_json()
    sid = post_data.get('sid')
    sname = post_data.get('sname')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from student where SID = %s "
    result = cur.execute(sqlSearch, sid)
    if result > 0:
        # error = "该学生账号已存在"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '0',
            }
        )
    else:
        sql = "insert into student values(%s,%s,%s)"
        cur.execute(sql, (sid, sname, sid))
        con.commit()
        # success = "添加成功"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '1',
            }
        )


@app.route('/api/AdminDeleteStudent', methods=['POST'])
def AdminDeleteStudent():
    post_data = request.get_json()
    sid = post_data.get('sid')
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sqlSearch = "select * from student where SID=%s"
    result = cur.execute(sqlSearch, sid)
    if result > 0:
        sql = "delete from student where SID=%s"
        cur.execute(sql, sid)
        con.commit()
        # success = "删除成功"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '1',
            }
        )
    else:
        # error = "学生不存在"
        cur.close()
        con.close()
        return jsonify(
            {
                "success": '0',
            }
        )


@app.route('/api/AdminOutputAll', methods=['POST'])
def AdminOutputAll():
    CLASSES = []
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sql = "select * from class order by CID"
    cur.execute(sql)
    lst = cur.fetchall()
    length = len(lst)
    global sscid, ssmon, sstue, sswed, ssthu, ssfri, sssat, sssun, ssroom, ssteacher, ssstart, ssend, sscname
    sscid = '0'
    ssmon = '0'
    sstue = '0'
    sswed = '0'
    ssthu = '0'
    ssfri = '0'
    sssat = '0'
    sssun = '0'
    ssroom = '0'
    ssteacher = '0'
    ssstart = '0'
    ssend = '0'
    sscname = '0'
    global i
    i = 1
    for detailrow in lst:
        if i == 1:
            sscid = str(detailrow[0])
            sscname = str(detailrow[1])
            ssteacher = str(detailrow[2])
            ssroom = str(detailrow[3])
            ssstart = str(detailrow[4])
            ssend = str(detailrow[5])
            ssmon = str(detailrow[6])
            sstue = str(detailrow[7])
            sswed = str(detailrow[8])
            ssthu = str(detailrow[9])
            ssfri = str(detailrow[10])
            sssat = str(detailrow[11])
            sssun = str(detailrow[12])
        elif 1 < i < length:
            if str(detailrow[0]) == sscid:
                if ssmon != str(detailrow[6]):
                    ssmon = ssmon + '、' + str(detailrow[6])
                if sstue != str(detailrow[7]):
                    sstue = sstue + '、' + str(detailrow[7])
                if sswed != str(detailrow[8]):
                    sswed = sswed + '、' + str(detailrow[8])
                if ssthu != str(detailrow[9]):
                    ssthu = ssthu + '、' + str(detailrow[9])
                if ssfri != str(detailrow[10]):
                    ssfri = ssfri + '、' + str(detailrow[10])
                if sssat != str(detailrow[11]):
                    sssat = sssat + '、' + str(detailrow[11])
                if sssun != str(detailrow[12]):
                    sssun = sssun + '、' + str(detailrow[12])
            else:
                cid = sscid
                cname = sscname
                teacher = ssteacher
                room = ssroom
                start = ssstart
                end = ssend
                mon = ssmon
                tue = sstue
                wed = sswed
                thu = ssthu
                fri = ssfri
                sat = sssat
                sun = sssun
                sscid = str(detailrow[0])
                sscname = str(detailrow[1])
                ssteacher = str(detailrow[2])
                ssroom = str(detailrow[3])
                ssstart = str(detailrow[4])
                ssend = str(detailrow[5])
                ssmon = str(detailrow[6])
                sstue = str(detailrow[7])
                sswed = str(detailrow[8])
                ssthu = str(detailrow[9])
                ssfri = str(detailrow[10])
                sssat = str(detailrow[11])
                sssun = str(detailrow[12])
                CLASSES.append({
                    'cid': cid,
                    'cname': cname,
                    'teacher': teacher,
                    'room': room,
                    'start': start,
                    'end': end,
                    'mon': mon,
                    'tue': tue,
                    'wed': wed,
                    'thu': thu,
                    'fri': fri,
                    'sat': sat,
                    'sun': sun
                })
        elif i == length:
            if str(detailrow[0]) == sscid:
                if ssmon != str(detailrow[6]):
                    ssmon = ssmon + '、' + str(detailrow[6])
                if sstue != str(detailrow[7]):
                    sstue = sstue + '、' + str(detailrow[7])
                if sswed != str(detailrow[8]):
                    sswed = sswed + '、' + str(detailrow[8])
                if ssthu != str(detailrow[9]):
                    ssthu = ssthu + '、' + str(detailrow[9])
                if ssfri != str(detailrow[10]):
                    ssfri = ssfri + '、' + str(detailrow[10])
                if sssat != str(detailrow[11]):
                    sssat = sssat + '、' + str(detailrow[11])
                if sssun != str(detailrow[12]):
                    sssun = sssun + '、' + str(detailrow[12])
                cid = sscid
                cname = sscname
                teacher = ssteacher
                room = ssroom
                start = ssstart
                end = ssend
                mon = ssmon
                tue = sstue
                wed = sswed
                thu = ssthu
                fri = ssfri
                sat = sssat
                sun = sssun
                CLASSES.append({
                    'cid': cid,
                    'cname': cname,
                    'teacher': teacher,
                    'room': room,
                    'start': start,
                    'end': end,
                    'mon': mon,
                    'tue': tue,
                    'wed': wed,
                    'thu': thu,
                    'fri': fri,
                    'sat': sat,
                    'sun': sun
                })
            else:
                cid = sscid
                cname = sscname
                teacher = ssteacher
                room = ssroom
                start = ssstart
                end = ssend
                mon = ssmon
                tue = sstue
                wed = sswed
                thu = ssthu
                fri = ssfri
                sat = sssat
                sun = sssun
                CLASSES.append({
                    'cid': cid,
                    'cname': cname,
                    'teacher': teacher,
                    'room': room,
                    'start': start,
                    'end': end,
                    'mon': mon,
                    'tue': tue,
                    'wed': wed,
                    'thu': thu,
                    'fri': fri,
                    'sat': sat,
                    'sun': sun
                })
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
                CLASSES.append({
                    'cid': cid,
                    'cname': cname,
                    'teacher': teacher,
                    'room': room,
                    'start': start,
                    'end': end,
                    'mon': mon,
                    'tue': tue,
                    'wed': wed,
                    'thu': thu,
                    'fri': fri,
                    'sat': sat,
                    'sun': sun
                })
        i = i + 1
    cur.close()
    con.close()
    return jsonify({'allclass': CLASSES, 'length': length})


@app.route('/api/AdminOutputAllStudents', methods=['POST'])
def AdminOutputAllStudents():
    STUDENT=[]
    con = pymysql.connect(host='localhost', user='root', password='000000', database='roomSystem',
                          charset='utf8')
    cur = con.cursor()
    sql = "select * from student"
    cur.execute(sql)
    lst = cur.fetchall()
    for detailrow in lst:
        sid = detailrow[0]
        sname = detailrow[1]
        code = detailrow[2]
        STUDENT.append({'sid':sid,'sname':sname,'code':code})
    cur.close()
    con.close()
    return jsonify({'allstudent': STUDENT,'length':len(lst)})


if __name__ == '__main__':
    app.run()
