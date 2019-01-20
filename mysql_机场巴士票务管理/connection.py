import pymysql	#程序包含的模块
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5 import QtGui


db = pymysql.connect('127.0.0.1', 'root', "sj15811582098","sysair")#连接数据库
cursor = db.cursor()    # 使用 cursor() 方法创建一个游标对象 cursor
#定义状态变量
#————————————————————————————————————————————————————
islogin=0
passenger_id = 0
#————————————————————————————————————————————————————
'''
sql = "select distinct dest from ROUTE as a,iroute as b where a.ROUTE_id = b.ROUTE_id"
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
results = cursor.fetchall()
for it in results:
	for i in range(len(it)):
		print (it[i],' ',end='')
	print ('\n')
'''
'''
aa=input("请输入一个字符串:")
sql="select t1.cust_numr_no from stock_fah t0 left join sale_orde t1 on t0.origin=t1.name where t0.origin='%s'"%(aa)
print(sql)
'''
#user_id=input("请输入用户ID:")
#password=input("请输入密码:")
#flag=input("工作人员或乘客或司机？")
#登陆
#----------------------------------------------------------------------
def checkPassword(self, user_id, password, flag):
    if flag == 1:
        sql = "select distinct password from client where client_id = '%s'" % (user_id)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           db.rollback()
        results = cursor.fetchall()
        print(results)
        if results!=None:
            P = results[0][0]
            if P == password:
                print ("登陆成功")
                islogin=1
                return 1
            else:
                print("登陆失败")
            return 1

    if flag == 2:
        sql = "select distinct password from driver where driver_id = '%s'" % (user_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        results = cursor.fetchall()
        if results!=None:
            P = results[0][0]
            if P == password:
                print("登陆成功")
                islogin=1
                return 1
            else:
                print("登陆失败")


    if flag == 3:
        sql = "select distinct password from passenger where passenger_id = '%s'" % (user_id)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           db.rollback()
        results = cursor.fetchall()
        if results!=None:
            P = results[0][0]
            if P == password:
                print ("登陆成功")
                islogin=1
                return 1
            else:
                print("登陆失败")

def getPassword(self, user_id, password, flag):
    if flag == 1:
        sql = "select distinct password from driver where driver_id = '%s'" % (user_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        results = cursor.fetchall()
        if results[0][0]:
            return results[0][0]
        else:
            return 0

    if flag == 2:
        sql = "select distinct password from passenger where passenger_id = '%s'" % (user_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        results = cursor.fetchall()
        if results[0][0]:
            return results[0][0]
        else:
            return 0

    if flag == 3:
        sql = "select distinct password from CLIENT where client_id = '%s'" % (user_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        results = cursor.fetchall()
        if results[0][0]:
            return results[0][0]
        else:
            return 0


def signup(userId,password,username):
    sql = "insert into passenger(passenger_id,password,passenger_name) Values('%d','%d','%s') " % (userId,password,username)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
#----------------------------------------------------------------------
#乘客查询票务
#----------------------------------------------------------------------
def comment(text,user_id):
    sql = "update passenger set passenger_req = '%s' where passenger_id = '%d'" % (text,int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
def showPassengerTicket(model,user_id):
    sql = "select * from TICKET where passenger_id = '%d'"%(int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')

    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['乘客编号', '巴士编号','司机编号','线路编号','车票编号','确认状态','日期','座位']
    model.setHorizontalHeaderLabels(title)
    return model
def queryRouteCondition(model):
    sql = "select * from route "
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    '''
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')
    '''
    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['线路', '线路名', '发车时间', '末班时间', '票价']
    model.setHorizontalHeaderLabels(title)

    return model


def queryInnerCondition(model,Rid):
    sql = "select * from iroute where route_id = '%d' "%(int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')
    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['线路号','站号', '起点', '终点', '票价']
    model.setHorizontalHeaderLabels(title)

    return model

def queryTimeInnerCondition(model,Rid):
    sql = "select distinct * from Time where route_id = '%d' "%(int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')
    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['线路','发车时间','余票']
    model.setHorizontalHeaderLabels(title)

    return model

def queryTime(index,Rid):
    sql = "select * from Time where route_id = '%d' "%(int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    time=results[index][1]


    return time


def queryInnerRoute(index,Rid):
    sql = "select * from iroute where route_id = '%d' "%(int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    iroute_id=results[index][1]
    return iroute_id


def buyTicket(IRid,Rid,time,user_id,date,seat):
    sql = "select remain from time where route_id = '%d' and time = '%s' "%(int(Rid),time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    remain=results[0][0]-1
    print (remain)
    sql = "update time set remain = '%d' where route_id = '%d' and time = '%s' " % (remain,int(Rid),time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    ticket_id = "T" + str(time) + str(IRid) + date
    print(ticket_id)

    sql = "select driver_id from timebus where route_id = '%d'"%(int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    driver_id = results[0][0]
    print(driver_id)

    sql = "select bus_id from timebus where route_id = '%d'" % (int(Rid))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    bus_id = results[0][0]
    print(bus_id)

    print(user_id)
    print(ticket_id)
    print(driver_id)
    print(bus_id)
    print(Rid)
    sql = "insert into TICKET(ticket_id,driver_id,bus_id,passenger_id,route_id,date,seat) values('%s','%d','%d','%d','%d','%s','%d')"%(ticket_id,driver_id,bus_id,int(user_id),int(Rid),date,seat)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    sql = "select * from ticket "
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('查看全部订票情况\n')
    return ticket_id

#----------------------------------------------------------------------


#司机确认票
#————————————————————————————————————————————————————————————————————————————————————————
def showTicket(model,user_id):
    sql = "select * from TICKET where driver_id = '%d'"%(int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')

    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['乘客编号', '巴士编号','司机编号','线路编号','车票编号','确认状态','日期','座位']
    model.setHorizontalHeaderLabels(title)
    return model


def getTicket(index,user_id):
    sql = "select * from TICKET where passenger_id = '%d'"%(int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    ticket_id=results[index][4]
    return ticket_id

def deleteTicket(ticket_id,userId):
    sql = "delete  from ticket where ticket_id = '%s'"%(ticket_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
def getTicket_id(index,user_id):
    sql = "select * from TICKET where driver_id = '%d'"%(int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    ticket_id=results[index][4]
    return ticket_id



def validate(Tid,user_id):
    sql = "update TICKET set validate = '确认' where ticket_id = '%s'"%(Tid)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    sql = "select * from TICKET where driver_id = '%d'" % (int(user_id))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')

#————————————————————————————————————————————————————————————————————————————————————————
#工作人员操作
# ————————————————————————————————————————————————————————————————————————————————————————
def checkPassenger(model,PID):
    sql = "select * from ticket where passenger_id = '%d'"%(int(PID))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = cursor.fetchall()
    for it in results:
        for i in range(len(it)):
            print(it[i], ' ', end='')
        print('\n')
    for row, linedata in enumerate(results):
        for col, itemdata in enumerate(linedata):
            item = QtGui.QStandardItem(str(itemdata))
            model.setItem(row, col, item)
    title = ['乘客编号', '巴士编号', '司机编号', '线路编号', '车票编号', '确认状态','日期','座位']
    model.setHorizontalHeaderLabels(title)
    return model
# ————————————————————————————————————————————————————————————————————————————————————————


