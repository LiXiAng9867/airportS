import sys
import signal
import connection
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import uic
import time
global date
date=time.strftime("%y")+time.strftime("%m")+time.strftime("%d")
print(date)
first_view="first_window.ui"
table_view="tableview.ui"
driver_view="driverView.ui"
time_view="timeView.ui"
client_view="client.ui"
signup_view="signupview.ui"
check_view="checkview.ui"
route_id=0
global userID
userID=1
Ui_MainWindow, _ = uic.loadUiType(first_view)
class firstWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(first_view, self)
        self.setWindowTitle("机场巴士票务系统")

    def msg1(self):
        # 使用infomation信息框
        QMessageBox.about(self, "提示", "购票成功")

    def msg2(self):
        # 使用infomation信息框
        QMessageBox.about(self, "提示", "没有您的信息，请注册")


class checkWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(check_view, self)
        # self.pushButton.clicked.connect(self.say)
        self.sm = QtGui.QStandardItemModel()
        self.queryTicket()
        self.setWindowTitle("机场巴士票务系统")
    def queryTicket(self):
        self.sm = QtGui.QStandardItemModel()
        global userID
        self.sm = connection.showPassengerTicket(self.sm,userID)
        self.showData()
    def delete(self):
        ticket_id = self.getTicket_id()
        connection.deleteTicket(ticket_id,userID)
        self.queryTicket()
    def getTicket_id(self):
        index = self.tableView.currentIndex().row()
        ticket_id = connection.getTicket_id(index,userID)
        return ticket_id

    def showData(self):
        # 按照编号排序
        # self.sm.sort(2, QtCore.Qt.DescendingOrder)
        print(self.sm)
        # 将数据模型绑定到QTableView
        self.tableView.setModel(self.sm)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # QTableView
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)


class signupWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(signup_view, self)
        self.setWindowTitle("机场巴士票务系统")
    def signup(self):
        UID=int(self.plainTextEdit.toPlainText())
        password=int(self.plainTextEdit.toPlainText())
        username=self.plainTextEdit.toPlainText()
        connection.signup(UID,password,username)

class clientWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(client_view, self)
        self.sm = QtGui.QStandardItemModel()
        self.prepareCombo()
        self.setWindowTitle("机场巴士票务系统")

    def prepareCombo(self):
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + time.strftime("%d"))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d")) + 1))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d")) + 2))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d")) + 3))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d")) + 4))
        self.comboBox_2.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '16', '17', '18'])

    def queryIroute(self):
        self.sm = QtGui.QStandardItemModel()
        route_id = self.comboBox.currentIndex()
        self.sm = connection.queryInnerCondition(self.sm, route_id)
        self.showData()
    def showData(self):
        self.tableView.setModel(self.sm)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
    def queryTicket(self):
        global userID
        userID=self.plainTextEdit.toPlainText()
        self.sm=connection.showPassengerTicket(self.sm,userID)
        self.showData()


class driverWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(driver_view, self)
        self.sm = QtGui.QStandardItemModel()
        self.queryIroute()
        self.prepareCombo()
        self.setWindowTitle("机场巴士票务系统")
    def prepareCombo(self):
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + time.strftime("%d"))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+1))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+2))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+3))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+4))
        self.comboBox_2.addItems(['1','2','3','4','5','6','7','8','9','10','16','17','18'])
    def queryIroute(self):
        self.sm = QtGui.QStandardItemModel()
        route_id=self.comboBox.currentIndex()
        self.sm=connection.queryInnerCondition(self.sm,route_id)
        self.showData()

    def queryTicket(self):
        global userID
        self.sm=connection.showTicket(self.sm,userID)
        self.showData()
    def showData(self):
        self.tableView.setModel(self.sm)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
    def validate(self):
        index=self.tableView.currentIndex().row()
        Tid=connection.getTicket_id(index,userID)
        connection.validate(Tid,userID)
        self.queryTicket()





