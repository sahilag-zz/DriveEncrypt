# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload.ui'
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

class Ui_UploadDialog(object):
    def setupUi(self, UploadDialog):
        UploadDialog.setObjectName(_fromUtf8("UploadDialog"))
        UploadDialog.resize(435, 376)
        self.address = QtGui.QLineEdit(UploadDialog)
        self.address.setGeometry(QtCore.QRect(10, 50, 411, 21))
        self.address.setObjectName(_fromUtf8("address"))
        self.address.readOnly=True
        self.browseButton = QtGui.QPushButton(UploadDialog)
        self.browseButton.setGeometry(QtCore.QRect(330, 80, 75, 23))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.uploadButton = QtGui.QPushButton(UploadDialog)
        self.uploadButton.setGeometry(QtCore.QRect(150, 140, 101, 31))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))

        self.retranslateUi(UploadDialog)
        QtCore.QMetaObject.connectSlotsByName(UploadDialog)

    def retranslateUi(self, UploadDialog):
        UploadDialog.setWindowTitle(_translate("UploadDialog", "Upload", None))
        self.browseButton.setText(_translate("UploadDialog", "Browse", None))
        self.uploadButton.setText(_translate("UploadDialog", "Encrypted Upload", None))

