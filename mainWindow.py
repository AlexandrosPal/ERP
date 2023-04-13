from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
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
        mainWindow.setCentralWidget(self.centralwidget)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName("menubar")

        # Customers
        self.menuCustomers = QtWidgets.QMenu(self.menubar)
        self.menuCustomers.setObjectName("menuCustomers")

        # Status bar
        self.menuEmployees = QtWidgets.QMenu(self.menubar)
        self.menuEmployees.setObjectName("menuEmployees")

        # Products
        self.menuProducts = QtWidgets.QMenu(self.menubar)
        self.menuProducts.setObjectName("menuProducts")
        
        # Orders
        self.menuOrders = QtWidgets.QMenu(self.menubar)
        self.menuOrders.setObjectName("menuOrders")
        
        # Suppliers
        self.menuSuppliers = QtWidgets.QMenu(self.menubar)
        self.menuSuppliers.setObjectName("menuSuppliers")
        
        # Departments
        self.menuDepartments = QtWidgets.QMenu(self.menubar)
        self.menuDepartments.setObjectName("menuDepartments")
        
        # Reports
        self.menuReports = QtWidgets.QMenu(self.menubar)
        self.menuReports.setObjectName("menuReports")
        
        # Cretae report
        self.menuCreate_report = QtWidgets.QMenu(self.menuReports)
        self.menuCreate_report.setObjectName("menuCreate_report")
        mainWindow.setMenuBar(self.menubar)
        
        # Create Customer
        self.actionCreate_Customer = QtWidgets.QAction(mainWindow)
        self.actionCreate_Customer.setObjectName("actionCreate_Customer")
        
        # View Customer
        self.actionView_Customers = QtWidgets.QAction(mainWindow)
        self.actionView_Customers.setObjectName("actionView_Customers")
        
        # Create Employee
        self.actionCreate_Employee = QtWidgets.QAction(mainWindow)
        self.actionCreate_Employee.setObjectName("actionCreate_Employee")
        
        # View Employee
        self.actionView_Employee = QtWidgets.QAction(mainWindow)
        self.actionView_Employee.setObjectName("actionView_Employee")
        
        # View Products
        self.actionView_Products = QtWidgets.QAction(mainWindow)
        self.actionView_Products.setObjectName("actionView_Products")
        
        # Create Product
        self.actionCreate_Products = QtWidgets.QAction(mainWindow)
        self.actionCreate_Products.setObjectName("actionCreate_Products")
        
        # Create Order
        self.actionCreate_Orders = QtWidgets.QAction(mainWindow)
        self.actionCreate_Orders.setObjectName("actionCreate_Orders")
        
        # View Order
        self.actionView_Orders = QtWidgets.QAction(mainWindow)
        self.actionView_Orders.setObjectName("actionView_Orders")
        
        # Create Supplier
        self.actionCreate_Supplier = QtWidgets.QAction(mainWindow)
        self.actionCreate_Supplier.setObjectName("actionCreate_Supplier")
        
        # View Supplier
        self.actionView_Supplier = QtWidgets.QAction(mainWindow)
        self.actionView_Supplier.setObjectName("actionView_Supplier")
        
        # Create Department
        self.actionCreate_Department = QtWidgets.QAction(mainWindow)
        self.actionCreate_Department.setObjectName("actionCreate_Department")
        
        # View Department
        self.actionView_Department = QtWidgets.QAction(mainWindow)
        self.actionView_Department.setObjectName("actionView_Department")
        
        # View Report
        self.actionView_reports = QtWidgets.QAction(mainWindow)
        self.actionView_reports.setObjectName("actionView_reports")
        
        # Print Report
        self.actionPrint_report = QtWidgets.QAction(mainWindow)
        self.actionPrint_report.setObjectName("actionPrint_report")
        
        # Report: Revenue per Customer
        self.actionRevenue_per_Customer = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Customer.setObjectName("actionRevenue_per_Customer")
        
        # Report: Revenue per Product
        self.actionRevenue_per_Product = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Product.setObjectName("actionRevenue_per_Product")
        
        # Report: Revenue per Supplier
        self.actionRevenue_per_Supplier = QtWidgets.QAction(mainWindow)
        self.actionRevenue_per_Supplier.setObjectName("actionRevenue_per_Supplier")
        
        # Adding the actions
        self.menuCustomers.addAction(self.actionCreate_Customer)
        self.menuCustomers.addAction(self.actionView_Customers)
        self.menuEmployees.addAction(self.actionCreate_Employee)
        self.menuEmployees.addAction(self.actionView_Employee)
        self.menuProducts.addAction(self.actionView_Products)
        self.menuProducts.addAction(self.actionCreate_Products)
        self.menuOrders.addAction(self.actionCreate_Orders)
        self.menuOrders.addAction(self.actionView_Orders)
        self.menuSuppliers.addAction(self.actionCreate_Supplier)
        self.menuSuppliers.addAction(self.actionView_Supplier)
        self.menuDepartments.addAction(self.actionCreate_Department)
        self.menuDepartments.addAction(self.actionView_Department)
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

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    # Pyqt5 translate function
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
        self.actionView_Employee.setText(_translate("mainWindow", "View Employee"))
        self.actionView_Products.setText(_translate("mainWindow", "Create Products"))
        self.actionCreate_Products.setText(_translate("mainWindow", "View Products"))
        self.actionCreate_Orders.setText(_translate("mainWindow", "Create Orders"))
        self.actionView_Orders.setText(_translate("mainWindow", "View Orders"))
        self.actionCreate_Supplier.setText(_translate("mainWindow", "Create Supplier"))
        self.actionView_Supplier.setText(_translate("mainWindow", "View Supplier"))
        self.actionCreate_Department.setText(_translate("mainWindow", "Create Department"))
        self.actionView_Department.setText(_translate("mainWindow", "View Department"))
        self.actionView_reports.setText(_translate("mainWindow", "View reports"))
        self.actionPrint_report.setText(_translate("mainWindow", "Print report"))
        self.actionRevenue_per_Customer.setText(_translate("mainWindow", "Revenue per Customer"))
        self.actionRevenue_per_Product.setText(_translate("mainWindow", "Revenue per Product"))
        self.actionRevenue_per_Supplier.setText(_translate("mainWindow", "Revenue per Supplier"))


# Initialize app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