class timeWindow(QMainWindow):
    global route_id
    global userID
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi(time_view, self)
        self.sm2 = QtGui.QStandardItemModel()
        self.queryTime(route_id)
        self.queryInnerRoute(route_id)
        self.iroute_id=1
        self.route_id=1
        self.seat=1
        self.setWindowTitle("机场巴士票务系统")

    def buy(self):
        global date
        if self.c1.checkState():
            flag=1
        if self.c2.checkState():
            flag=2
        if self.c3.checkState():
            flag=3
        if self.c4.checkState():
            flag=4
        if self.c5.checkState():
            flag=5
        if self.c6.checkState():
            flag=6
        if self.c7.checkState():
            flag=7
        if self.c8.checkState():
            flag=8
        if self.c9.checkState():
            flag=9
        if self.c10.checkState():
            flag=10
        if self.c11.checkState():
            flag=11
        if self.c12.checkState():
            flag=12
        if self.c13.checkState():
            flag=13
        if self.c14.checkState():
            flag=14
        if self.c15.checkState():
            flag=15
        if self.c16.checkState():
            flag=16
        if self.c17.checkState():
            flag=17
        if self.c18.checkState():
            flag=18
        if self.c19.checkState():
            flag=19
        if self.c20.checkState():
            flag=20
        if self.c21.checkState():
            flag=21
        if self.c22.checkState():
            flag=22
        if self.c23.checkState():
            flag=23
        if self.c24.checkState():
            flag=24
        if self.c25.checkState():
            flag = 25
        if self.c26.checkState():
            flag = 26
        if self.c27.checkState():
            flag = 27
        if self.c28.checkState():
            flag = 28
        if self.c29.checkState():
            flag = 29
        if self.c30.checkState():
            flag = 30
        seat = flag
        self.seat=seat
        #我写这段代码的时候内心是崩溃的，我tm也不知道pyqt有没有tag，也搞不出懒加载，如果能改成正常的我希望它能优雅一点


    def getTime(self):
        index=self.tableView.currentIndex().row()
        self.time=connection.queryTime(index+1,route_id+1)
    def getInnerRoute(self):
        index2=self.tableView_2.currentIndex().row()
        self.iroute_id=connection.queryInnerRoute(index2+1,route_id+1)
    def display(self):
        self.showInnerRoute()
        self.showTime()
    def get(self):
        self.getTime()
        self.getInnerRoute()
        seat=self.seat
        ticket_id = connection.buyTicket(self.iroute_id, self.route_id, self.time, userID, date, seat)
        self.label_3.setText(ticket_id)
    def showTime(self):
        self.queryTime(route_id+1)
        self.showData()
    def showInnerRoute(self):
        self.queryInnerRoute(route_id+1)
        self.showData()
    def queryInnerRoute(self,route_id):
        self.sm2 = QtGui.QStandardItemModel()
        self.sm2 = connection.queryInnerCondition(self.sm2, route_id)
    def queryTime(self,route_id):
        self.sm = QtGui.QStandardItemModel()
        self.sm = connection.queryTimeInnerCondition(self.sm,route_id)
    def showData(self):
        #站点table
        self.tableView_2.setModel(self.sm2)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.setColumnWidth(0, 100)
        self.tableView_2.setColumnWidth(1, 200)
        #时间table
        self.tableView.setModel(self.sm)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)



class tableWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        loadUi('tableview.ui', self)
        #self.pushButton.clicked.connect(self.say)
        self.sm = QtGui.QStandardItemModel()
        self.sm = connection.queryRouteCondition(self.sm)
        self.showData()
        self.prepareCombo()
        self.setWindowTitle("机场巴士票务系统")

    def comment(self):
        text=self.plainTextEdit.toPlainText()
        connection.comment(text,userID)

    def prepareCombo(self):
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + time.strftime("%d"))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+1))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+2))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+3))
        self.comboBox.addItem(time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d"))+4))
        self.comboBox_2.addItems(['省内线路', '省际线路', '夜间线路'])
        self.comboBox_3.addItems(['1','2','3','4','5','6','7','8','9','10','16','17','18'])

    def queryIroute(self):
        self.sm = QtGui.QStandardItemModel()
        route_id=self.comboBox_3.currentIndex()
        self.sm=connection.queryInnerCondition(self.sm,route_id)
        self.showData()

    def index(self):
        global route_id
        global date
        route_id=self.comboBox_3.currentIndex()
        if self.comboBox.currentIndex()==1:
            global date
            date = time.strftime("%y") + time.strftime("%m") + str(int(time.strftime("%d")) + 1)

    def showData(self):


        # 按照编号排序
        #self.sm.sort(2, QtCore.Qt.DescendingOrder)
        print(self.sm)
        # 将数据模型绑定到QTableView
        self.tableView.setModel(self.sm)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # QTableView
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)



