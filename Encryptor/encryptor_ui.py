# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryptor.ui'
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

class Ui_LoadPage(object):
    def setupUi(self, LoadPage):
        LoadPage.setObjectName(_fromUtf8("LoadPage"))
        LoadPage.resize(437, 374)
        self.uploadButton = QtGui.QPushButton(LoadPage)
        self.uploadButton.setGeometry(QtCore.QRect(170, 120, 91, 41))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.downloadButton = QtGui.QPushButton(LoadPage)
        self.downloadButton.setGeometry(QtCore.QRect(170, 180, 91, 41))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))

        self.retranslateUi(LoadPage)
        QtCore.QMetaObject.connectSlotsByName(LoadPage)

    def retranslateUi(self, LoadPage):
        LoadPage.setWindowTitle(_translate("LoadPage", "Welcome to Encryptor!!", None))
        self.uploadButton.setText(_translate("LoadPage", "Upload", None))
        self.downloadButton.setText(_translate("LoadPage", "Download", None))

