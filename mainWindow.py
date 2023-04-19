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

with conn:
    # c.execute("CREATE TABLE customers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), department varchar(50), pay INTEGER)")
    # c.execute("CREATE TABLE suppliers(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), email varchar(50), phone int)")
    # c.execute("CREATE TABLE departments(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50))")
    # c.execute("CREATE TABLE products(ID INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), category varchar(50), price INTEGER, supplier varchar(50))")
    # c.execute("DROP TABLE customers")
    # c.execute("DROP TABLE employees")
    # c.execute("DROP TABLE suppliers")
    # c.execute("DROP TABLE departments")
    # c.execute("DROP TABLE products")
    # c.execute("SELECT * FROM departments")
    # print(c.fetchall())
    pass
 

class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setFixedSize(737, 511)
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
        self.actionCreate_Product = QtWidgets.QAction(mainWindow)
        self.actionCreate_Product.setObjectName("actionCreate_Product")
        self.actionView_Products = QtWidgets.QAction(mainWindow)
        self.actionView_Products.setObjectName("actionView_Products")
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
        self.menuProducts.addAction(self.actionCreate_Product)
        self.menuProducts.addAction(self.actionView_Products)
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
        self.actionCreate_Product.triggered.connect(lambda: self.createWindow('products'))
        self.actionView_Customers.triggered.connect(lambda: self.viewWindow('customers'))
        self.actionView_Employees.triggered.connect(lambda: self.viewWindow('employees'))
        self.actionView_Suppliers.triggered.connect(lambda: self.viewWindow('suppliers'))
        self.actionView_Departments.triggered.connect(lambda: self.viewWindow('departments'))
        self.actionView_Products.triggered.connect(lambda: self.viewWindow('products'))

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


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
            label4 = QtWidgets.QLabel("Annual Pay:", sub)
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

        tableWidget.setRowCount(0)
        for data in c.fetchall():
            row_index = tableWidget.rowCount()
            for column_index, data in enumerate(data):
                data = str(data)
                tableWidget.setRowCount(row_index+1)
                tableWidget.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(data))
        
    def errorPopup(self, reason):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        if reason == 'departmentError':
            msg.setText("Department not found.")
        elif reason == 'departmentExists':
            msg.setText("Department already exists.")
        elif reason == 'supplierError':
            msg.setText("Supplier not found.")
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
        self.actionCreate_Product.setText(_translate("mainWindow", "Create Products"))
        self.actionView_Products.setText(_translate("mainWindow", "View Products"))
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