class NavigateController():
    def __init__(self):
        self.firstView = firstWindow()
        self.tableView = tableWindow()
        self.driverView = driverWindow()
        self.clientView = clientWindow()
        self.timeView = timeWindow()
        self.signupView = signupWindow()
        self.checkView = checkWindow()
        self.init_slots()

    def loginEntrence(self):
        correct=0
        global userID
        userID=self.firstView.userText.toPlainText()
        password=self.firstView.passwordText.toPlainText()
        flag=1
        if self.firstView.checkBox.checkState():
            flag=1
        if self.firstView.checkBox_2.checkState():
            flag=2
        if self.firstView.checkBox_3.checkState():
            flag=3
        correct=connection.checkPassword(self,userID,password,flag)
        print(userID)
        print(password)
        print(correct)
        #if self.firstView.checkBox.checkState():
        if self.firstView.checkBox.checkState() and correct:
            self.clientView.show()
            self.firstView.hide()
        if self.firstView.checkBox_2.checkState() and correct:
            self.driverView.show()
            self.firstView.hide()
        if self.firstView.checkBox_3.checkState() and correct:
            self.tableView.show()
            self.firstView.hide()
        else :
            self.firstView.msg1()


    def init_slots(self):
        self.firstView.pushButton.clicked.connect(self.loginEntrence)
        self.firstView.signupButton_2.clicked.connect(self.signupView.show)
        self.firstView.signupButton_2.clicked.connect(self.firstView.hide)
        self.firstView.signupButton_2.clicked.connect(self.driverView.queryTicket)
        self.signupView.pushButton.clicked.connect(self.signupView.hide)
        self.signupView.pushButton.clicked.connect(self.tableView.show)
        self.signupView.pushButton.clicked.connect(self.signupView.signup)
        self.tableView.backButton.clicked.connect(self.tableView.hide)
        self.tableView.backButton.clicked.connect(self.firstView.show)
        self.driverView.backButton.clicked.connect(self.driverView.hide)
        self.driverView.backButton.clicked.connect(self.firstView.show)
        self.tableView.queryButton.clicked.connect(self.tableView.queryIroute)
        self.tableView.buyButton.clicked.connect(self.tableView.hide)
        self.tableView.buyButton.clicked.connect(self.tableView.index)
        self.tableView.buyButton.clicked.connect(self.timeView.show)
        self.tableView.buyButton.clicked.connect(self.timeView.display)
        self.tableView.checkButton.clicked.connect(self.tableView.hide)
        self.tableView.checkButton.clicked.connect(self.checkView.queryTicket)
        self.tableView.checkButton.clicked.connect(self.checkView.show)
        self.tableView.pushButton.clicked.connect(self.tableView.comment)
        self.checkView.backButton.clicked.connect(self.checkView.hide)
        self.checkView.backButton.clicked.connect(self.tableView.show)
        self.checkView.deleteButton.clicked.connect(self.checkView.delete)
        self.timeView.backButton.clicked.connect(self.timeView.hide)
        self.timeView.backButton.clicked.connect(self.tableView.show)
        self.timeView.confirmButton.clicked.connect(self.timeView.get)
        self.timeView.confirmButton.clicked.connect(self.timeView.buy)
        self.driverView.validateButton.clicked.connect(self.driverView.validate)
        self.clientView.searchButton.clicked.connect(self.clientView.queryTicket)
        self.clientView.backButton.clicked.connect(self.clientView.hide)
        self.clientView.backButton.clicked.connect(self.firstView.show)
        self.clientView.pushButton.clicked.connect(self.clientView.queryIroute)

app = QApplication(sys.argv)
window = NavigateController()
window.firstView.show()
app.exec()