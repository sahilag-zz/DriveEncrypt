# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
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

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName(_fromUtf8("DownloadDialog"))
        DownloadDialog.resize(435, 374)
        self.scrollArea = QtGui.QScrollArea(DownloadDialog)
        self.scrollArea.setGeometry(QtCore.QRect(40, 30, 221, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 309))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.fileList = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.fileList.setGeometry(QtCore.QRect(0, 0, 221, 311))
        self.fileList.setObjectName(_fromUtf8("fileList"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.downloadButton = QtGui.QPushButton(DownloadDialog)
        self.downloadButton.setGeometry(QtCore.QRect(300, 290, 101, 41))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.address = QtGui.QLineEdit(DownloadDialog)
        self.address.setGeometry(QtCore.QRect(280, 60, 141, 20))
        self.address.setObjectName(_fromUtf8("address"))
        self.browseButton = QtGui.QPushButton(DownloadDialog)
        self.browseButton.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))

        self.retranslateUi(DownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Download", None))
        self.downloadButton.setText(_translate("DownloadDialog", "Download", None))
        self.browseButton.setText(_translate("DownloadDialog", "Browse", None))

