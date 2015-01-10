# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/about_dialog.ui'
#
# Created: Sun Jan  4 14:07:42 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(472, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/freeiconmaker_2 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setAutoFillBackground(False)
        AboutDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(AboutDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_widget = QtGui.QTabWidget(AboutDialog)
        self.tab_widget.setTabPosition(QtGui.QTabWidget.North)
        self.tab_widget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widge_about = QtGui.QWidget()
        self.tab_widge_about.setObjectName("tab_widge_about")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_widge_about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(self.tab_widge_about)
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.tab_widget.addTab(self.tab_widge_about, "")
        self.horizontalLayout.addWidget(self.tab_widget)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Pynocchio Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/freeiconmaker_2 1.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:12pt; font-weight:600; color:#c05800;\">Pynocchio</span><span style=\" font-family:\'DejaVu Sans\'; font-size:12pt; font-weight:600;\"> Comic Reader - Beta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:11pt; font-weight:600; color:#c05800;\">Pynocchio</span><span style=\" font-family:\'DejaVu Sans\'; font-size:10pt;\"> is an image viewer specifically designed to handle comic books.  </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:10pt;\">It reads ZIP, RAR and TAR archives, as well as plain image files.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Pynocchio Comic Reader is licensed under the GNU General Public License.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\';\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Copyright © 2014 </span><a href=\"michellstut@gmail.com\"><span style=\" font-family:\'DejaVu Sans\'; text-decoration: underline; color:#539fa3;\">Michell Stuttgart Faria</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Pynocchio use </span><a href=\"http://freeiconmaker.com/\"><span style=\" font-family:\'DejaVu Sans\'; text-decoration: underline; color:#0057ae;\">FREE Icon Maker</span></a><span style=\" font-family:\'DejaVu Sans\';\"> to build icon set.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Icons pack by </span><a href=\"https://www.iconfinder.com/iconsets/streamline-icon-set-free-pack\"><span style=\" font-family:\'DejaVu Sans\'; text-decoration: underline; color:#0057ae;\">Streamline icon set free pack.</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/MStuttgart\"><span style=\" font-family:\'DejaVu Sans\'; text-decoration: underline; color:#539fa3;\">Github</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_widge_about), QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))

import main_window_rc