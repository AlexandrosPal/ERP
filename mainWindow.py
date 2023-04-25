from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import logging
import datetime
import random


# Logging User
erpLogger = logging.getLogger('ERP')
erpLogger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s: %(message)s')
fileHandler = logging.FileHandler('erp.log')
fileHandler.setFormatter(formatter)
erpLogger.addHandler(fileHandler)

conn = sqlite3.connect('erp.db')
c = conn.cursor()


with conn:
    # c.execute("CREATE TABLE customers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), department varchar(50), pay INTEGER)")
    # c.execute("CREATE TABLE suppliers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE departments(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50))")
    # c.execute("CREATE TABLE products(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), category varchar(50), price INTEGER, supplier varchar(50))")
    # c.execute("CREATE TABLE orders(ID INTEGER PRIMARY KEY AUTOINCREMENT, customer varchar(50), product varchar(50), quantity INTEGER, date DATE)")
    # c.execute("CREATE TABLE company(name varchar(50), adress varchar(50), ssn INTEGER, type varchar(50), number INTEGER, email varchar(50), category varchar(50), capital INTEGER)")
    # c.execute("CREATE TABLE reports(name varchar(50), number INTEGER)")
    # c.execute("DROP TABLE customers")
    # c.execute("DROP TABLE employees")
    # c.execute("DROP TABLE suppliers")
    # c.execute("DROP TABLE departments")
    # c.execute("DROP TABLE products")
    # c.execute("DROP TABLE orders")
    # c.execute("DROP TABLE company")
    # c.execute("DROP TABLE reports")
    # c.execute("SELECT * FROM reports")
    # c.execute("SELECT * FROM company")
    # print(c.fetchall())
    pass
 

