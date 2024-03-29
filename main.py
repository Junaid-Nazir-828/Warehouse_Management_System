from PyQt5 import QtCore, QtGui, QtWidgets
import db
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1059, 822)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                self.tabWidget.setStyleSheet("background-color:#EDEEE9;")
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                self.tab.setObjectName("tab")
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_11.setObjectName("horizontalLayout_11")
                self.label = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.horizontalLayout_11.addWidget(self.label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.artical_number_lineEdit_tab1 = QtWidgets.QLineEdit(self.tab)
                self.artical_number_lineEdit_tab1.setMinimumSize(QtCore.QSize(0, 0))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.artical_number_lineEdit_tab1.setFont(font)
                self.artical_number_lineEdit_tab1.setStyleSheet("background-color:white;")
                self.artical_number_lineEdit_tab1.setObjectName("artical_number_lineEdit_tab1")
                self.horizontalLayout_11.addWidget(self.artical_number_lineEdit_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_6.addLayout(self.horizontalLayout_11)
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.label_2 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.horizontalLayout_10.addWidget(self.label_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.artical_name_lineEdit_tab1 = QtWidgets.QLineEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.artical_name_lineEdit_tab1.setFont(font)
                self.artical_name_lineEdit_tab1.setStyleSheet("background-color:white;")
                self.artical_name_lineEdit_tab1.setObjectName("artical_name_lineEdit_tab1")
                self.horizontalLayout_10.addWidget(self.artical_name_lineEdit_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_6.addLayout(self.horizontalLayout_10)
                self.verticalLayout.addLayout(self.horizontalLayout_6)
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_15.setObjectName("horizontalLayout_15")
                self.label_5 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.horizontalLayout_15.addWidget(self.label_5, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.production_date_tab1 = QtWidgets.QDateEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.production_date_tab1.setFont(font)
                self.production_date_tab1.setStyleSheet("padding: 0px 15px;\n"
        "background-color:white;")
                self.production_date_tab1.setObjectName("production_date_tab1")
                self.horizontalLayout_15.addWidget(self.production_date_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_4.addLayout(self.horizontalLayout_15)
                self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_14.setObjectName("horizontalLayout_14")
                self.label_6 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.horizontalLayout_14.addWidget(self.label_6, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.best_before_date_tab1 = QtWidgets.QDateEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.best_before_date_tab1.setFont(font)
                self.best_before_date_tab1.setStyleSheet("padding: 0px 15px;\n"
        "background-color:white;")
                self.best_before_date_tab1.setObjectName("best_before_date_tab1")
                self.horizontalLayout_14.addWidget(self.best_before_date_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_4.addLayout(self.horizontalLayout_14)
                self.verticalLayout.addLayout(self.horizontalLayout_4)
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_17.setObjectName("horizontalLayout_17")
                self.label_7 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_7.setFont(font)
                self.label_7.setObjectName("label_7")
                self.horizontalLayout_17.addWidget(self.label_7, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.batch_number_lineEdit_tab1 = QtWidgets.QLineEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.batch_number_lineEdit_tab1.setFont(font)
                self.batch_number_lineEdit_tab1.setStyleSheet("background-color:white;")
                self.batch_number_lineEdit_tab1.setObjectName("batch_number_lineEdit_tab1")
                self.horizontalLayout_17.addWidget(self.batch_number_lineEdit_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_3.addLayout(self.horizontalLayout_17)
                self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                self.label_8 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_8.setFont(font)
                self.label_8.setObjectName("label_8")
                self.horizontalLayout_16.addWidget(self.label_8, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.quantity_lineEdit_tab1 = QtWidgets.QLineEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.quantity_lineEdit_tab1.setFont(font)
                self.quantity_lineEdit_tab1.setStyleSheet("background-color:white;")
                self.quantity_lineEdit_tab1.setObjectName("quantity_lineEdit_tab1")
                self.horizontalLayout_16.addWidget(self.quantity_lineEdit_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_3.addLayout(self.horizontalLayout_16)
                self.verticalLayout.addLayout(self.horizontalLayout_3)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_13.setObjectName("horizontalLayout_13")
                self.label_3 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.horizontalLayout_13.addWidget(self.label_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.producing_employee_combo_tab1 = QtWidgets.QComboBox(self.tab)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.producing_employee_combo_tab1.setFont(font)
                self.producing_employee_combo_tab1.setStyleSheet("background-color:white;")
                self.producing_employee_combo_tab1.setObjectName("producing_employee_combo_tab1")
                self.horizontalLayout_13.addWidget(self.producing_employee_combo_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_5.addLayout(self.horizontalLayout_13)
                self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_12.setObjectName("horizontalLayout_12")
                self.label_4 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.horizontalLayout_12.addWidget(self.label_4, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.product_combo_tab1 = QtWidgets.QComboBox(self.tab)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.product_combo_tab1.setFont(font)
                self.product_combo_tab1.setStyleSheet("background-color:white;")
                self.product_combo_tab1.setObjectName("product_combo_tab1")
                self.horizontalLayout_12.addWidget(self.product_combo_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_5.addLayout(self.horizontalLayout_12)
                self.verticalLayout.addLayout(self.horizontalLayout_5)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setSpacing(20)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.label_9 = QtWidgets.QLabel(self.tab)
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(10)
                self.label_9.setFont(font)
                self.label_9.setObjectName("label_9")
                self.horizontalLayout_2.addWidget(self.label_9, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.special_features_lineEdit_tab1 = QtWidgets.QLineEdit(self.tab)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.special_features_lineEdit_tab1.setFont(font)
                self.special_features_lineEdit_tab1.setStyleSheet("background-color:white;")
                self.special_features_lineEdit_tab1.setObjectName("special_features_lineEdit_tab1")
                self.horizontalLayout_2.addWidget(self.special_features_lineEdit_tab1, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setObjectName("horizontalLayout")

                self.add_product_button_tab1 = QtWidgets.QPushButton(self.tab, clicked = lambda : self.add_product_button_clicked_tab1())
                font = QtGui.QFont()
                font.setFamily("Myanmar Text")
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.add_product_button_tab1.setFont(font)
                self.add_product_button_tab1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_product_button_tab1.setStyleSheet("padding:2px 20px;")
                self.add_product_button_tab1.setObjectName("add_product_button_tab1")
                self.horizontalLayout.addWidget(self.add_product_button_tab1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addLayout(self.horizontalLayout)
                self.verticalLayout.setStretch(0, 1)
                self.verticalLayout.setStretch(1, 1)
                self.verticalLayout.setStretch(2, 1)
                self.verticalLayout.setStretch(3, 1)
                self.verticalLayout.setStretch(4, 1)
                self.verticalLayout.setStretch(5, 1)
                self.horizontalLayout_8.addLayout(self.verticalLayout)
                self.tabWidget.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")
                self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.tab_2)
                self.horizontalLayout_22.setObjectName("horizontalLayout_22")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setSpacing(20)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_20.setObjectName("horizontalLayout_20")
                self.name_lineEdit_tab2 = QtWidgets.QLineEdit(self.tab_2)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.name_lineEdit_tab2.setFont(font)
                self.name_lineEdit_tab2.setStyleSheet("background-color:white;\n"
        "")
                self.name_lineEdit_tab2.setObjectName("name_lineEdit_tab2")
                self.horizontalLayout_20.addWidget(self.name_lineEdit_tab2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.date_tab2 = QtWidgets.QDateEdit(self.tab_2)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.date_tab2.setFont(font)
                self.date_tab2.setStyleSheet("background-color:white;\n"
        "padding:2px 0px;")
                self.date_tab2.setObjectName("date_tab2")
                self.horizontalLayout_20.addWidget(self.date_tab2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                
                self.add_customer_button_tab2 = QtWidgets.QPushButton(self.tab_2 , clicked = lambda : self.add_customer_button_tab2_clicked())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.add_customer_button_tab2.setFont(font)
                self.add_customer_button_tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_customer_button_tab2.setStyleSheet("padding:5px 20px;")
                self.add_customer_button_tab2.setObjectName("add_customer_button_tab2")
                self.horizontalLayout_20.addWidget(self.add_customer_button_tab2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout_2.addLayout(self.horizontalLayout_20)
                self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_19.setObjectName("horizontalLayout_19")
                self.customer_tableWidget_tab2 = QtWidgets.QTableWidget(self.tab_2)
                self.customer_tableWidget_tab2.setStyleSheet("background-color:white;")
                self.customer_tableWidget_tab2.setObjectName("customer_tableWidget_tab2")
                self.customer_tableWidget_tab2.setColumnCount(0)
                self.customer_tableWidget_tab2.setRowCount(0)
                self.horizontalLayout_19.addWidget(self.customer_tableWidget_tab2)
                self.customer_tableWidget_tab2.cellClicked.connect(self.update_current_selected_customer_row)

                self.verticalLayout_2.addLayout(self.horizontalLayout_19)
                self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_18.setObjectName("horizontalLayout_18")
                self.delete_button_tab2 = QtWidgets.QPushButton(self.tab_2, clicked = lambda : self.delete_customer_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab2.setFont(font)
                self.delete_button_tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab2.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab2.setObjectName("delete_button_tab2")
                self.horizontalLayout_18.addWidget(self.delete_button_tab2, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_2.addLayout(self.horizontalLayout_18)
                self.horizontalLayout_22.addLayout(self.verticalLayout_2)
                self.tabWidget.addTab(self.tab_2, "")
                self.tab_4 = QtWidgets.QWidget()
                self.tab_4.setObjectName("tab_4")
                self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.tab_4)
                self.horizontalLayout_30.setObjectName("horizontalLayout_30")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout()
                self.verticalLayout_4.setSpacing(20)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_27.setObjectName("horizontalLayout_27")
                self.label_11 = QtWidgets.QLabel(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_11")
                self.horizontalLayout_27.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.name_lineEdit_tab3 = QtWidgets.QLineEdit(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.name_lineEdit_tab3.setFont(font)
                self.name_lineEdit_tab3.setStyleSheet("background-color:white;\n"
        "")
                self.name_lineEdit_tab3.setObjectName("name_lineEdit_tab3")
                self.horizontalLayout_27.addWidget(self.name_lineEdit_tab3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.add_product_button_tab3 = QtWidgets.QPushButton(self.tab_4, clicked = lambda : self.add_product_button_clikced_tab_3())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.add_product_button_tab3.setFont(font)
                self.add_product_button_tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_product_button_tab3.setObjectName("add_product_button_tab3")
                self.horizontalLayout_27.addWidget(self.add_product_button_tab3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout_4.addLayout(self.horizontalLayout_27)
                self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_21.setObjectName("horizontalLayout_21")
                self.product_combo_tab3 = QtWidgets.QComboBox(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.product_combo_tab3.setFont(font)
                self.product_combo_tab3.setStyleSheet("background-color:white;")
                self.product_combo_tab3.setObjectName("product_combo_tab3")
                self.horizontalLayout_21.addWidget(self.product_combo_tab3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.label_13 = QtWidgets.QLabel(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.label_13.setFont(font)
                self.label_13.setObjectName("label_13")
                self.horizontalLayout_21.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.raw_material_combo_tab3 = QtWidgets.QComboBox(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.raw_material_combo_tab3.setFont(font)
                self.raw_material_combo_tab3.setStyleSheet("background-color:white;")
                self.raw_material_combo_tab3.setObjectName("raw_material_combo_tab3")
                self.horizontalLayout_21.addWidget(self.raw_material_combo_tab3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.quantity_lineEdit_tab3 = QtWidgets.QLineEdit(self.tab_4)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.quantity_lineEdit_tab3.setFont(font)
                self.quantity_lineEdit_tab3.setStyleSheet("background-color:white;")
                self.quantity_lineEdit_tab3.setObjectName("quantity_lineEdit_tab3")
                self.horizontalLayout_21.addWidget(self.quantity_lineEdit_tab3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.add_raw_material_button_tab3 = QtWidgets.QPushButton(self.tab_4,clicked = lambda : self.add_raw_material_button_clicked_tab3())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.add_raw_material_button_tab3.setFont(font)
                self.add_raw_material_button_tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_raw_material_button_tab3.setObjectName("add_raw_material_button_tab3")
                self.horizontalLayout_21.addWidget(self.add_raw_material_button_tab3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout_4.addLayout(self.horizontalLayout_21)
                self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_28.setObjectName("horizontalLayout_28")
                self.define_product_tableWidget_tab3 = QtWidgets.QTableWidget(self.tab_4)
                self.define_product_tableWidget_tab3.setStyleSheet("background-color:white;")
                self.define_product_tableWidget_tab3.setObjectName("define_product_tableWidget_tab3")
                self.define_product_tableWidget_tab3.setColumnCount(0)
                self.define_product_tableWidget_tab3.setRowCount(0)

                self.define_product_tableWidget_tab3.cellClicked.connect(self.update_current_selected_defined_product_row)
                self.horizontalLayout_28.addWidget(self.define_product_tableWidget_tab3)

                self.verticalLayout_4.addLayout(self.horizontalLayout_28)
                self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_29.setObjectName("horizontalLayout_29")
                
                self.delete_button_tab3 = QtWidgets.QPushButton(self.tab_4, clicked = lambda : self.delete_defined_product_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab3.setFont(font)
                self.delete_button_tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab3.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab3.setObjectName("delete_button_tab3")
                self.horizontalLayout_29.addWidget(self.delete_button_tab3, 0, QtCore.Qt.AlignHCenter)
                # self.see_details_button_tab3 = QtWidgets.QPushButton(self.tab_4)
                # font = QtGui.QFont()
                # font.setPointSize(12)
                # self.see_details_button_tab3.setFont(font)
                # self.see_details_button_tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                # self.see_details_button_tab3.setStyleSheet("padding:10px 30px;")
                # self.see_details_button_tab3.setObjectName("see_details_button_tab3")
                # self.horizontalLayout_29.addWidget(self.see_details_button_tab3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout_4.addLayout(self.horizontalLayout_29)
                self.horizontalLayout_30.addLayout(self.verticalLayout_4)
                self.tabWidget.addTab(self.tab_4, "")
                self.tab_5 = QtWidgets.QWidget()
                self.tab_5.setObjectName("tab_5")
                self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.tab_5)
                self.horizontalLayout_36.setObjectName("horizontalLayout_36")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout()
                self.verticalLayout_5.setSpacing(20)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_33.setObjectName("horizontalLayout_33")
                self.name_tab4 = QtWidgets.QLineEdit(self.tab_5)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.name_tab4.setFont(font)
                self.name_tab4.setStyleSheet("background-color:white;\n"
        "")
                self.name_tab4.setObjectName("name_tab4")
                self.horizontalLayout_33.addWidget(self.name_tab4, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.quantity_tab4 = QtWidgets.QLineEdit(self.tab_5)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.quantity_tab4.setFont(font)
                self.quantity_tab4.setStyleSheet("background-color:white;")
                self.quantity_tab4.setObjectName("quantity_tab4")
                self.horizontalLayout_33.addWidget(self.quantity_tab4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.add_raw_material_button_tab4 = QtWidgets.QPushButton(self.tab_5, clicked = lambda : self.add_raw_material_clicked_tab4())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.add_raw_material_button_tab4.setFont(font)
                self.add_raw_material_button_tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_raw_material_button_tab4.setStyleSheet("padding:5px 20px;")
                self.add_raw_material_button_tab4.setObjectName("add_raw_material_button_tab4")
                self.horizontalLayout_33.addWidget(self.add_raw_material_button_tab4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout_5.addLayout(self.horizontalLayout_33)
                self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_34.setObjectName("horizontalLayout_34")

                self.raw_material_tableWidget_tab4 = QtWidgets.QTableWidget(self.tab_5)
                self.raw_material_tableWidget_tab4.setStyleSheet("background-color:white;")
                self.raw_material_tableWidget_tab4.setObjectName("raw_material_tableWidget_tab4")
                self.raw_material_tableWidget_tab4.setColumnCount(0)
                self.raw_material_tableWidget_tab4.setRowCount(0)
                self.raw_material_tableWidget_tab4.cellClicked.connect(self.update_current_selected_raw_material_row)

                self.horizontalLayout_34.addWidget(self.raw_material_tableWidget_tab4)
                self.verticalLayout_5.addLayout(self.horizontalLayout_34)
                self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_35.setObjectName("horizontalLayout_35")
                
                self.delete_button_tab4 = QtWidgets.QPushButton(self.tab_5,clicked = lambda : self.delete_raw_material_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab4.setFont(font)
                self.delete_button_tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab4.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab4.setObjectName("delete_button_tab4")
                
                self.horizontalLayout_35.addWidget(self.delete_button_tab4, 0, QtCore.Qt.AlignHCenter)
                # self.see_details_button_tab4 = QtWidgets.QPushButton(self.tab_5)
                # font = QtGui.QFont()
                # font.setPointSize(12)
                # self.see_details_button_tab4.setFont(font)
                # self.see_details_button_tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                # self.see_details_button_tab4.setStyleSheet("padding:10px 30px;")
                # self.see_details_button_tab4.setObjectName("see_details_button_tab4")
                # self.horizontalLayout_35.addWidget(self.see_details_button_tab4, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_5.addLayout(self.horizontalLayout_35)
                self.horizontalLayout_36.addLayout(self.verticalLayout_5)
                self.tabWidget.addTab(self.tab_5, "")
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setObjectName("tab_3")
                self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.tab_3)
                self.horizontalLayout_26.setObjectName("horizontalLayout_26")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout()
                self.verticalLayout_3.setSpacing(20)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_23.setObjectName("horizontalLayout_23")
                self.employee_name_tab5 = QtWidgets.QLineEdit(self.tab_3)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.employee_name_tab5.setFont(font)
                self.employee_name_tab5.setStyleSheet("background-color:white;\n"
        "")
                self.employee_name_tab5.setObjectName("employee_name_tab5")
                self.horizontalLayout_23.addWidget(self.employee_name_tab5, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.date_add_employee_tab5 = QtWidgets.QDateEdit(self.tab_3)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.date_add_employee_tab5.setFont(font)
                self.date_add_employee_tab5.setStyleSheet("background-color:white;")
                self.date_add_employee_tab5.setObjectName("date_add_employee_tab5")
                self.horizontalLayout_23.addWidget(self.date_add_employee_tab5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                
                self.add_employee_button_tab5 = QtWidgets.QPushButton(self.tab_3, clicked = lambda : self.add_employee_button_tab5_clicked())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.add_employee_button_tab5.setFont(font)
                self.add_employee_button_tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.add_employee_button_tab5.setStyleSheet("padding:5px 20px;")
                self.add_employee_button_tab5.setObjectName("add_employee_button_tab5")
                self.horizontalLayout_23.addWidget(self.add_employee_button_tab5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout_3.addLayout(self.horizontalLayout_23)
                self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_24.setObjectName("horizontalLayout_24")
                self.employees_tableWidget_tab5 = QtWidgets.QTableWidget(self.tab_3)
                self.employees_tableWidget_tab5.setStyleSheet("background-color:white;")
                self.employees_tableWidget_tab5.setObjectName("employees_tableWidget_tab5")
                self.employees_tableWidget_tab5.setColumnCount(0)
                self.employees_tableWidget_tab5.setRowCount(0)
                self.employees_tableWidget_tab5.cellClicked.connect(self.update_current_selected_employee_row)

                self.horizontalLayout_24.addWidget(self.employees_tableWidget_tab5)
                self.verticalLayout_3.addLayout(self.horizontalLayout_24)
                self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                self.delete_button_tab5 = QtWidgets.QPushButton(self.tab_3, clicked = lambda : self.delete_employee_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab5.setFont(font)
                self.delete_button_tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab5.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab5.setObjectName("delete_button_tab5")
                self.horizontalLayout_25.addWidget(self.delete_button_tab5, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_3.addLayout(self.horizontalLayout_25)
        #         self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        #         self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        #         self.employee_name_combo_tab5 = QtWidgets.QComboBox(self.tab_3)
        #         font = QtGui.QFont()
        #         font.setPointSize(12)
        #         self.employee_name_combo_tab5.setFont(font)
        #         self.employee_name_combo_tab5.setStyleSheet("background-color:white;")
        #         self.employee_name_combo_tab5.setObjectName("employee_name_combo_tab5")
        #         self.horizontalLayout_31.addWidget(self.employee_name_combo_tab5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #         self.from_date_tab5 = QtWidgets.QDateEdit(self.tab_3)
        #         font = QtGui.QFont()
        #         font.setPointSize(12)
        #         self.from_date_tab5.setFont(font)
        #         self.from_date_tab5.setStyleSheet("background-color:white;\n"
        # "padding:2px 0px;")
        #         self.from_date_tab5.setObjectName("from_date_tab5")
        #         self.horizontalLayout_31.addWidget(self.from_date_tab5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #         self.to_date_tab5 = QtWidgets.QDateEdit(self.tab_3)
        #         font = QtGui.QFont()
        #         font.setPointSize(12)
        #         self.to_date_tab5.setFont(font)
        #         self.to_date_tab5.setStyleSheet("background-color:white;")
        #         self.to_date_tab5.setObjectName("to_date_tab5")
        #         self.horizontalLayout_31.addWidget(self.to_date_tab5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #         self.see_products_button_tab5 = QtWidgets.QPushButton(self.tab_3)
        #         font = QtGui.QFont()
        #         font.setPointSize(12)
        #         self.see_products_button_tab5.setFont(font)
        #         self.see_products_button_tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #         self.see_products_button_tab5.setStyleSheet("padding:10px 30px;")
        #         self.see_products_button_tab5.setObjectName("see_products_button_tab5")
        #         self.horizontalLayout_31.addWidget(self.see_products_button_tab5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        #         self.verticalLayout_3.addLayout(self.horizontalLayout_31)
                # self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
                # self.horizontalLayout_32.setObjectName("horizontalLayout_32")
                # self.results_textedit_tab5 = QtWidgets.QTextEdit(self.tab_3)
                # self.results_textedit_tab5.setStyleSheet("background-color:white;")
                # self.results_textedit_tab5.setObjectName("results_textedit_tab5")
                # self.horizontalLayout_32.addWidget(self.results_textedit_tab5)
                # self.verticalLayout_3.addLayout(self.horizontalLayout_32)
                self.verticalLayout_3.setStretch(0, 1)
                self.verticalLayout_3.setStretch(1, 5)
                self.verticalLayout_3.setStretch(2, 1)
                self.verticalLayout_3.setStretch(3, 1)
                self.verticalLayout_3.setStretch(4, 2)
                self.horizontalLayout_26.addLayout(self.verticalLayout_3)
                self.tabWidget.addTab(self.tab_3, "")
                self.tab_6 = QtWidgets.QWidget()
                self.tab_6.setObjectName("tab_6")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_6)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout()
                self.verticalLayout_6.setSpacing(20)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_37.setObjectName("horizontalLayout_37")
                self.product_combo_tab6 = QtWidgets.QComboBox(self.tab_6)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.product_combo_tab6.setFont(font)
                self.product_combo_tab6.setStyleSheet("background-color:white;")
                self.product_combo_tab6.setObjectName("product_combo_tab6")
                self.horizontalLayout_37.addWidget(self.product_combo_tab6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.customer_combo_tab6 = QtWidgets.QComboBox(self.tab_6)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.customer_combo_tab6.setFont(font)
                self.customer_combo_tab6.setStyleSheet("background-color:white;")
                self.customer_combo_tab6.setObjectName("customer_combo_tab6")
                self.horizontalLayout_37.addWidget(self.customer_combo_tab6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                
                self.deliver_product_button_tab6 = QtWidgets.QPushButton(self.tab_6, clicked = lambda : self.deliver_product_button_tab6_clicked())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.deliver_product_button_tab6.setFont(font)
                self.deliver_product_button_tab6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.deliver_product_button_tab6.setStyleSheet("padding:5px 20px;")
                self.deliver_product_button_tab6.setObjectName("deliver_product_button_tab6")
                self.horizontalLayout_37.addWidget(self.deliver_product_button_tab6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.verticalLayout_6.addLayout(self.horizontalLayout_37)
                self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_38.setObjectName("horizontalLayout_38")
                self.finished_products_tableWidget_tab6 = QtWidgets.QTableWidget(self.tab_6)
                self.finished_products_tableWidget_tab6.setStyleSheet("background-color:white;")
                self.finished_products_tableWidget_tab6.setObjectName("finished_products_tableWidget_tab6")
                self.finished_products_tableWidget_tab6.setColumnCount(0)
                self.finished_products_tableWidget_tab6.setRowCount(0)
                self.finished_products_tableWidget_tab6.cellClicked.connect(self.update_current_selected_finished_product_row)
                
                self.horizontalLayout_38.addWidget(self.finished_products_tableWidget_tab6)
                self.verticalLayout_6.addLayout(self.horizontalLayout_38)
                self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_39.setObjectName("horizontalLayout_39")
                self.delete_button_tab6 = QtWidgets.QPushButton(self.tab_6, clicked = lambda : self.delete_finished_product_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab6.setFont(font)
                self.delete_button_tab6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab6.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab6.setObjectName("delete_button_tab6")
                self.horizontalLayout_39.addWidget(self.delete_button_tab6, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_6.addLayout(self.horizontalLayout_39)
                self.horizontalLayout_7.addLayout(self.verticalLayout_6)
                self.tabWidget.addTab(self.tab_6, "")
                self.tab_7 = QtWidgets.QWidget()
                self.tab_7.setObjectName("tab_7")
                self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.tab_7)
                self.horizontalLayout_43.setObjectName("horizontalLayout_43")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout()
                self.verticalLayout_7.setSpacing(20)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_41.setObjectName("horizontalLayout_41")
                self.products_table_tableWidget_tab7 = QtWidgets.QTableWidget(self.tab_7)
                self.products_table_tableWidget_tab7.setStyleSheet("background-color:white;")
                self.products_table_tableWidget_tab7.setObjectName("products_table_tableWidget_tab7")
                self.products_table_tableWidget_tab7.setColumnCount(0)
                self.products_table_tableWidget_tab7.setRowCount(0)
                self.products_table_tableWidget_tab7.cellClicked.connect(self.update_current_selected_delivered_product_row)
                
                self.horizontalLayout_41.addWidget(self.products_table_tableWidget_tab7)
                self.verticalLayout_7.addLayout(self.horizontalLayout_41)
                self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_42.setObjectName("horizontalLayout_42")
                self.delete_button_tab7 = QtWidgets.QPushButton(self.tab_7, clicked = lambda : self.delete_delivered_product_data())
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delete_button_tab7.setFont(font)
                self.delete_button_tab7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.delete_button_tab7.setStyleSheet("padding:10px 30px;")
                self.delete_button_tab7.setObjectName("delete_button_tab7")
                self.horizontalLayout_42.addWidget(self.delete_button_tab7, 0, QtCore.Qt.AlignHCenter)
                self.verticalLayout_7.addLayout(self.horizontalLayout_42)
                self.horizontalLayout_43.addLayout(self.verticalLayout_7)
                self.tabWidget.addTab(self.tab_7, "")
                self.horizontalLayout_9.addWidget(self.tabWidget)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                # startup code 
                self.__defined_product_table_settings()
                self.__raw_materials_table_settings()
                self.__employee_table_settings()
                self.__finished_products_table_settings()
                self.__customer_table_settings()
                self.__delivered_table_settings()

                # vars 
                self.current_selected_customer_row = None
                self.current_selected_defined_product_row = None
                self.current_selected_raw_material_row = None
                self.current_selected_employee_row = None
                self.current_selected_finished_product_row = None
                self.current_selected_delivered_product_row = None


                self.db_instance = db.WarehouseDBHandler()
                
                # tables and combos filling
                self.__fill_raw_materials_table()
                self.__fill_raw_materials_combos()

                self.__fill_defined_product_table()
                self.__fill_defined_product_combos()

                self.__fill_employee_table()
                self.__fill_employee_combos()

                self.__fill_finished_products_table()
                self.__fill_finished_products_combos()

                self.__fill_customer_table()
                self.__fill_customer_combos()

                self.__fill_delivered_table()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Warehouse Management System"))
                self.label.setText(_translate("MainWindow", "Artical Number"))
                self.label_2.setText(_translate("MainWindow", "Artical Name"))
                self.label_5.setText(_translate("MainWindow", "Production Date"))
                self.label_6.setText(_translate("MainWindow", "Best Before"))
                self.label_7.setText(_translate("MainWindow", "Batch Number"))
                self.label_8.setText(_translate("MainWindow", "Quantity"))
                self.label_3.setText(_translate("MainWindow", "Produng Employee"))
                self.label_4.setText(_translate("MainWindow", "Product"))
                self.label_9.setText(_translate("MainWindow", "Special Features"))
                self.add_product_button_tab1.setText(_translate("MainWindow", "Add Product"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Product"))
                self.name_lineEdit_tab2.setPlaceholderText(_translate("MainWindow", "Name"))
                self.add_customer_button_tab2.setText(_translate("MainWindow", "Add Customer"))
                self.delete_button_tab2.setText(_translate("MainWindow", "Delete"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Customer"))
                self.label_11.setText(_translate("MainWindow", "Product Name"))
                self.name_lineEdit_tab3.setPlaceholderText(_translate("MainWindow", "Name"))
                self.add_product_button_tab3.setText(_translate("MainWindow", "Add Product"))
                self.label_13.setText(_translate("MainWindow", "Raw Material"))
                self.quantity_lineEdit_tab3.setPlaceholderText(_translate("MainWindow", "Quantity"))
                self.add_raw_material_button_tab3.setText(_translate("MainWindow", "Add Raw Material"))
                self.delete_button_tab3.setText(_translate("MainWindow", "Delete"))
                # self.see_details_button_tab3.setText(_translate("MainWindow", "See Details"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Define Products"))
                self.name_tab4.setPlaceholderText(_translate("MainWindow", "Name"))
                self.quantity_tab4.setPlaceholderText(_translate("MainWindow", "Quantity"))
                self.add_raw_material_button_tab4.setText(_translate("MainWindow", "Add Raw Material"))
                self.delete_button_tab4.setText(_translate("MainWindow", "Delete"))
                # self.see_details_button_tab4.setText(_translate("MainWindow", "See Details"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Raw Material"))
                self.employee_name_tab5.setPlaceholderText(_translate("MainWindow", "Employee Name"))
                self.add_employee_button_tab5.setText(_translate("MainWindow", "Add Employee"))
                self.delete_button_tab5.setText(_translate("MainWindow", "Delete"))
                # self.see_products_button_tab5.setText(_translate("MainWindow", "See Products"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Employee"))
                self.deliver_product_button_tab6.setText(_translate("MainWindow", "Deliver Product"))
                self.delete_button_tab6.setText(_translate("MainWindow", "Delete"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Finished Products"))
                self.delete_button_tab7.setText(_translate("MainWindow", "Delete"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Delivered Products"))
                                              

        # delete Functions
        def update_current_selected_customer_row(self, row, col):
                self.current_selected_customer_row = row        

        def update_current_selected_defined_product_row(self, row, col):
                self.current_selected_defined_product_row = row        

        def update_current_selected_raw_material_row(self, row, col):
                self.current_selected_raw_material_row = row        

        def update_current_selected_employee_row(self, row, col):
                self.current_selected_employee_row = row        

        def update_current_selected_finished_product_row(self, row, col):
                self.current_selected_finished_product_row = row        

        def update_current_selected_delivered_product_row(self, row, col):
                self.current_selected_delivered_product_row = row        


        def delete_customer_data(self):
                if self.current_selected_customer_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_customer(self.customer_tableWidget_tab2.item(self.current_selected_customer_row,0).text())                                
                                if delete:
                                        self.customer_tableWidget_tab2.removeRow(self.current_selected_customer_row)
                                        self.current_selected_customer_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        def delete_defined_product_data(self):
                if self.current_selected_defined_product_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_defined_product(self.define_product_tableWidget_tab3.item(self.current_selected_defined_product_row,0).text())                                
                                if delete:
                                        self.define_product_tableWidget_tab3.removeRow(self.current_selected_defined_product_row)
                                        self.current_selected_defined_product_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        def delete_raw_material_data(self):
                if self.current_selected_raw_material_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_raw_material(self.raw_material_tableWidget_tab4.item(self.current_selected_raw_material_row,0).text())                                
                                if delete:
                                        self.raw_material_tableWidget_tab4.removeRow(self.current_selected_raw_material_row)
                                        self.current_selected_raw_material_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        def delete_employee_data(self):
                if self.current_selected_employee_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_employee(self.employees_tableWidget_tab5.item(self.current_selected_employee_row,0).text())                                
                                if delete:
                                        self.employees_tableWidget_tab5.removeRow(self.current_selected_employee_row)
                                        self.current_selected_employee_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        def delete_finished_product_data(self):
                if self.current_selected_finished_product_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_finished_product(self.finished_products_tableWidget_tab6.item(self.current_selected_finished_product_row,0).text())                                
                                if delete:
                                        self.finished_products_tableWidget_tab6.removeRow(self.current_selected_finished_product_row)
                                        self.current_selected_finished_product_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        def delete_delivered_product_data(self):
                if self.current_selected_delivered_product_row is not None: 
                        reply = QMessageBox.question(
                                None,
                                'Confirmation',
                                'Are you sure you want to delete?',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No
                                )

                        # Check the user's response
                        if reply == QMessageBox.Yes:
                                # User clicked "Yes," so close and destroy the window                                                    
                                delete = self.db_instance.delete_finished_product(self.products_table_tableWidget_tab7.item(self.current_selected_delivered_product_row,0).text())                                
                                if delete:
                                        self.products_table_tableWidget_tab7.removeRow(self.current_selected_delivered_product_row)
                                        self.current_selected_delivered_product_row = None
                                        
                else:
                        QMessageBox.information(None,'Error','Please select row first')

        # Initial Raw Material functions
        def __raw_materials_table_settings(self):
                self.raw_material_tableWidget_tab4.setColumnCount(3)
                column_names = ['Raw Material ID','Name','Quantity']
                self.raw_material_tableWidget_tab4.setHorizontalHeaderLabels(column_names)
                self.raw_material_tableWidget_tab4.verticalHeader().setVisible(False)

        def __fill_raw_materials_combos(self):                
                raw_materials_list = self.db_instance.get_all_raw_materials_ids()                
                if raw_materials_list:                        
                        self.raw_material_combo_tab3.clear()
                        raw_materials_list.insert(0,'')
                        self.raw_material_combo_tab3.addItems(raw_materials_list)

        def __fill_raw_materials_table(self):                
                raw_materials_list = self.db_instance.get_all_raw_materials()                
                if raw_materials_list:                                                                        
                        self.raw_material_tableWidget_tab4.setRowCount(0)
                        self.__raw_materials_table_settings()
                        
                        for row_index, row_data in enumerate(raw_materials_list):                                
                                self.raw_material_tableWidget_tab4.insertRow(row_index)
                                for column_index, cell_data in enumerate(row_data):
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.raw_material_tableWidget_tab4.setItem(row_index, column_index, item)

        # Initial Defined Product functions
        def __defined_product_table_settings(self):
                self.define_product_tableWidget_tab3.setColumnCount(3)
                column_names = ['Defined Product ID','Name','Raw Materials']
                self.define_product_tableWidget_tab3.setHorizontalHeaderLabels(column_names)
                self.define_product_tableWidget_tab3.verticalHeader().setVisible(False)                                        

        def __fill_defined_product_combos(self):
                defined_products_lists = self.db_instance.get_defined_products_ids()

                if defined_products_lists:
                        # print(defined_products_lists)
                        self.product_combo_tab3.clear()
                        self.product_combo_tab1.clear()

                        defined_products_lists.insert(0,'')
                        
                        self.product_combo_tab3.addItems(defined_products_lists)

                        self.product_combo_tab1.addItems(defined_products_lists)

        def __fill_defined_product_table(self):
                defined_products_lists = self.db_instance.get_all_defined_products()

                if defined_products_lists:                                                                        
                        self.define_product_tableWidget_tab3.setRowCount(0)
                        self.__raw_materials_table_settings()
                        
                        for row_index, row_data in enumerate(defined_products_lists):                                
                                self.define_product_tableWidget_tab3.insertRow(row_index)                                
                                for column_index, cell_data in enumerate(row_data):                                        
                                        if isinstance(cell_data,bytes):
                                                cell_data = cell_data.decode('utf-8')                                        
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.define_product_tableWidget_tab3.setItem(row_index, column_index, item)

        # Initial Employee Functions
        def __employee_table_settings(self):
                self.employees_tableWidget_tab5.setColumnCount(3)
                column_names = ['Employee ID','Name','Joining Date']
                self.employees_tableWidget_tab5.setHorizontalHeaderLabels(column_names)
                self.employees_tableWidget_tab5.verticalHeader().setVisible(False)
        
        def __fill_employee_combos(self):
                employee_list = self.db_instance.get_all_employee_ids()

                if employee_list:
                        self.producing_employee_combo_tab1.clear()
                        # self.employee_name_combo_tab5.clear()

                        employee_list.insert(0,'')

                        self.producing_employee_combo_tab1.addItems(employee_list)
                        # self.employee_name_combo_tab5.addItems(employee_list)

        def __fill_employee_table(self):
                employee_data = self.db_instance.get_all_employees()

                if employee_data:                                                                        
                        self.employees_tableWidget_tab5.setRowCount(0)
                        self.__employee_table_settings()
                        
                        for row_index, row_data in enumerate(employee_data):                                
                                self.employees_tableWidget_tab5.insertRow(row_index)                                
                                for column_index, cell_data in enumerate(row_data):                                        
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.employees_tableWidget_tab5.setItem(row_index, column_index, item)


        # Initial Product tab 1 Functions
        def __finished_products_table_settings(self):
                self.finished_products_tableWidget_tab6.setColumnCount(10)
                column_names = ['Product ID','Artical Number','Artical Name','Production Data','Best Before','Batch Number','Quantity','Producing Employee','Product','Special Features']
                self.finished_products_tableWidget_tab6.setHorizontalHeaderLabels(column_names)
                self.finished_products_tableWidget_tab6.verticalHeader().setVisible(False)

        def __fill_finished_products_combos(self):
                product_list = self.db_instance.get_all_finished_products_ids()

                if product_list:
                        self.product_combo_tab6.clear()

                        product_list.insert(0,'')

                        self.product_combo_tab6.addItems(product_list)
        
        def __fill_finished_products_table(self):
                finished_products = self.db_instance.get_all_finished_products()

                if finished_products:
                        self.finished_products_tableWidget_tab6.setRowCount(0)
                        self.__finished_products_table_settings()
                        
                        for row_index, row_data in enumerate(finished_products):                                
                                self.finished_products_tableWidget_tab6.insertRow(row_index)                                
                                for column_index, cell_data in enumerate(row_data):                                        
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.finished_products_tableWidget_tab6.setItem(row_index, column_index, item)


        # Initial Customer Functions
        def __customer_table_settings(self):
                self.customer_tableWidget_tab2.setColumnCount(3)
                column_names = ['Customer ID','Name','Date Added']
                self.customer_tableWidget_tab2.setHorizontalHeaderLabels(column_names)
                self.customer_tableWidget_tab2.verticalHeader().setVisible(False)

        def __fill_customer_combos(self):
                customer_list = self.db_instance.get_customer_ids()

                if customer_list:
                        self.customer_combo_tab6.clear()

                        customer_list.insert(0,'')

                        self.customer_combo_tab6.addItems(customer_list)

        def __fill_customer_table(self):
                customers = self.db_instance.get_all_customers()

                if customers:
                        self.customer_tableWidget_tab2.setRowCount(0)
                        self.__customer_table_settings()
                        
                        for row_index, row_data in enumerate(customers):                                
                                self.customer_tableWidget_tab2.insertRow(row_index)                                
                                for column_index, cell_data in enumerate(row_data):                                        
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.customer_tableWidget_tab2.setItem(row_index, column_index, item)


        # Delivered Product Table
        def __delivered_table_settings(self):
                self.products_table_tableWidget_tab7.setColumnCount(3)
                column_names = ['Delivered ID','Product ID','Customer Name']
                self.products_table_tableWidget_tab7.setHorizontalHeaderLabels(column_names)
                self.products_table_tableWidget_tab7.verticalHeader().setVisible(False)

        def __fill_delivered_table(self):
                products = self.db_instance.read_delivered_products()

                if products:
                        self.products_table_tableWidget_tab7.setRowCount(0)
                        self.__delivered_table_settings()
                        
                        for row_index, row_data in enumerate(products):                                
                                self.products_table_tableWidget_tab7.insertRow(row_index)                                
                                for column_index, cell_data in enumerate(row_data):                                        
                                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                                        self.products_table_tableWidget_tab7.setItem(row_index, column_index, item)

        # Raw Materials Tab 4 Clicked Functions
        def add_raw_material_clicked_tab4(self):
                if self.name_tab4.text() == '' or self.quantity_tab4.text() == '':
                        QMessageBox.information(None,'ERROR','Fill all the fields!')                                                
                        
                else:                        
                        self.db_instance.insert_raw_material(self.name_tab4.text(),self.quantity_tab4.text())

                        self.name_tab4.clear()
                        self.quantity_tab4.clear()
                        
                        self.__fill_raw_materials_table()
                        self.__fill_raw_materials_combos()
                        QMessageBox.information(None,'SUCCESS','Raw materials added!')
        

        # Define Products Tab 3 CLicked Functions
        def add_product_button_clikced_tab_3(self):
                if self.name_lineEdit_tab3.text() == '':
                        QMessageBox.information(None,'ERROR','Fill all the fields!')                                                

                else:
                        query = self.db_instance.insert_defined_product(self.name_lineEdit_tab3.text(),{})

                        if query:
                                self.name_lineEdit_tab3.clear()
                                
                                self.__fill_defined_product_table()
                                self.__fill_defined_product_combos()
                                QMessageBox.information(None,'SUCCESS','Product added successfully!')
                        else:
                                QMessageBox.information(None,'FAILURE','Product could not added!')


        def add_raw_material_button_clicked_tab3(self):
                if self.product_combo_tab3.currentText() == '' or self.raw_material_combo_tab3.currentText() == '' or self.quantity_lineEdit_tab3.text() == '':
                        QMessageBox.information(None,'ERROR','Fill all the fields!')                                                

                else:
                        product_id = int(self.product_combo_tab3.currentText().split(':')[1])                        
                        raw_material = self.raw_material_combo_tab3.currentText().split(':')[0]
                        raw_materials = self.db_instance.get_defined_products_blob(product_id)                        
                        if raw_material in raw_materials[0]:
                                raw_materials[0][raw_material] += int(self.quantity_lineEdit_tab3.text())
                        else:
                                raw_materials[0][raw_material] = int(self.quantity_lineEdit_tab3.text())

                        self.db_instance.update_defined_product_blob(product_id,raw_materials)
                                                
                        self.product_combo_tab3.setCurrentIndex(0)
                        self.raw_material_combo_tab3.setCurrentIndex(0)
                        self.quantity_lineEdit_tab3.clear()

                        self.__fill_defined_product_table()
                        QMessageBox.information(None,'SUCCESS','Raw Materials Updated!')



        def add_product_clicked_tab3(self):
                if self.name_lineEdit_tab3.text() == '':
                        QMessageBox.information(None,'ERROR','Name field is empty!')

                else:
                        query = self.db_instance.insert_defined_product(self.name_lineEdit_tab3.text(),'')

                        if query:
                                self.name_lineEdit_tab3.clear()
                                QMessageBox.information(None,'SUCCESS','Product added successfully!')
                        else:
                                QMessageBox.information(None,'FAILURE','Product could not be added!')


        # Employee Tab 5
        def add_employee_button_tab5_clicked(self):
                if self.employee_name_tab5.text() == '':
                        QMessageBox.information(None,'ERROR','Name field is empty!')
                else:                        
                        query = self.db_instance.insert_employee(self.employee_name_tab5.text(),self.date_add_employee_tab5.text())
                        
                        if query:
                                self.employee_name_tab5.clear()

                                self.__fill_employee_combos()
                                self.__fill_employee_table()
                                QMessageBox.information(None,'SUCCESS','Employee added successfully!')
                        else:
                                QMessageBox.information(None,'FAILURE','Employee could not be added!')


        # Add Product Tab 1 clicked Functions
        def add_product_button_clicked_tab1(self): 
                if self.artical_name_lineEdit_tab1.text() == '' or self.artical_number_lineEdit_tab1.text() == '' or \
                        self.production_date_tab1.text() == '' or self.best_before_date_tab1.text() == '' or \
                        self.batch_number_lineEdit_tab1.text() == '' or self.quantity_lineEdit_tab1.text() == '' or \
                        self.producing_employee_combo_tab1.currentText() == '' or self.product_combo_tab1.currentText() == '':
                       
                        QMessageBox.information(None,'FAILURE','Fill all the fields first!')

                else:
                        try:
                        # get raw material against the product 
                                defined_products_raw_material = self.db_instance.get_defined_products_blob(int(self.product_combo_tab1.currentText().split(':')[1]))                                
                                # [(1, 'tiles', 10), (2, 'cement', 5), (3, 'files', 80), (4, 'Junaid', 20), (6, 'filess', 1), (8, 'hadi', 49), (9, 'garments', 20)]
                                
                                not_enough_raw_material = False
                                updated_raw_materials = {}

                                for i in defined_products_raw_material[0]:                                        
                                        inventory_raw_material = self.db_instance.get_raw_material_by_name(i)                                        
                                        if inventory_raw_material and inventory_raw_material['quantity'] >= int(defined_products_raw_material[0][i]) * int(self.quantity_lineEdit_tab1.text()):
                                                updated_raw_materials[inventory_raw_material["id"]] = inventory_raw_material['quantity'] - int(defined_products_raw_material[0][i]) * int(self.quantity_lineEdit_tab1.text())
                                        else:
                                                not_enough_raw_material = True
                                                break

                                if not_enough_raw_material:
                                        QMessageBox.information(None,'FAILURE','Not enough raw material!')

                                else:                                        
                                        query = self.db_instance.insert_finished_product(self.artical_number_lineEdit_tab1.text(),self.artical_name_lineEdit_tab1.text(),
                                                                                self.production_date_tab1.text() , self.best_before_date_tab1.text(), 
                                                                                self.batch_number_lineEdit_tab1.text(), self.quantity_lineEdit_tab1.text(),
                                                                                self.producing_employee_combo_tab1.currentText().split(':')[0],self.product_combo_tab1.currentText().split(':')[0],
                                                                                self.special_features_lineEdit_tab1.text())
                                
                                        if query:
                                                for i in updated_raw_materials:
                                                        self.db_instance.update_raw_material(i,updated_raw_materials[i])                                                
                                                
                                                self.artical_number_lineEdit_tab1.clear()
                                                self.artical_name_lineEdit_tab1.clear()                         
                                                self.batch_number_lineEdit_tab1.clear()                                       
                                                self.quantity_lineEdit_tab1.clear()
                                                self.special_features_lineEdit_tab1.clear()
                                                self.product_combo_tab1.setCurrentIndex(0)
                                                self.producing_employee_combo_tab1.setCurrentIndex(0)                                                

                                                self.__fill_finished_products_combos()
                                                self.__fill_finished_products_table()
                                                self.__fill_raw_materials_table()
                                                QMessageBox.information(None,'SUCCESS','Product added successfully!')
                                        
                                        else:
                                                QMessageBox.information(None,'FAILURE','Product could not be added!')
                        
                        except Exception as e:                       
                                print(f'ERROR - {str(e)}')


        # Customer Tab 2 Clicked Functions
        def add_customer_button_tab2_clicked(self):
                if self.name_lineEdit_tab2.text() == '':
                        pass
                else:
                        query = self.db_instance.insert_customer(self.name_lineEdit_tab2.text(),self.date_tab2.text())
                        if query:
                                self.name_lineEdit_tab2.clear()

                                self.__fill_customer_table()
                                self.__fill_customer_combos()                              
                                QMessageBox.information(None,'SUCCESS','Customer added successfully!')


        # Delivered Product Tab 7
        def deliver_product_button_tab6_clicked(self):                
                if self.product_combo_tab6.currentText() == '' or self.customer_combo_tab6.currentText() == '':
                        pass
                else:
                        product_id = int(self.product_combo_tab6.currentText().split(':')[1])
                        customer_name = self.customer_combo_tab6.currentText().split(':')[0]

                        q = self.db_instance.insert_delivered_product(product_id,customer_name)                        
                        if q:
                                self.__fill_delivered_table()
                                QMessageBox.information(None,'SUCCESS','Product delivered successfully!')
                                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
