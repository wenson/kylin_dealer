# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lunzi/Projects/Python/Kylin_Dealer/ui/choose_cargo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChooseCargo(object):
    def setupUi(self, ChooseCargo):
        ChooseCargo.setObjectName("ChooseCargo")
        ChooseCargo.resize(753, 436)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChooseCargo)
        self.buttonBox.setGeometry(QtCore.QRect(520, 390, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.cargoTypeListTable = QtWidgets.QTableWidget(ChooseCargo)
        self.cargoTypeListTable.setGeometry(QtCore.QRect(10, 50, 441, 331))
        self.cargoTypeListTable.setObjectName("cargoTypeListTable")
        self.cargoTypeListTable.setColumnCount(5)
        self.cargoTypeListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoTypeListTable.setHorizontalHeaderItem(4, item)
        self.cargoListTable = QtWidgets.QTableWidget(ChooseCargo)
        self.cargoListTable.setGeometry(QtCore.QRect(460, 50, 281, 331))
        self.cargoListTable.setObjectName("cargoListTable")
        self.cargoListTable.setColumnCount(3)
        self.cargoListTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cargoListTable.setHorizontalHeaderItem(2, item)
        self.searchEdit = QtWidgets.QLineEdit(ChooseCargo)
        self.searchEdit.setGeometry(QtCore.QRect(50, 10, 191, 31))
        self.searchEdit.setObjectName("searchEdit")
        self.label = QtWidgets.QLabel(ChooseCargo)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ChooseCargo)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ChooseCargo)
        self.label_3.setGeometry(QtCore.QRect(640, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.countLabel = QtWidgets.QLabel(ChooseCargo)
        self.countLabel.setGeometry(QtCore.QRect(710, 20, 60, 16))
        self.countLabel.setObjectName("countLabel")
        self.cargoTypeNameLabel = QtWidgets.QLabel(ChooseCargo)
        self.cargoTypeNameLabel.setGeometry(QtCore.QRect(310, 20, 81, 16))
        self.cargoTypeNameLabel.setText("")
        self.cargoTypeNameLabel.setObjectName("cargoTypeNameLabel")
        self.label_4 = QtWidgets.QLabel(ChooseCargo)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 60, 16))
        self.label_4.setObjectName("label_4")
        self.dateLabel = QtWidgets.QLabel(ChooseCargo)
        self.dateLabel.setGeometry(QtCore.QRect(530, 20, 101, 16))
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")

        self.retranslateUi(ChooseCargo)
        self.buttonBox.accepted.connect(ChooseCargo.accept)
        self.buttonBox.rejected.connect(ChooseCargo.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseCargo)

    def retranslateUi(self, ChooseCargo):
        _translate = QtCore.QCoreApplication.translate
        ChooseCargo.setWindowTitle(_translate("ChooseCargo", "选择货物"))
        item = self.cargoTypeListTable.horizontalHeaderItem(0)
        item.setText(_translate("ChooseCargo", "货物种类"))
        item = self.cargoTypeListTable.horizontalHeaderItem(1)
        item.setText(_translate("ChooseCargo", "单位"))
        item = self.cargoTypeListTable.horizontalHeaderItem(2)
        item.setText(_translate("ChooseCargo", "库存"))
        item = self.cargoTypeListTable.horizontalHeaderItem(3)
        item.setText(_translate("ChooseCargo", "保质期"))
        item = self.cargoTypeListTable.horizontalHeaderItem(4)
        item.setText(_translate("ChooseCargo", "售价"))
        item = self.cargoListTable.horizontalHeaderItem(0)
        item.setText(_translate("ChooseCargo", "生产日期"))
        item = self.cargoListTable.horizontalHeaderItem(1)
        item.setText(_translate("ChooseCargo", "库存"))
        item = self.cargoListTable.horizontalHeaderItem(2)
        item.setText(_translate("ChooseCargo", "备注"))
        self.label.setText(_translate("ChooseCargo", "搜索："))
        self.label_2.setText(_translate("ChooseCargo", "已选择："))
        self.label_3.setText(_translate("ChooseCargo", "售出数量："))
        self.countLabel.setText(_translate("ChooseCargo", "0"))
        self.label_4.setText(_translate("ChooseCargo", "售出批次："))


