from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import logging


# Logging User
erpLogger = logging.getLogger('ERP')
erpLogger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s: %(message)s')
fileHandler = logging.FileHandler('erp.log')
fileHandler.setFormatter(formatter)
erpLogger.addHandler(fileHandler)


conn = sqlite3.connect('erp.db')
c = conn.cursor()

# with conn:
    # c.execute("CREATE TABLE customers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), department varchar(50))")
    # c.execute("CREATE TABLE suppliers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE departments(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50))")
    # c.execute("DROP TABLE customers")
    # c.execute("DROP TABLE employees")
    # c.execute("DROP TABLE suppliers")
    # c.execute("DROP TABLE departments")


class Ui_mainWindow(object):
    windowCount = 0

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(737, 511)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-4, -8, 831, 601))
        self.background.setFocusPolicy(QtCore.Qt.NoFocus)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("assets/background.png"))
        self.background.setObjectName("background")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(-1, -1, 741, 471))
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName("menubar")
        self.menuCustomers = QtWidgets.QMenu(self.menubar)
        self.menuCustomers.setObjectName("menuCustomers")
        self.menuEmployees = QtWidgets.QMenu(self.menubar)
        self.menuEmployees.setObjectName("menuEmployees")
        self.menuProducts = QtWidgets.QMenu(self.menubar)
        self.menuProducts.setObjectName("menuProducts")
        self.menuOrders = QtWidgets.QMenu(self.menubar)
        self.menuOrders.setObjectName("menuOrders")
        self.menuSuppliers = QtWidgets.QMenu(self.menubar)
        self.menuSuppliers.setObjectName("menuSuppliers")
        self.menuDepartments = QtWidgets.QMenu(self.menubar)
        self.menuDepartments.setObjectName("menuDepartments")
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        self.menuCreate_report = QtWidgets.QMenu(self.menuReports)
        self.menuCreate_report.setObjectName("menuCreate_report")
        mainWindow.setMenuBar(self.menubar)
        self.actionCreate_Customer = QtWidgets.QAction(mainWindow)
        self.actionCreate_Customer.setObjectName("actionCreate_Customer")
        self.actionView_Customers = QtWidgets.QAction(mainWindow)
        self.actionView_Customers.setObjectName("actionView_Customers")
        self.actionCreate_Employee = QtWidgets.QAction(mainWindow)
        self.actionCreate_Employee.setObjectName("actionCreate_Employee")
        self.actionView_Employees = QtWidgets.QAction(mainWindow)
        self.actionView_Employees.setObjectName("actionView_Employee")
        self.actionView_Products = QtWidgets.QAction(mainWindow)
        self.actionView_Products.setObjectName("actionView_Products")
        self.actionView_Products_2 = QtWidgets.QAction(mainWindow)
        self.actionView_Products_2.setObjectName("actionView_Products_2")
        self.actionCreate_Orders = QtWidgets.QAction(mainWindow)
        self.actionCreate_Orders.setObjectName("actionCreate_Orders")
        self.actionView_Orders = QtWidgets.QAction(mainWindow)
        self.actionView_Orders.setObjectName("actionView_Orders")
        self.actionCreate_Supplier = QtWidgets.QAction(mainWindow)
        self.actionCreate_Supplier.setObjectName("actionCreate_Supplier")
        self.actionView_Suppliers = QtWidgets.QAction(mainWindow)
        self.actionView_Suppliers.setObjectName("actionView_Supplier")
        self.actionCreate_Department = QtWidgets.QAction(mainWindow)
        self.actionCreate_Department.setObjectName("actionCreate_Department")
        self.actionView_Departments = QtWidgets.QAction(mainWindow)
        self.actionView_Departments.setObjectName("actionView_Department")
        self.actionView_reports = QtWidgets.QAction(mainWindow)
        self.actionView_reports.setObjectName("actionView_reports")
        self.actionPrint_report = QtWidgets.QAction(mainWindow)
        self.actionPrint_report.setObjectName("actionPrint_report")
        self.actionRevenue_per_Customer = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Customer.setObjectName("actionRevenue_per_Customer")
        self.actionRevenue_per_Product = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Product.setObjectName("actionRevenue_per_Product")
        self.actionRevenue_per_Supplier = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Supplier.setObjectName("actionRevenue_per_Supplier")
        self.menuCustomers.addAction(self.actionCreate_Customer)
        self.menuCustomers.addAction(self.actionView_Customers)
        self.menuEmployees.addAction(self.actionCreate_Employee)
        self.menuEmployees.addAction(self.actionView_Employees)
        self.menuProducts.addAction(self.actionView_Products)
        self.menuProducts.addAction(self.actionView_Products_2)
        self.menuOrders.addAction(self.actionCreate_Orders)
        self.menuOrders.addAction(self.actionView_Orders)
        self.menuSuppliers.addAction(self.actionCreate_Supplier)
        self.menuSuppliers.addAction(self.actionView_Suppliers)
        self.menuDepartments.addAction(self.actionCreate_Department)
        self.menuDepartments.addAction(self.actionView_Departments)
        self.menuCreate_report.addAction(self.actionRevenue_per_Customer)
        self.menuCreate_report.addAction(self.actionRevenue_per_Product)
        self.menuCreate_report.addAction(self.actionRevenue_per_Supplier)
        self.menuReports.addAction(self.menuCreate_report.menuAction())
        self.menuReports.addAction(self.actionView_reports)
        self.menuReports.addAction(self.actionPrint_report)
        self.menubar.addAction(self.menuCustomers.menuAction())
        self.menubar.addAction(self.menuEmployees.menuAction())
        self.menubar.addAction(self.menuProducts.menuAction())
        self.menubar.addAction(self.menuSuppliers.menuAction())
        self.menubar.addAction(self.menuOrders.menuAction())
        self.menubar.addAction(self.menuDepartments.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())

        self.actionCreate_Customer.triggered.connect(lambda: self.createWindow('customers'))
        self.actionCreate_Employee.triggered.connect(lambda: self.createWindow('employees'))
        self.actionCreate_Supplier.triggered.connect(lambda: self.createWindow('suppliers'))
        self.actionCreate_Department.triggered.connect(lambda: self.createWindow('departments'))
        self.actionView_Customers.triggered.connect(self.viewCustomers)
        self.actionView_Employees.triggered.connect(self.viewEmployees)
        self.actionView_Suppliers.triggered.connect(self.viewSuppliers)
        self.actionView_Departments.triggered.connect(self.viewDepartments)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def createWindow(self, table):
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(300, 200)
        sub.setWindowTitle(f"Create {table}")
        if table == 'customers' or table == 'employees' or table == 'suppliers':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            label2 = QtWidgets.QLabel("Email:", sub)
            label3 = QtWidgets.QLabel("Phone Number:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit2 = QtWidgets.QLineEdit(sub)
            lineEdit3 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.addInfotoDB(table, lineEdit.text(), lineEdit2.text(), lineEdit3.text()))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label2.setFont(font)
            label2.setGeometry(QtCore.QRect(40, 80, 81, 21))
            label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label3.setFont(font)
            label3.setGeometry(QtCore.QRect(20, 120, 111, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            lineEdit2.setGeometry(QtCore.QRect(140, 80, 113, 20))
            lineEdit3.setGeometry(QtCore.QRect(140, 120, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
            
        elif table == 'departments':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.addInfotoDB('departments', lineEdit, None, None))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
        
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def viewCustomers(self):
        Ui_mainWindow.windowCount += 1
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(440, 260)
        sub.setWindowTitle("View Customers")

        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setObjectName("tableWidget")
        tableWidget.setColumnCount(4)
        tableWidget.setRowCount(0)
        headers = ["ID", "Name", "Email", "Phone"]
        tableWidget.setHorizontalHeaderLabels(headers)
        lineEdit = QtWidgets.QLineEdit(sub)
        lineEdit_2 = QtWidgets.QLineEdit(sub)
        lineEdit_3 = QtWidgets.QLineEdit(sub)
        pushButton = QtWidgets.QPushButton("Search", sub)
        tableWidget.setGeometry(QtCore.QRect(15, 70, 411, 171))
        lineEdit.setGeometry(QtCore.QRect(15, 40, 91, 20))
        lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
        lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
        pushButton.setGeometry(QtCore.QRect(315, 40, 111, 23))
        lineEdit.setPlaceholderText("Search by name")
        lineEdit_2.setPlaceholderText("Search by email")
        lineEdit_3.setPlaceholderText("search by phone")
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.viewInfo('customers', tableWidget)

        self.mdiArea.addSubWindow(sub)
        
        sub.show()

    def viewEmployees(self):
        Ui_mainWindow.windowCount += 1
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(440, 260)
        sub.setWindowTitle("View Employees")

        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setObjectName("tableWidget")
        tableWidget.setColumnCount(4)
        tableWidget.setRowCount(0)
        headers = ["ID", "Name", "Email", "Phone"]
        tableWidget.setHorizontalHeaderLabels(headers)
        lineEdit = QtWidgets.QLineEdit(sub)
        lineEdit_2 = QtWidgets.QLineEdit(sub)
        lineEdit_3 = QtWidgets.QLineEdit(sub)
        pushButton = QtWidgets.QPushButton("Search", sub)
        tableWidget.setGeometry(QtCore.QRect(15, 70, 411, 171))
        lineEdit.setGeometry(QtCore.QRect(15, 40, 91, 20))
        lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
        lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
        pushButton.setGeometry(QtCore.QRect(315, 40, 111, 23))
        lineEdit.setPlaceholderText("Search by name")
        lineEdit_2.setPlaceholderText("Search by email")
        lineEdit_3.setPlaceholderText("search by phone")
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.viewInfo('employees', tableWidget)

        self.mdiArea.addSubWindow(sub)
        
        sub.show()

    def viewSuppliers(self):
        Ui_mainWindow.windowCount += 1
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(440, 260)
        sub.setWindowTitle("View Suppliers")

        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setObjectName("tableWidget")
        tableWidget.setColumnCount(4)
        tableWidget.setRowCount(0)
        headers = ["ID", "Name", "Email", "Phone"]
        tableWidget.setHorizontalHeaderLabels(headers)
        lineEdit = QtWidgets.QLineEdit(sub)
        lineEdit_2 = QtWidgets.QLineEdit(sub)
        lineEdit_3 = QtWidgets.QLineEdit(sub)
        pushButton = QtWidgets.QPushButton("Search", sub)
        tableWidget.setGeometry(QtCore.QRect(15, 70, 411, 171))
        lineEdit.setGeometry(QtCore.QRect(15, 40, 91, 20))
        lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
        lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
        pushButton.setGeometry(QtCore.QRect(315, 40, 111, 23))
        lineEdit.setPlaceholderText("Search by name")
        lineEdit_2.setPlaceholderText("Search by email")
        lineEdit_3.setPlaceholderText("search by phone")
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.viewInfo('suppliers', tableWidget)

        self.mdiArea.addSubWindow(sub)
        
        sub.show()

    def viewDepartments(self):
        Ui_mainWindow.windowCount += 1
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(440, 260)
        sub.setWindowTitle("View Suppliers")

        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setObjectName("tableWidget")
        tableWidget.setColumnCount(3)
        tableWidget.setRowCount(0)
        headers = ["ID", "Name", "Number of Employees"]
        tableWidget.setHorizontalHeaderLabels(headers)
        lineEdit = QtWidgets.QLineEdit(sub)
        lineEdit_2 = QtWidgets.QLineEdit(sub)
        lineEdit_3 = QtWidgets.QLineEdit(sub)
        pushButton = QtWidgets.QPushButton("Search", sub)
        tableWidget.setGeometry(QtCore.QRect(15, 70, 411, 171))
        lineEdit.setGeometry(QtCore.QRect(15, 40, 91, 20))
        lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
        lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
        pushButton.setGeometry(QtCore.QRect(315, 40, 111, 23))
        lineEdit.setPlaceholderText("Search by name")
        lineEdit_2.setPlaceholderText("Search by email")
        lineEdit_3.setPlaceholderText("search by phone")
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.viewInfo('departments', tableWidget)

        self.mdiArea.addSubWindow(sub)
        
        sub.show()

    def addInfotoDB(self, table, name, email, phone_department):
        with conn:
            try:
                if table == 'customers' or table == 'suppliers':
                    c.execute(f"INSERT INTO {table} (name, email, phone) VALUES ('{name.text()}', '{email.text()}', '{phone_department.text()}')")
                    c.execute(f"SELECT * FROM {table}")
                    print(c.fetchall())
                    name.clear()
                    email.clear()
                    phone_department.clear()
                elif table == 'employees':
                    c.execute("SELECT name FROM departments")
                    if phone_department not in c.fetchall():
                        self.errorPopup('departmentError')
                    else:
                        c.execute(f"INSERT INTO {table} (name, email, department) VALUES ('{name.text()}', '{email.text()}', '{phone_department.text()}')")
                        c.execute(f"SELECT * FROM {table}")
                        print(c.fetchall())
                        name.clear()
                        email.clear()
                        phone_department.clear()
                elif table == 'departments':
                    c.execute("SELECT names FROM departments")
                    departments = c.fetchall()
                    for department in departments:
                        print(department[0])
                        if department[0] == name:
                            self.errorPopup('departmentExists')
                        else:
                            c.execute(f"INSERT INTO {table} (name) VALUES ('{name.text()}')")
                    name.clear()

            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")

    def viewInfo(self, dbTable, table):
        if dbTable == 'departments':
            with conn:
                c.execute(f"SELECT departments.ID, departments.name, COUNT(employees.ID) FROM departments JOIN employees ON departments.name = employees.department")
                print(c.fetchall())
        with conn:
            c.execute(f"SELECT * FROM {dbTable}")
        table.setRowCount(0)
        for data in c.fetchall():
            row_index = table.rowCount()
            for column_index, data in enumerate(data):
                data = str(data)
                table.setRowCount(row_index+1)
                table.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))

    def errorPopup(self, reason):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        if reason == 'departmentError':
            msg.setText("Department not found.")
        elif reason == 'departmentExists':
            msg.setText("Department already exists.")
        show = msg.exec_()     


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.menuCustomers.setTitle(_translate("mainWindow", "Customers"))
        self.menuEmployees.setTitle(_translate("mainWindow", "Employees"))
        self.menuProducts.setTitle(_translate("mainWindow", "Products"))
        self.menuOrders.setTitle(_translate("mainWindow", "Orders"))
        self.menuSuppliers.setTitle(_translate("mainWindow", "Suppliers"))
        self.menuDepartments.setTitle(_translate("mainWindow", "Departments"))
        self.menuReports.setTitle(_translate("mainWindow", "Reports"))
        self.menuCreate_report.setTitle(_translate("mainWindow", "Create report"))
        self.actionCreate_Customer.setText(_translate("mainWindow", "Create Customer"))
        self.actionView_Customers.setText(_translate("mainWindow", "View Customers"))
        self.actionCreate_Employee.setText(_translate("mainWindow", "Create Employee"))
        self.actionView_Employees.setText(_translate("mainWindow", "View Employee"))
        self.actionView_Products.setText(_translate("mainWindow", "Create Products"))
        self.actionView_Products_2.setText(_translate("mainWindow", "View Products"))
        self.actionCreate_Orders.setText(_translate("mainWindow", "Create Order"))
        self.actionView_Orders.setText(_translate("mainWindow", "View Orders"))
        self.actionCreate_Supplier.setText(_translate("mainWindow", "Create Supplier"))
        self.actionView_Suppliers.setText(_translate("mainWindow", "View Supplier"))
        self.actionCreate_Department.setText(_translate("mainWindow", "Create Department"))
        self.actionView_Departments.setText(_translate("mainWindow", "View Department"))
        self.actionView_reports.setText(_translate("mainWindow", "View reports"))
        self.actionPrint_report.setText(_translate("mainWindow", "Print report"))
        self.actionRevenue_per_Customer.setText(_translate("mainWindow", "Revenue per Customer"))
        self.actionRevenue_per_Product.setText(_translate("mainWindow", "Revenue per Product"))
        self.actionRevenue_per_Supplier.setText(_translate("mainWindow", "Revenue per Supplier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
