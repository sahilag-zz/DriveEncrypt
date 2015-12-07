# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keygen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Password_Dialog(object):
    def setupUi(self, Password_Dialog):
        Password_Dialog.setObjectName(_fromUtf8("Password_Dialog"))
        Password_Dialog.resize(434, 374)
        self.lineEdit = QtGui.QLineEdit(Password_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 140, 341, 20))
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.setkeyButton = QtGui.QPushButton(Password_Dialog)
        self.setkeyButton.setGeometry(QtCore.QRect(160, 180, 111, 21))
        self.setkeyButton.setObjectName(_fromUtf8("setkeyButton"))

        self.retranslateUi(Password_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Password_Dialog)

    def retranslateUi(self, Password_Dialog):
        Password_Dialog.setWindowTitle(_translate("Password_Dialog", "Initialize Encryptor", None))
        self.lineEdit.setPlaceholderText(_translate("Password_Dialog", "Enter your key generation password here (8-16 characters)", None))
        self.setkeyButton.setText(_translate("Password_Dialog", "Generate Key", None))

