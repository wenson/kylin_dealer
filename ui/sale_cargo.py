# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/sale_cargo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaleDialog(object):
    def setupUi(self, SaleDialog):
        SaleDialog.setObjectName("SaleDialog")
        SaleDialog.resize(650, 399)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaleDialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 360, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(SaleDialog)
        self.label.setGeometry(QtCore.QRect(30, 19, 60, 21))
        self.label.setObjectName("label")
        self.customNameLabel = QtWidgets.QLabel(SaleDialog)
        self.customNameLabel.setGeometry(QtCore.QRect(80, 19, 60, 21))
        self.customNameLabel.setObjectName("customNameLabel")
        self.chooseCustomBtn = QtWidgets.QPushButton(SaleDialog)
        self.chooseCustomBtn.setGeometry(QtCore.QRect(152, 10, 91, 41))
        self.chooseCustomBtn.setObjectName("chooseCustomBtn")
        self.saleListTable = QtWidgets.QTableWidget(SaleDialog)
        self.saleListTable.setGeometry(QtCore.QRect(10, 180, 631, 171))
        self.saleListTable.setObjectName("saleListTable")
        self.saleListTable.setColumnCount(6)
        self.saleListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.saleListTable.setHorizontalHeaderItem(5, item)
        self.label_2 = QtWidgets.QLabel(SaleDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 67, 60, 21))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(SaleDialog)
        self.dateEdit.setGeometry(QtCore.QRect(80, 60, 161, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.addCargoBtn = QtWidgets.QPushButton(SaleDialog)
        self.addCargoBtn.setGeometry(QtCore.QRect(20, 110, 221, 61))
        self.addCargoBtn.setObjectName("addCargoBtn")
        self.label_3 = QtWidgets.QLabel(SaleDialog)
        self.label_3.setGeometry(QtCore.QRect(300, 20, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SaleDialog)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(SaleDialog)
        self.label_5.setGeometry(QtCore.QRect(300, 95, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SaleDialog)
        self.label_6.setGeometry(QtCore.QRect(300, 140, 81, 31))
        self.label_6.setObjectName("label_6")
        self.commentEdit = QtWidgets.QLineEdit(SaleDialog)
        self.commentEdit.setGeometry(QtCore.QRect(370, 140, 261, 31))
        self.commentEdit.setObjectName("commentEdit")
        self.oweEdit = QtWidgets.QLineEdit(SaleDialog)
        self.oweEdit.setGeometry(QtCore.QRect(370, 95, 81, 31))
        self.oweEdit.setObjectName("oweEdit")
        self.label_7 = QtWidgets.QLabel(SaleDialog)
        self.label_7.setGeometry(QtCore.QRect(460, 100, 21, 21))
        self.label_7.setObjectName("label_7")
        self.payEdit = QtWidgets.QLineEdit(SaleDialog)
        self.payEdit.setGeometry(QtCore.QRect(370, 55, 81, 31))
        self.payEdit.setObjectName("payEdit")
        self.label_8 = QtWidgets.QLabel(SaleDialog)
        self.label_8.setGeometry(QtCore.QRect(460, 60, 21, 21))
        self.label_8.setObjectName("label_8")
        self.needPayEdit = QtWidgets.QLineEdit(SaleDialog)
        self.needPayEdit.setGeometry(QtCore.QRect(370, 15, 81, 31))
        self.needPayEdit.setObjectName("needPayEdit")
        self.label_9 = QtWidgets.QLabel(SaleDialog)
        self.label_9.setGeometry(QtCore.QRect(460, 20, 21, 21))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(SaleDialog)
        self.buttonBox.accepted.connect(SaleDialog.accept)
        self.buttonBox.rejected.connect(SaleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaleDialog)

    def retranslateUi(self, SaleDialog):
        _translate = QtCore.QCoreApplication.translate
        SaleDialog.setWindowTitle(_translate("SaleDialog", "出货"))
        self.label.setText(_translate("SaleDialog", "客户："))
        self.customNameLabel.setText(_translate("SaleDialog", "未选择"))
        self.chooseCustomBtn.setText(_translate("SaleDialog", "选择客户..."))
        item = self.saleListTable.horizontalHeaderItem(0)
        item.setText(_translate("SaleDialog", "货物种类"))
        item = self.saleListTable.horizontalHeaderItem(1)
        item.setText(_translate("SaleDialog", "单位"))
        item = self.saleListTable.horizontalHeaderItem(2)
        item.setText(_translate("SaleDialog", "数量"))
        item = self.saleListTable.horizontalHeaderItem(3)
        item.setText(_translate("SaleDialog", "生产日期"))
        item = self.saleListTable.horizontalHeaderItem(4)
        item.setText(_translate("SaleDialog", "保质期"))
        item = self.saleListTable.horizontalHeaderItem(5)
        item.setText(_translate("SaleDialog", "售价"))
        self.label_2.setText(_translate("SaleDialog", "日期："))
        self.addCargoBtn.setText(_translate("SaleDialog", "添加货物"))
        self.label_3.setText(_translate("SaleDialog", "应付货款："))
        self.label_4.setText(_translate("SaleDialog", "实付货款："))
        self.label_5.setText(_translate("SaleDialog", "欠款："))
        self.label_6.setText(_translate("SaleDialog", "备注："))
        self.oweEdit.setText(_translate("SaleDialog", "0"))
        self.label_7.setText(_translate("SaleDialog", "元"))
        self.payEdit.setText(_translate("SaleDialog", "0"))
        self.label_8.setText(_translate("SaleDialog", "元"))
        self.needPayEdit.setText(_translate("SaleDialog", "0"))
        self.label_9.setText(_translate("SaleDialog", "元"))