class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setFixedSize(737, 511)
        mainWindow.setWindowIcon(QtGui.QIcon('assets/icon.png'))
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
        self.menuCompany = QtWidgets.QMenu(self.menubar)
        self.menuCompany.setObjectName("Setup_Company")
        mainWindow.setMenuBar(self.menubar)
        self.actionCreate_Customer = QtWidgets.QAction(mainWindow)
        self.actionCreate_Customer.setObjectName("actionCreate_Customer")
        self.actionView_Customers = QtWidgets.QAction(mainWindow)
        self.actionView_Customers.setObjectName("actionView_Customers")
        self.actionCreate_Employee = QtWidgets.QAction(mainWindow)
        self.actionCreate_Employee.setObjectName("actionCreate_Employee")
        self.actionView_Employees = QtWidgets.QAction(mainWindow)
        self.actionView_Employees.setObjectName("actionView_Employee")
        self.actionCreate_Product = QtWidgets.QAction(mainWindow)
        self.actionCreate_Product.setObjectName("actionCreate_Product")
        self.actionView_Products = QtWidgets.QAction(mainWindow)
        self.actionView_Products.setObjectName("actionView_Products")
        self.actionCreate_Order = QtWidgets.QAction(mainWindow)
        self.actionCreate_Order.setObjectName("actionCreate_Order")
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
        self.actionBalance_Sheet = QtWidgets.QAction(mainWindow)
        self.actionBalance_Sheet.setObjectName("actionBalance_Sheet")
        self.actionSetup_Company = QtWidgets.QAction(mainWindow)
        self.actionSetup_Company.setObjectName("actionSetup_Company")
        self.actionView_Information = QtWidgets.QAction(mainWindow)
        self.actionView_Information.setObjectName("actionInformation")
        self.actionAdd_Capital = QtWidgets.QAction(mainWindow)
        self.actionAdd_Capital.setObjectName("actionAdd_Capital")
        self.menuCustomers.addAction(self.actionCreate_Customer)
        self.menuCustomers.addAction(self.actionView_Customers)
        self.menuEmployees.addAction(self.actionCreate_Employee)
        self.menuEmployees.addAction(self.actionView_Employees)
        self.menuProducts.addAction(self.actionCreate_Product)
        self.menuProducts.addAction(self.actionView_Products)
        self.menuOrders.addAction(self.actionCreate_Order)
        self.menuOrders.addAction(self.actionView_Orders)
        self.menuSuppliers.addAction(self.actionCreate_Supplier)
        self.menuSuppliers.addAction(self.actionView_Suppliers)
        self.menuDepartments.addAction(self.actionCreate_Department)
        self.menuDepartments.addAction(self.actionView_Departments)
        self.menuCreate_report.addAction(self.actionBalance_Sheet)
        self.menuCreate_report.addSeparator()
        self.menuCreate_report.addAction(self.actionRevenue_per_Customer)
        self.menuCreate_report.addAction(self.actionRevenue_per_Product)
        self.menuCreate_report.addAction(self.actionRevenue_per_Supplier)
        self.menuReports.addAction(self.menuCreate_report.menuAction())
        self.menuReports.addAction(self.actionView_reports)
        self.menuReports.addAction(self.actionPrint_report)
        self.menubar.addAction(self.menuCustomers.menuAction())
        self.menubar.addAction(self.menuEmployees.menuAction())
        self.menubar.addAction(self.menuSuppliers.menuAction())
        self.menubar.addAction(self.menuProducts.menuAction())
        self.menubar.addAction(self.menuOrders.menuAction())
        self.menubar.addAction(self.menuDepartments.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuCompany.menuAction())
        self.menuCompany.addAction(self.actionSetup_Company)
        self.menuCompany.addAction(self.actionView_Information)
        self.menuCompany.addAction(self.actionAdd_Capital)

        self.actionCreate_Customer.triggered.connect(lambda: self.createWindow('customers'))
        self.actionCreate_Employee.triggered.connect(lambda: self.createWindow('employees'))
        self.actionCreate_Supplier.triggered.connect(lambda: self.createWindow('suppliers'))
        self.actionCreate_Department.triggered.connect(lambda: self.createWindow('departments'))
        self.actionCreate_Product.triggered.connect(lambda: self.createWindow('products'))
        self.actionCreate_Order.triggered.connect(lambda: self.createWindow('orders'))
        self.actionView_Customers.triggered.connect(lambda: self.viewWindow('customers'))
        self.actionView_Employees.triggered.connect(lambda: self.viewWindow('employees'))
        self.actionView_Suppliers.triggered.connect(lambda: self.viewWindow('suppliers'))
        self.actionView_Departments.triggered.connect(lambda: self.viewWindow('departments'))
        self.actionView_Products.triggered.connect(lambda: self.viewWindow('products'))
        self.actionView_Orders.triggered.connect(lambda: self.viewWindow('orders'))
        self.actionRevenue_per_Customer.triggered.connect(lambda: self.createReport('revenueCustomer'))
        self.actionRevenue_per_Product.triggered.connect(lambda: self.createReport('revenueProduct'))
        self.actionRevenue_per_Supplier.triggered.connect(lambda: self.createReport('revenueSupplier'))
        self.actionBalance_Sheet.triggered.connect(lambda: self.createReport('BalanceSheet'))
        self.actionView_reports.triggered.connect(lambda: self.viewReports())
        self.actionSetup_Company.triggered.connect(lambda: self.company('setup'))
        self.actionView_Information.triggered.connect(lambda: self.company('information'))
        self.actionAdd_Capital.triggered.connect(lambda: self.company('capital'))
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        try:
            with conn:
                c.execute("SELECT * FROM company")
                self.actionSetup_Company.setEnabled(False)

        except sqlite3.DatabaseError:
            self.actionCreate_Customer.setEnabled(False)
            self.menuCustomers.setEnabled(False)
            self.menuEmployees.setEnabled(False)
            self.menuProducts.setEnabled(False)
            self.menuOrders.setEnabled(False)
            self.menuSuppliers.setEnabled(False)
            self.menuDepartments.setEnabled(False)
            self.menuReports.setEnabled(False)
            self.actionView_Information.setEnabled(False)
            self.actionAdd_Capital.setEnabled(False)
            

    def createWindow(self, table):
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(300, 200)
        sub.setWindowTitle(f"Create {table}")

        if table == 'customers' or table == 'suppliers':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            label2 = QtWidgets.QLabel("Email:", sub)
            label3 = QtWidgets.QLabel("Phone Number:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit2 = QtWidgets.QLineEdit(sub)
            lineEdit3 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.insertInfo(table, lineEdit, lineEdit2, lineEdit3))

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
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            
        elif table == 'employees':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            label2 = QtWidgets.QLabel("Email:", sub)
            label3 = QtWidgets.QLabel("Department:", sub)
            label4 = QtWidgets.QLabel("Monthly Pay:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit2 = QtWidgets.QLineEdit(sub)
            lineEdit3 = QtWidgets.QLineEdit(sub)
            lineEdit4 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.insertInfo(table, lineEdit, lineEdit2, lineEdit3, lineEdit4))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label2.setFont(font)
            label2.setGeometry(QtCore.QRect(40, 70, 81, 21))
            label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label3.setFont(font)
            label3.setGeometry(QtCore.QRect(10, 100, 111, 21))
            label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label4.setFont(font)
            label4.setGeometry(QtCore.QRect(10, 130, 111, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            lineEdit2.setGeometry(QtCore.QRect(140, 70, 113, 20))
            lineEdit3.setGeometry(QtCore.QRect(140, 100, 113, 20))
            lineEdit4.setGeometry(QtCore.QRect(140, 130, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        elif table == 'departments':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.insertInfo(table, lineEdit))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

            self.mdiArea.addSubWindow(sub)
            sub.show()

        elif table == 'products':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Name:", sub)
            label2 = QtWidgets.QLabel("Category:", sub)
            label3 = QtWidgets.QLabel("Price:", sub)
            label4 = QtWidgets.QLabel("Supplier:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit2 = QtWidgets.QLineEdit(sub)
            lineEdit3 = QtWidgets.QLineEdit(sub)
            lineEdit4 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.insertInfo(table, lineEdit, lineEdit2, lineEdit3, lineEdit4))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label2.setFont(font)
            label2.setGeometry(QtCore.QRect(40, 70, 81, 21))
            label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label3.setFont(font)
            label3.setGeometry(QtCore.QRect(10, 100, 111, 21))
            label4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label4.setFont(font)
            label4.setGeometry(QtCore.QRect(10, 130, 111, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            lineEdit2.setGeometry(QtCore.QRect(140, 70, 113, 20))
            lineEdit3.setGeometry(QtCore.QRect(140, 100, 113, 20))
            lineEdit4.setGeometry(QtCore.QRect(140, 130, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        elif table == 'orders':
            font = QtGui.QFont()
            font.setPointSize(12)
            label = QtWidgets.QLabel("Customer:", sub)
            label2 = QtWidgets.QLabel("Product:", sub)
            label3 = QtWidgets.QLabel("Quantity:", sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit2 = QtWidgets.QLineEdit(sub)
            lineEdit3 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Create", sub, clicked = lambda: self.insertInfo(table, lineEdit, lineEdit2, lineEdit3))

            label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label.setFont(font)
            label.setGeometry(QtCore.QRect(40, 40, 81, 21))
            label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label2.setFont(font)
            label2.setGeometry(QtCore.QRect(40, 80, 81, 21))
            label3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            label3.setFont(font)
            label3.setGeometry(QtCore.QRect(10, 120, 111, 21))
            lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
            lineEdit2.setGeometry(QtCore.QRect(140, 80, 113, 20))
            lineEdit3.setGeometry(QtCore.QRect(140, 120, 113, 20))
            pushButton.setGeometry(QtCore.QRect(70, 160, 161, 23))
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.mdiArea.addSubWindow(sub)
        sub.show()

    def viewWindow(self, table):
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(440, 260)
        sub.setWindowTitle(f"View {table}")

        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setObjectName("tableWidget")
        tableWidget.setRowCount(0)
        lineEdit = QtWidgets.QLineEdit(sub)
        pushButton = QtWidgets.QPushButton("Search", sub)
        tableWidget.setGeometry(QtCore.QRect(15, 70, 411, 171))
        lineEdit.setGeometry(QtCore.QRect(15, 40, 91, 20))
        pushButton.setGeometry(QtCore.QRect(315, 40, 111, 23))
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        if table == 'customers' or table == 'suppliers':
            lineEdit_2 = QtWidgets.QLineEdit(sub)
            lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
            lineEdit_3 = QtWidgets.QLineEdit(sub)
            lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
            tableWidget.setColumnCount(4)
            headers = ["ID", "Name", "Email", "Phone"]
            lineEdit.setPlaceholderText("Search by name")
            lineEdit_2.setPlaceholderText("Search by email")
            lineEdit_3.setPlaceholderText("search by phone")
            pushButton.clicked.connect(lambda: self.filterView(table, tableWidget, lineEdit, lineEdit_2, lineEdit_3))
        elif table == 'employees':
            lineEdit_2 = QtWidgets.QLineEdit(sub)
            lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
            lineEdit_3 = QtWidgets.QLineEdit(sub)
            lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
            tableWidget.setColumnCount(5)
            headers = ["ID", "Name", "Email", "Department", "Pay"]
            lineEdit.setPlaceholderText("Search by name")
            lineEdit_2.setPlaceholderText("Search by email")
            lineEdit_3.setPlaceholderText("search by department")
            pushButton.clicked.connect(lambda: self.filterView(table, tableWidget, lineEdit, lineEdit_2, lineEdit_3))
        elif table == 'departments':
            tableWidget.setColumnCount(3)
            headers = ["ID", "Name", "Employees"]
            lineEdit.setPlaceholderText("Search by name")
            pushButton.clicked.connect(lambda: self.filterView(table, tableWidget, lineEdit))
        elif table == 'products':
            lineEdit_2 = QtWidgets.QLineEdit(sub)
            lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
            lineEdit_3 = QtWidgets.QLineEdit(sub)
            lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
            tableWidget.setColumnCount(5)
            headers = ["ID", "Name", "Category", "Price", "Supplier"]
            lineEdit.setPlaceholderText("Search by name")
            lineEdit_2.setPlaceholderText("Search by category")
            lineEdit_3.setPlaceholderText("search by supplier")
            pushButton.clicked.connect(lambda: self.filterView(table, tableWidget, lineEdit, lineEdit_2, lineEdit_3))
        elif table == 'orders':
            lineEdit_2 = QtWidgets.QLineEdit(sub)
            lineEdit_2.setGeometry(QtCore.QRect(115, 40, 91, 20))
            lineEdit_3 = QtWidgets.QLineEdit(sub)
            lineEdit_3.setGeometry(QtCore.QRect(215, 40, 91, 20))
            tableWidget.setColumnCount(6)
            headers = ["ID", "Customer", "Product", "Quantity", "Date", "Total Price"]
            lineEdit.setPlaceholderText("Search by customer")
            lineEdit_2.setPlaceholderText("Search by product")
            lineEdit_3.setPlaceholderText("search by date")
            pushButton.clicked.connect(lambda: self.filterView(table, tableWidget, lineEdit, lineEdit_2, lineEdit_3))
        tableWidget.setHorizontalHeaderLabels(headers)

        self.viewInfo(table, tableWidget)
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def insertInfo(self, table, *args):
        try:
            if table == 'customers' or table == 'suppliers':
                name, email, phone = args
                with conn:
                        c.execute(f"INSERT INTO {table} (name, email, phone) VALUES ('{name.text()}', '{email.text()}', '{phone.text()}')")
                        c.execute(f"SELECT * FROM {table}")
                name.clear()
                email.clear()
                phone.clear()

            elif table == 'employees':
                name, email, department, pay = args
                with conn:
                    c.execute("SELECT name FROM departments")
                departments = c.fetchall()
                state = True
                for listedDepartment in departments:
                    if listedDepartment[0] != department.text():
                        state = False
                    else:
                        state = True
                        break
                if state:
                    with conn:
                        annualPay = int(pay.text())
                        c.execute(f"INSERT INTO {table} (name, email, department, pay) VALUES ('{name.text()}', '{email.text()}', '{department.text()}', '{annualPay:,}')")
                    name.clear()
                    email.clear()
                    department.clear()
                    pay.clear()
                else:
                    self.errorPopup('departmentError')

            elif table == 'departments':
                name = args[0]
                with conn:
                        c.execute("SELECT name FROM departments")
                departments = c.fetchall()
                if departments == []:
                    with conn:
                        c.execute(f"INSERT INTO {table} (name) VALUES ('{name.text()}')")
                        name.clear()
                
                else:  
                    for department in departments:
                        if department[0].lower() == name.text().lower():
                            self.errorPopup('departmentExists')
                            break
                        else:
                            with conn:
                                c.execute(f"INSERT INTO {table} (name) VALUES ('{name.text()}')")
                                name.clear()
                                break

            elif table == 'products':
                name, category, price, supplier = args
                with conn:
                    c.execute("SELECT name FROM suppliers")
                suppliers = c.fetchall()
                state = True
                for listedSupplier in suppliers:
                    if listedSupplier[0] != supplier.text():
                        state = False
                    else:
                        state = True
                        break
                if state:
                    print(state)
                    print(name.text(), category.text(), price.text(), supplier.text())
                    with conn:
                        c.execute(f"INSERT INTO {table} (name, category, price, supplier) VALUES ('{name.text()}', '{category.text()}', '{price.text()}', '{supplier.text()}')")
                    name.clear()
                    category.clear()
                    price.clear()
                    supplier.clear()
                else:
                    self.errorPopup('supplierError')

            elif table == 'orders':
                customer, product, quantity = args
                try:
                    quantityTest = int(quantity.text())
                except:
                    self.errorPopup('quantityValueError')
                    return False
                with conn:
                    c.execute("SELECT name FROM customers")
                customers = c.fetchall()
                stateCustomer = True
                stateProduct = True
                for listedCustomer in customers:
                    if listedCustomer[0] != customer.text():
                        stateCustomer = False
                    else:
                        stateCustomer = True
                        break
                with conn:
                    c.execute("SELECT name FROM products")
                products = c.fetchall()
                for listedProduct in products:
                    if listedProduct[0] != product.text():
                        stateProduct = False
                    else:
                        stateProduct = True
                        break
                if stateCustomer:
                    if stateProduct:
                        with conn:
                            date = datetime.date.today().strftime('%d-%m-%Y')
                            c.execute(f"INSERT INTO orders (customer, product, quantity, date) VALUES ('{customer.text()}', '{product.text()}', '{quantity.text()}', '{date}')")
                        customer.clear()
                        product.clear()
                        quantity.clear()
                    else:
                        self.errorPopup('productError')
                else:
                    self.errorPopup('customerError')

        except sqlite3.DatabaseError as e:
            erpLogger.info(f"Problem faced: {e}")

    def viewInfo(self, table, tableWidget):
        if table == 'departments':
            with conn:
                c.execute("SELECT departments.ID, departments.name, COUNT(employees.ID) FROM departments LEFT JOIN employees ON departments.name = employees.department GROUP BY departments.ID")
                tableWidget.setRowCount(0)
                for data in c.fetchall():
                    row_index = tableWidget.rowCount()
                    for column_index, data in enumerate(data):
                        data = str(data)
                        tableWidget.setRowCount(row_index+1)
                        tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))

            header = tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
            for index in range(3):
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        elif table == 'orders':
            with conn:
                c.execute("SELECT orders.ID, orders.customer, orders.product, orders.quantity, orders.date, (products.price * orders.quantity) FROM orders JOIN products ON orders.product = products.name GROUP by orders.ID")
                tableWidget.setRowCount(0)
                for data in c.fetchall():
                    row_index = tableWidget.rowCount()
                    for column_index, data in enumerate(data):
                        data = str(data)
                        tableWidget.setRowCount(row_index+1)
                        tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))
            
            header = tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
            for index in range(5):
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        else:
            with conn:
                c.execute(f"SELECT * FROM {table}")
                tableWidget.setRowCount(0)
                for data in c.fetchall():
                    row_index = tableWidget.rowCount()
                    for column_index, data in enumerate(data):
                        data = str(data)
                        tableWidget.setRowCount(row_index+1)
                        tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))

            header = tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
            for index in range(4):
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def filterView(self, table, tableWidget, *args):
        if table == 'customers' or table == 'suppliers':
            try:
                name, email, phone = args
                if name.text() != '' and email.text() == '' and phone.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}'")

                elif name.text() == '' and email.text() != '' and phone.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE email = '{email.text()}'")

                elif name.text() == '' and email.text() == '' and phone.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE phone = '{phone.text()}'")

                elif name.text() != '' and email.text() != '' and phone.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND email = '{email.text()}'")

                elif name.text() == '' and email.text() != '' and phone.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE email = '{email.text()}' AND phone = '{phone.text()}'")

                elif name.text() != '' and email.text() == '' and phone.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND phone = '{phone.text()}'")

                elif name.text() != '' and email.text() != '' and phone.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND email = '{email.text()}' AND phone = '{phone.text()}'")

                elif name.text() == '' and email.text() == '' and phone.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table}")
                
            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")
        
        elif table == 'employees':
            try:
                name, email, department = args
                if name.text() != '' and email.text() == '' and department.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}'")

                elif name.text() == '' and email.text() != '' and department.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE email = '{email.text()}'")

                elif name.text() == '' and email.text() == '' and department.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE department = '{department.text()}'")

                elif name.text() != '' and email.text() != '' and department.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND email = '{email.text()}'")

                elif name.text() == '' and email.text() != '' and department.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE email = '{email.text()}' AND department = '{department.text()}'")

                elif name.text() != '' and email.text() == '' and department.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND department = '{department.text()}'")

                elif name.text() != '' and email.text() != '' and department.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE name = '{name.text()}' AND email = '{email.text()}' AND department = '{department.text()}'")

                elif name.text() == '' and email.text() == '' and department.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table}")
                
            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")

        elif table == 'departments':
            try:
                name = args[0]
                if name.text() != '':
                    with conn:
                        c.execute(f"SELECT departments.ID, departments.name, COUNT(employees.ID) FROM departments LEFT JOIN employees ON departments.name = employees.department WHERE departments.name = '{name.text()}' GROUP BY departments.ID")

                elif name.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table}")
                
            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")

        elif table == 'orders':
            customer, product, date = args
            try:
                if customer.text() != '' and product.text() == '' and date.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE customer = '{customer.text()}'")

                elif customer.text() == '' and product.text() != '' and date.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE product = '{product.text()}'")

                elif customer.text() == '' and product.text() == '' and date.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE date = '{date.text()}'")

                elif customer.text() != '' and product.text() != '' and date.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE customer = '{customer.text()}' AND product = '{product.text()}'")

                elif customer.text() == '' and product.text() != '' and date.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE product = '{product.text()}' AND date = '{date.text()}'")

                elif customer.text() != '' and product.text() == '' and date.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE customer = '{customer.text()}' AND date = '{date.text()}'")

                elif customer.text() != '' and product.text() != '' and date.text() != '':
                    with conn:
                        c.execute(f"SELECT * FROM {table} WHERE customer = '{customer.text()}' AND product = '{product.text()}' AND date = '{date.text()}'")

                elif customer.text() == '' and product.text() == '' and date.text() == '':
                    with conn:
                        c.execute(f"SELECT * FROM {table}")
                
                
            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")
        
        tableWidget.setRowCount(0)
        for data in c.fetchall():
            row_index = tableWidget.rowCount()
            for column_index, data in enumerate(data):
                data = str(data)
                tableWidget.setRowCount(row_index+1)
                tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))

    def createReport(self, type):
        if type == 'revenueCustomer' or type == 'revenueProduct' or type == 'revenueSupplier':
            sub = QtWidgets.QMdiSubWindow()
            sub.setFixedSize(490, 300)
            sub.setWindowTitle("Report")

            font8 = QtGui.QFont()
            font8.setPointSize(8)
            font10 = QtGui.QFont()
            font10.setPointSize(10)

            label = QtWidgets.QLabel(sub)
            label_2 = QtWidgets.QLabel(sub)
            label_3 = QtWidgets.QLabel(sub)
            label_4 = QtWidgets.QLabel(sub)
            pushButton = QtWidgets.QPushButton("Save", sub)
            tableWidget = QtWidgets.QTableWidget(sub)
            tableWidget.setColumnCount(3)
            tableWidget.setRowCount(0)

            headers = ["ID", "Name", "Revenue"]
            tableWidget.setHorizontalHeaderLabels(headers)

            label.setGeometry(QtCore.QRect(40, 35, 111, 21))
            label_2.setGeometry(QtCore.QRect(160, 35, 31, 21))
            label_3.setGeometry(QtCore.QRect(200, 35, 190, 21))
            label_4.setGeometry(QtCore.QRect(342, 35, 37, 21))
            pushButton.setGeometry(QtCore.QRect(390, 35, 75, 23))
            tableWidget.setGeometry(QtCore.QRect(20, 65, 451, 211))

            if type == 'revenueCustomer':
                pushButton.clicked.connect(lambda: saveReport('revenueCustomer'))
                label.setText("Number of Customers :")
                label_3.setText("Average orders per Customer :")
                try:
                    with conn:
                        c.execute("SELECT customers.ID, customers.name, SUM(products.price * orders.quantity) FROM orders JOIN products ON orders.product = products.name JOIN customers on orders.customer = customers.name GROUP BY customers.name ORDER BY customers.ID")
                        tableWidget.setRowCount(0)
                        for data in c.fetchall():
                            row_index = tableWidget.rowCount()
                            for column_index, data in enumerate(data):
                                data = str(data)
                                tableWidget.setRowCount(row_index+1)
                                tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))
                    
                        c.execute(f"SELECT COUNT(customers.ID) FROM customers")
                        numberOfCustomers = str(c.fetchall()[0][0])
                        label_2.setText(numberOfCustomers)

                        c.execute(f"SELECT COUNT(orders.id) FROM orders")
                        numberOfOrders = str(c.fetchall()[0][0])
                        average = float(numberOfOrders)/float(numberOfCustomers)
                        label_4.setText(f"{average:.2f}")

                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

            elif type == 'revenueProduct':
                pushButton.clicked.connect(lambda: saveReport('revenueProduct'))
                label.setText("Number of Products :")
                label_3.setText("Average Product Revenue:")
                try:
                    with conn:
                        c.execute("SELECT products.ID, products.name, SUM(products.price * orders.quantity) AS revenue FROM products JOIN orders ON orders.product = products.name GROUP BY products.name ORDER BY revenue DESC")
                        tableWidget.setRowCount(0)
                        for data in c.fetchall():
                            row_index = tableWidget.rowCount()
                            for column_index, data in enumerate(data):
                                data = str(data)
                                tableWidget.setRowCount(row_index+1)
                                tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))
                    
                        c.execute(f"SELECT COUNT(products.ID) FROM products")
                        numberOfProducts = str(c.fetchall()[0][0])
                        label_2.setText(numberOfProducts)

                        c.execute(f"SELECT SUM(products.price * orders.quantity) FROM orders JOIN products ON orders.product = products.name")
                        totalRevenue = str(c.fetchall()[0][0])
                        average = float(totalRevenue)/float(numberOfProducts)
                        label_4.setText(f"{average:.2f}")

                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

            elif type == 'revenueSupplier':
                pushButton.clicked.connect(lambda: saveReport('revenueSupplier'))
                label.setText("Number of Suppliers :")
                label_3.setText("Average Supplier Revenue:")
                try:
                    with conn:
                        c.execute("SELECT suppliers.ID, suppliers.name, SUM(products.price * orders.quantity) AS revenue FROM suppliers JOIN products ON products.supplier = suppliers.name JOIN orders ON orders.product = products.name GROUP BY suppliers.name ORDER BY revenue DESC")
                        tableWidget.setRowCount(0)
                        for data in c.fetchall():
                            row_index = tableWidget.rowCount()
                            for column_index, data in enumerate(data):
                                data = str(data)
                                tableWidget.setRowCount(row_index+1)
                                tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))
                    
                        c.execute(f"SELECT COUNT(suppliers.ID) FROM suppliers")
                        numberOfSuppliers = str(c.fetchall()[0][0])
                        label_2.setText(numberOfSuppliers)

                        c.execute(f"SELECT SUM(products.price * orders.quantity) FROM orders JOIN products ON orders.product = products.name")
                        totalRevenue = str(c.fetchall()[0][0])
                        average = float(totalRevenue)/float(numberOfSuppliers)
                        label_4.setText(f"{average:.2f}")

                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

            self.mdiArea.addSubWindow(sub)
            sub.show()

        elif type == 'BalanceSheet':
            sub = QtWidgets.QMdiSubWindow()
            sub.setFixedSize(450, 181)
            sub.setWindowTitle("Balance Sheet")

            font12 = QtGui.QFont()
            font12.setPointSize(12)
            font10 = QtGui.QFont()
            font10.setPointSize(10)

            line = QtWidgets.QFrame(sub)
            with conn:
                c.execute(f"SELECT MIN(date) FROM orders")
                dateFrom = str(c.fetchall()[0][0])
            dateFromLabel = QtWidgets.QLabel(dateFrom, sub)
            with conn:
                c.execute(f"SELECT MAX(date) FROM orders")
                dateTo = str(c.fetchall()[0][0])
            dateToLabel = QtWidgets.QLabel(dateTo, sub)
            line_2 = QtWidgets.QFrame(sub)
            pushButton = QtWidgets.QPushButton("Balance Sheet", sub, clicked = lambda: printBalanceSheat(label_7, label_5, label_10, label_13, label_11))
            saveButton = QtWidgets.QPushButton("Save", sub, clicked = lambda: saveReport('BalanceSheet'))
            label_2 = QtWidgets.QLabel("Personel Exp. :", sub)
            label_4 = QtWidgets.QLabel("Suppliers Exp. :", sub)
            label_5 = QtWidgets.QLabel("0", sub)
            label_7 = QtWidgets.QLabel("0", sub)
            label_8 = QtWidgets.QLabel("Capital :", sub)
            label_9 = QtWidgets.QLabel("Sales Earnings :", sub)
            label_10 = QtWidgets.QLabel("0", sub)
            label_13 = QtWidgets.QLabel("0", sub)
            label_11 = QtWidgets.QLabel("$ 0", sub)
            line.setGeometry(QtCore.QRect(70, 50, 311, 41))
            line_2.setGeometry(QtCore.QRect(210, 70, 32, 71))
            pushButton.setGeometry(QtCore.QRect(170, 35, 112, 25))
            saveButton.setGeometry(QtCore.QRect(350, 140, 60, 20))
            label_2.setGeometry(QtCore.QRect(70, 80, 102, 20))
            label_4.setGeometry(QtCore.QRect(50, 110, 122, 20))
            label_5.setGeometry(QtCore.QRect(166, 80, 42, 20))
            label_7.setGeometry(QtCore.QRect(166, 110, 42, 20))
            label_8.setGeometry(QtCore.QRect(240, 80, 102, 20))
            label_9.setGeometry(QtCore.QRect(220, 110, 122, 20))
            label_10.setGeometry(QtCore.QRect(345, 110, 42, 20))
            label_13.setGeometry(QtCore.QRect(345, 80, 42, 20))
            label_11.setGeometry(QtCore.QRect(180, 140, 92, 21))
            dateFromLabel.setGeometry(QtCore.QRect(30, 37, 110, 22))
            dateToLabel.setGeometry(QtCore.QRect(360, 37, 110, 22))
            pushButton.setFont(font12)
            label_2.setFont(font10)
            label_4.setFont(font10)
            label_5.setFont(font10)
            label_7.setFont(font10)
            label_8.setFont(font10)
            label_9.setFont(font10)
            label_10.setFont(font10)
            label_13.setFont(font10)
            label_11.setFont(font10)
            line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
            line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
            label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)

            self.mdiArea.addSubWindow(sub)
            sub.show()

            def printBalanceSheat(suppliersExpLabel, personelExpLabel, salesEarLabel, capitalLabel, balanceLabel):
                try:
                    with conn:
                        c.execute(f"SELECT SUM(products.price * 0.70 * orders.quantity) FROM orders JOIN products ON orders.product = products.name")
                        suppliersExp = round(c.fetchall()[0][0])
                        suppliersExpLabel.setText(f"{suppliersExp}")
    
                    with conn:
                        c.execute(f"SELECT SUM(employees.pay) FROM employees")
                        personelExp = round(c.fetchall()[0][0])
                        personelExpLabel.setText(f"{personelExp}")
    
                    with conn:
                        c.execute(f"SELECT SUM(orders.quantity * products.price) FROM orders JOIN products ON orders.product = products.name")
                        salesEar = round(c.fetchall()[0][0])
                        salesEarLabel.setText(f"{salesEar}")

                    with conn:
                        c.execute("SELECT capital FROM company")
        
                    capital = c.fetchall()[0][0]
                    if capital is not None:
                        capitalLabel.setText(f"{capital}")
                    else:
                        capitalLabel.setText("0")
                        self.errorPopup("capitalError")

                    balance = (capital + salesEar) - (suppliersExp + personelExp)
                    balanceLabel.setText(f"$ {balance}")
                    if int(balance) > 0:
                        balanceLabel.setStyleSheet("#label_11 {color: green;}")
                    elif int(balance) == 0:
                        balanceLabel.setStyleSheet("#label_11 {color: black;}")
                    elif int(balance) < 0:
                        balanceLabel.setStyleSheet("#label_11 {color: red;}")
                
                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

                except TypeError as e:
                    print(f"TypeError: {e}")  # can't round none type (because tables are empty)

        def saveReport(type):
            try:
                with conn:
                    c.execute(f"SELECT number FROM reports")
                    numbers = c.fetchall()
                    while True:
                        number = random.randint(510000000, 510999999)
                        if number not in numbers:
                            break
                    today = datetime.date.today().strftime("%d/%m/%Y")
                    if type == 'revenueCustomer' or type == 'revenueProduct' or type == 'revenueSupplier':
                        c.execute(f"INSERT INTO reports (name, number) VALUES ('report_{today}', '{number}')")
                        c.execute(f"CREATE TABLE '{number}' (ID integer, name varchar(50), revenue INTEGER)")
                    
                        if type == 'revenueCustomer':
                            c.execute("SELECT customers.ID, customers.name, SUM(products.price * orders.quantity) FROM orders JOIN products ON orders.product = products.name JOIN customers on orders.customer = customers.name GROUP BY customers.name ORDER BY customers.ID")
                            data = c.fetchall()
                            for info in data:
                                c.execute(f"INSERT INTO '{number}' (ID, name, revenue) VALUES ('{info[0]}', '{info[1]}', '{info[2]}')")

                        elif type == 'revenueProduct':
                            c.execute("SELECT products.ID, products.name, SUM(products.price * orders.quantity) AS revenue FROM products JOIN orders ON orders.product = products.name GROUP BY products.name ORDER BY revenue DESC")
                            data = c.fetchall()
                            for info in data:
                                c.execute(f"INSERT INTO '{number}' (ID, name, revenue) VALUES ('{info[0]}', '{info[1]}', '{info[2]}')")

                        elif type == 'revenueSupplier':
                            c.execute("SELECT suppliers.ID, suppliers.name, SUM(products.price * orders.quantity) AS revenue FROM suppliers JOIN products ON products.supplier = suppliers.name JOIN orders ON orders.product = products.name GROUP BY suppliers.name ORDER BY revenue DESC")
                            data = c.fetchall()
                            for info in data:
                                c.execute(f"INSERT INTO '{number}' (ID, name, revenue) VALUES ('{info[0]}', '{info[1]}', '{info[2]}')")

                    elif type == 'BalanceSheet':
                        c.execute(f"INSERT INTO reports (name, number) VALUES ('balanceSheet_{today}', '{number}')")
                        c.execute(f"CREATE TABLE '{number}'(mindate date, maxdate date, personel, suppliers, capital, sales, balance)")
                        
                        c.execute(f"SELECT MIN(date) FROM orders")
                        dateFrom = str(c.fetchall()[0][0])
                    
                        c.execute(f"SELECT MAX(date) FROM orders")
                        dateTo = str(c.fetchall()[0][0])

                        c.execute(f"SELECT SUM(products.price * 0.70 * orders.quantity) FROM orders JOIN products ON orders.product = products.name")
                        suppliersExp = round(c.fetchall()[0][0])
    
                        c.execute(f"SELECT SUM(employees.pay) FROM employees")
                        personelExp = round(c.fetchall()[0][0])
    
                        c.execute(f"SELECT SUM(orders.quantity * products.price) FROM orders JOIN products ON orders.product = products.name")
                        salesEar = round(c.fetchall()[0][0])

                        with conn:
                            c.execute("SELECT capital FROM company")
                            capital = int(c.fetchall()[0][0])
                        balance = (capital + salesEar) - (suppliersExp + personelExp)

                        c.execute(f"""INSERT INTO '{number}' (mindate, maxdate, personel, suppliers, capital, sales, balance) 
                                        VALUES ('{dateFrom}', '{dateTo}', '{personelExp}', '{suppliersExp}', '{capital}', '{salesEar}', '{balance}')""")
                        
            except sqlite3.DatabaseError as e:
                erpLogger.info(f"Problem faced: {e}")

    def viewReports(self):
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(265, 338)
        sub.setWindowTitle("Reports")
        
        tableWidget = QtWidgets.QTableWidget(sub)
        tableWidget.setGeometry(QtCore.QRect(12, 35, 241, 280))
        tableWidget.setColumnCount(2)
        headers = ["Name", "Number"]
        tableWidget.setHorizontalHeaderLabels(headers)
        tableWidget.itemDoubleClicked.connect(lambda: viewReport())

        with conn:
            c.execute("SELECT * FROM reports")
            tableWidget.setRowCount(0)
            for data in c.fetchall():
                row_index = tableWidget.rowCount()
                for column_index, data in enumerate(data):
                    data = str(data)
                    tableWidget.setRowCount(row_index+1)
                    tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))

            header = tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
            for index in range(2):
                header.setSectionResizeMode(index, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        def viewReport():
            print("report")

        self.mdiArea.addSubWindow(sub)
        sub.show()

    def company(self, action):
        if action == 'capital':
            self.errorPopup("capitalWarning")

            sub = QtWidgets.QMdiSubWindow()
            sub.setFixedSize(280, 150)
            sub.setWindowTitle("Company")

            label = QtWidgets.QLabel("Amount :", sub)
            capitalLineEdit = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Add", sub, clicked = lambda: addCapital(capitalLineEdit))

            label.setGeometry(QtCore.QRect(50, 60, 50, 20))
            capitalLineEdit.setGeometry(QtCore.QRect(115, 60, 80, 20))
            pushButton.setGeometry(QtCore.QRect(160, 100, 81, 23))
            pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

            def addCapital(capital):
                with conn:
                    c.execute(f"UPDATE company SET capital = (SELECT capital FROM company) + {capital.text()}")
                capital.clear()

            self.mdiArea.addSubWindow(sub)
            sub.show()
            return True
        
        sub = QtWidgets.QMdiSubWindow()
        sub.setFixedSize(385, 300)
        sub.setWindowTitle("Company")
        
        font10 = QtGui.QFont()
        font10.setPointSize(10)
        line = QtWidgets.QFrame(sub)
        label = QtWidgets.QLabel(" Company name:", sub)
        label_2 = QtWidgets.QLabel(" Company SSN:", sub)
        label_3 = QtWidgets.QLabel(" Phone number:", sub)
        label_4 = QtWidgets.QLabel("Product/Services category:", sub)
        label_5 = QtWidgets.QLabel(" Company Adress:", sub)
        label_6 = QtWidgets.QLabel(" Company type:", sub)
        label_7 = QtWidgets.QLabel(" Company email:", sub)
        label_8 = QtWidgets.QLabel("Starting Capital:", sub)
        if action == 'setup':
            lineEdit = QtWidgets.QLineEdit(sub)
            lineEdit_2 = QtWidgets.QLineEdit(sub)
            lineEdit_3 = QtWidgets.QLineEdit(sub)
            lineEdit_4 = QtWidgets.QLineEdit(sub)
            lineEdit_5 = QtWidgets.QLineEdit(sub)
            lineEdit_6 = QtWidgets.QLineEdit(sub)
            lineEdit_7 = QtWidgets.QLineEdit(sub)
            lineEdit_8 = QtWidgets.QLineEdit(sub)
            pushButton = QtWidgets.QPushButton("Register", sub, clicked = lambda: registerCompanyInfo(lineEdit.text(), lineEdit_5.text(), lineEdit_2.text(), lineEdit_6.text(), lineEdit_3.text(), lineEdit_7.text(), lineEdit_4.text(), lineEdit_8.text(), self.actionSetup_Company, self.actionView_Information))
            
            lineEdit.setGeometry(QtCore.QRect(20, 60, 151, 20))
            lineEdit_2.setGeometry(QtCore.QRect(20, 110, 151, 20))
            lineEdit_3.setGeometry(QtCore.QRect(20, 160, 151, 20))
            lineEdit_4.setGeometry(QtCore.QRect(20, 210, 151, 20))
            lineEdit_5.setGeometry(QtCore.QRect(210, 60, 151, 20))
            lineEdit_6.setGeometry(QtCore.QRect(210, 110, 151, 20))
            lineEdit_7.setGeometry(QtCore.QRect(210, 160, 151, 20))
            lineEdit_8.setGeometry(QtCore.QRect(210, 210, 151, 20))

        elif action == 'information':
            labelName = QtWidgets.QLabel(sub)
            labelSSN = QtWidgets.QLabel(sub)
            labelPhone = QtWidgets.QLabel(sub)
            labelCategory = QtWidgets.QLabel(sub)
            labelAdress = QtWidgets.QLabel(sub)
            labelType = QtWidgets.QLabel(sub)
            labelEmail = QtWidgets.QLabel(sub)
            labelCapital = QtWidgets.QLabel(sub)
            comboBox = QtWidgets.QComboBox(sub)
            lineEdit = QtWidgets.QLineEdit(sub)
            items = ["Name", "SSN", "Phone", "Category", "Adress", "Type", "Email", "Capital"]
            comboBox.addItems(items)
            pushButton = QtWidgets.QPushButton("Change", sub, clicked = lambda: changeInfo(comboBox, lineEdit))
            labelName.setGeometry(QtCore.QRect(20, 60, 151, 20))
            labelSSN.setGeometry(QtCore.QRect(20, 110, 151, 20))
            labelPhone.setGeometry(QtCore.QRect(20, 160, 151, 20))
            labelCategory.setGeometry(QtCore.QRect(20, 210, 151, 20))
            labelAdress.setGeometry(QtCore.QRect(210, 60, 151, 20))
            labelType.setGeometry(QtCore.QRect(210, 110, 151, 20))
            labelEmail.setGeometry(QtCore.QRect(210, 160, 151, 20))
            labelCapital.setGeometry(QtCore.QRect(210, 210, 151, 20))
            comboBox.setGeometry(QtCore.QRect(60, 250, 81, 23))
            lineEdit.setGeometry(QtCore.QRect(153, 250, 81, 23))
            comboBox.currentIndexChanged.connect(lambda: checkComboBox(comboBox.currentText()))
            
            def checkComboBox(selection):
                if selection == 'Capital':
                    self.errorPopup("capitalWarning")

            with conn:
                c.execute("SELECT * FROM company")

            data = c.fetchall()
            name, adress, SSN, type, phone, email, category, capital = data[0]
            labelName.setText(str(name))
            labelSSN.setText(str(SSN))
            labelPhone.setText(str(phone))
            labelCategory.setText(category)
            labelAdress.setText(str(adress))
            labelType.setText(str(type))
            labelEmail.setText(str(email))
            labelCapital.setText(str(capital))

            def changeInfo(comboBox, lineEdit):
                item = comboBox.currentText()
                newText = lineEdit.text()      
                try:
                    with conn:
                        c.execute(f"UPDATE company SET {item} = '{newText}' WHERE name = (SELECT name FROM company)")
                
                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

                if item == 'Name':
                    labelName.setText(newText)
                elif item == 'SSN':
                    labelSSN.setText(newText)
                elif item == 'Phone':
                    labelPhone.setText(newText)
                elif item == 'Category':
                    labelCategory.setText(newText)
                elif item == 'Adress':
                    labelAdress.setText(newText)
                elif item == 'Type':
                    labelType.setText(newText)
                elif item == 'Email':
                    labelEmail.setText(newText)
                elif item == 'Capital':
                    labelCapital.setText(newText)

        label.setFont(font10)
        label_2.setFont(font10)
        label_3.setFont(font10)
        label_4.setFont(font10)
        label_5.setFont(font10)
        label_6.setFont(font10)
        label_7.setFont(font10)
        label_8.setFont(font10)
        line.setGeometry(QtCore.QRect(180, 50, 20, 191))
        label.setGeometry(QtCore.QRect(20, 40, 101, 20))
        label_2.setGeometry(QtCore.QRect(20, 90, 101, 20))
        label_3.setGeometry(QtCore.QRect(20, 140, 101, 20))
        label_4.setGeometry(QtCore.QRect(20, 190, 161, 20))
        label_5.setGeometry(QtCore.QRect(210, 40, 111, 20))
        label_6.setGeometry(QtCore.QRect(210, 90, 101, 20))
        label_7.setGeometry(QtCore.QRect(210, 140, 101, 20))
        label_8.setGeometry(QtCore.QRect(210, 190, 101, 20))
        pushButton.setGeometry(QtCore.QRect(244, 250, 81, 23))
        line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        def registerCompanyInfo(name, adress, ssn, type, number, email, category, capital, setpupAction, infromationAction):
            with conn:
                c.execute("CREATE TABLE customers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
                c.execute("CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), department varchar(50), pay INTEGER)")
                c.execute("CREATE TABLE suppliers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
                c.execute("CREATE TABLE departments(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50))")
                c.execute("CREATE TABLE products(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), category varchar(50), price INTEGER, supplier varchar(50))")
                c.execute("CREATE TABLE orders(ID INTEGER PRIMARY KEY AUTOINCREMENT, customer varchar(50), product varchar(50), quantity INTEGER, date DATE)")
                c.execute("CREATE TABLE company(name varchar(50), adress varchar(50), ssn INTEGER, type varchar(50), number INTEGER, email varchar(50), category varchar(50), capital INTEGER)")
                c.execute("CREATE TABLE reports(name varchar(50), number INTEGER)")
            
                try:
                    with conn:
                        c.execute(f"INSERT INTO company (name, adress, ssn, type, number, email, category, capital) VALUES ('{name}', '{adress}', '{ssn}', '{type}', '{number}', '{email}', '{category}', '{capital}')")

                except sqlite3.DatabaseError as e:
                    erpLogger.info(f"Problem faced: {e}")

            setpupAction.setEnabled(False)
            self.actionCreate_Customer.setEnabled(True)
            self.menuCustomers.setEnabled(True)
            self.menuEmployees.setEnabled(True)
            self.menuProducts.setEnabled(True)
            self.menuOrders.setEnabled(True)
            self.menuSuppliers.setEnabled(True)
            self.menuDepartments.setEnabled(True)
            self.menuReports.setEnabled(True)
            self.actionView_Information.setEnabled(True)
            self.actionAdd_Capital.setEnabled(True)
            infromationAction.setEnabled(True)
            sub.close()

        self.mdiArea.addSubWindow(sub)
        sub.show()

    def errorPopup(self, reason):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        if reason == 'departmentError':
            msg.setText("Department not found.")
        elif reason == 'departmentExists':
            msg.setText("Department already exists.")
        elif reason == 'supplierError':
            msg.setText("Supplier not found.")
        elif reason == 'customerError':
            msg.setText("Customer not found..")
        elif reason == 'productError':
            msg.setText("Product not found.")
        elif reason == 'quantityValueError':
            msg.setText("Quantity value must be a number")
        elif reason == 'capitalError':
            msg.setText("Capital is not set.")
        elif reason == 'capitalWarning':
            msg.setText("You are about to change the capital.")

        show = msg.exec_()     


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Manager"))
        self.menuCustomers.setTitle(_translate("mainWindow", "Customers"))
        self.menuEmployees.setTitle(_translate("mainWindow", "Employees"))
        self.menuProducts.setTitle(_translate("mainWindow", "Products"))
        self.menuOrders.setTitle(_translate("mainWindow", "Orders"))
        self.menuSuppliers.setTitle(_translate("mainWindow", "Suppliers"))
        self.menuDepartments.setTitle(_translate("mainWindow", "Departments"))
        self.menuReports.setTitle(_translate("mainWindow", "Reports"))
        self.menuCreate_report.setTitle(_translate("mainWindow", "Create report"))
        self.menuCompany.setTitle(_translate("mainWindow", "Company"))
        self.actionCreate_Customer.setText(_translate("mainWindow", "Create Customer"))
        self.actionView_Customers.setText(_translate("mainWindow", "View Customers"))
        self.actionCreate_Employee.setText(_translate("mainWindow", "Create Employee"))
        self.actionView_Employees.setText(_translate("mainWindow", "View Employee"))
        self.actionCreate_Product.setText(_translate("mainWindow", "Create Products"))
        self.actionView_Products.setText(_translate("mainWindow", "View Products"))
        self.actionCreate_Order.setText(_translate("mainWindow", "Create Order"))
        self.actionView_Orders.setText(_translate("mainWindow", "View Orders"))
        self.actionCreate_Supplier.setText(_translate("mainWindow", "Create Supplier"))
        self.actionView_Suppliers.setText(_translate("mainWindow", "View Supplier"))
        self.actionCreate_Department.setText(_translate("mainWindow", "Create Department"))
        self.actionView_Departments.setText(_translate("mainWindow", "View Department"))
        self.actionView_reports.setText(_translate("mainWindow", "View reports"))
        self.actionPrint_report.setText(_translate("mainWindow", "Print report"))
        self.actionBalance_Sheet.setText(_translate("mainWindow", "Balance Sheet"))
        self.actionRevenue_per_Customer.setText(_translate("mainWindow", "Revenue per Customer"))
        self.actionRevenue_per_Product.setText(_translate("mainWindow", "Revenue per Product"))
        self.actionRevenue_per_Supplier.setText(_translate("mainWindow", "Revenue per Supplier"))
        self.actionSetup_Company.setText(_translate("mainWindow", "Setup Company"))
        self.actionView_Information.setText(_translate("mainWindow", "View Information"))
        self.actionAdd_Capital.setText(_translate("mainWindow", "Add Capital"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
