# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\barium133\Code\barium\lib\clients\gui\frequency_gui.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1130, 628)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(55, 20, 981, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setVerticalSpacing(24)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)
        self.GPIB21spinFreq = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB21spinFreq.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB21spinFreq.setFont(font)
        self.GPIB21spinFreq.setKeyboardTracking(False)
        self.GPIB21spinFreq.setSuffix(_fromUtf8(""))
        self.GPIB21spinFreq.setDecimals(0)
        self.GPIB21spinFreq.setMinimum(2000.0)
        self.GPIB21spinFreq.setMaximum(18000.0)
        self.GPIB21spinFreq.setObjectName(_fromUtf8("GPIB21spinFreq"))
        self.gridLayout_4.addWidget(self.GPIB21spinFreq, 2, 1, 1, 1)
        self.GPIB7spinFreq = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB7spinFreq.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB7spinFreq.setFont(font)
        self.GPIB7spinFreq.setKeyboardTracking(False)
        self.GPIB7spinFreq.setDecimals(1)
        self.GPIB7spinFreq.setMinimum(0.1)
        self.GPIB7spinFreq.setMaximum(2060.0)
        self.GPIB7spinFreq.setSingleStep(0.1)
        self.GPIB7spinFreq.setObjectName(_fromUtf8("GPIB7spinFreq"))
        self.gridLayout_4.addWidget(self.GPIB7spinFreq, 4, 1, 1, 1)
        self.GPIB21spinAmpDec = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB21spinAmpDec.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB21spinAmpDec.setFont(font)
        self.GPIB21spinAmpDec.setKeyboardTracking(False)
        self.GPIB21spinAmpDec.setDecimals(0)
        self.GPIB21spinAmpDec.setMinimum(-110.0)
        self.GPIB21spinAmpDec.setMaximum(0.0)
        self.GPIB21spinAmpDec.setSingleStep(10.0)
        self.GPIB21spinAmpDec.setProperty("value", -110.0)
        self.GPIB21spinAmpDec.setObjectName(_fromUtf8("GPIB21spinAmpDec"))
        self.gridLayout_4.addWidget(self.GPIB21spinAmpDec, 2, 3, 1, 1)
        self.GPIB19spinFreq = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB19spinFreq.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB19spinFreq.setSizeIncrement(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB19spinFreq.setFont(font)
        self.GPIB19spinFreq.setFrame(True)
        self.GPIB19spinFreq.setKeyboardTracking(False)
        self.GPIB19spinFreq.setDecimals(0)
        self.GPIB19spinFreq.setMinimum(2000.0)
        self.GPIB19spinFreq.setMaximum(18000.0)
        self.GPIB19spinFreq.setProperty("value", 2000.0)
        self.GPIB19spinFreq.setObjectName(_fromUtf8("GPIB19spinFreq"))
        self.gridLayout_4.addWidget(self.GPIB19spinFreq, 1, 1, 1, 1)
        self.GPIB6spinFreq = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB6spinFreq.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB6spinFreq.setFont(font)
        self.GPIB6spinFreq.setKeyboardTracking(False)
        self.GPIB6spinFreq.setDecimals(1)
        self.GPIB6spinFreq.setMinimum(0.1)
        self.GPIB6spinFreq.setMaximum(2060.0)
        self.GPIB6spinFreq.setSingleStep(0.1)
        self.GPIB6spinFreq.setObjectName(_fromUtf8("GPIB6spinFreq"))
        self.gridLayout_4.addWidget(self.GPIB6spinFreq, 3, 1, 1, 1)
        self.GPIB8spinAmp = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB8spinAmp.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB8spinAmp.setFont(font)
        self.GPIB8spinAmp.setKeyboardTracking(False)
        self.GPIB8spinAmp.setDecimals(0)
        self.GPIB8spinAmp.setMinimum(-143.0)
        self.GPIB8spinAmp.setMaximum(13.0)
        self.GPIB8spinAmp.setProperty("value", -143.0)
        self.GPIB8spinAmp.setObjectName(_fromUtf8("GPIB8spinAmp"))
        self.gridLayout_4.addWidget(self.GPIB8spinAmp, 5, 2, 1, 1)
        self.GPIB19spinAmpVer = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB19spinAmpVer.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB19spinAmpVer.setFont(font)
        self.GPIB19spinAmpVer.setKeyboardTracking(False)
        self.GPIB19spinAmpVer.setDecimals(0)
        self.GPIB19spinAmpVer.setMinimum(-10.0)
        self.GPIB19spinAmpVer.setMaximum(3.0)
        self.GPIB19spinAmpVer.setSingleStep(1.0)
        self.GPIB19spinAmpVer.setProperty("value", -10.0)
        self.GPIB19spinAmpVer.setObjectName(_fromUtf8("GPIB19spinAmpVer"))
        self.gridLayout_4.addWidget(self.GPIB19spinAmpVer, 1, 4, 1, 1)
        self.spinAmp4 = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.spinAmp4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinAmp4.setFont(font)
        self.spinAmp4.setKeyboardTracking(False)
        self.spinAmp4.setObjectName(_fromUtf8("spinAmp4"))
        self.gridLayout_4.addWidget(self.spinAmp4, 6, 2, 1, 1)
        self.GPIB7spinAmp = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB7spinAmp.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB7spinAmp.setFont(font)
        self.GPIB7spinAmp.setKeyboardTracking(False)
        self.GPIB7spinAmp.setDecimals(0)
        self.GPIB7spinAmp.setMinimum(-143.0)
        self.GPIB7spinAmp.setMaximum(13.0)
        self.GPIB7spinAmp.setProperty("value", -143.0)
        self.GPIB7spinAmp.setObjectName(_fromUtf8("GPIB7spinAmp"))
        self.gridLayout_4.addWidget(self.GPIB7spinAmp, 4, 2, 1, 1)
        self.GPIB21switch = QtGui.QPushButton(self.gridLayoutWidget)
        self.GPIB21switch.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB21switch.setAutoFillBackground(False)
        self.GPIB21switch.setCheckable(True)
        self.GPIB21switch.setChecked(False)
        self.GPIB21switch.setAutoRepeatInterval(100)
        self.GPIB21switch.setObjectName(_fromUtf8("GPIB21switch"))
        self.gridLayout_4.addWidget(self.GPIB21switch, 2, 5, 1, 1)
        self.GPIB21spinAmpVer = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB21spinAmpVer.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB21spinAmpVer.setFont(font)
        self.GPIB21spinAmpVer.setKeyboardTracking(False)
        self.GPIB21spinAmpVer.setDecimals(0)
        self.GPIB21spinAmpVer.setMinimum(-10.0)
        self.GPIB21spinAmpVer.setMaximum(3.0)
        self.GPIB21spinAmpVer.setProperty("value", -10.0)
        self.GPIB21spinAmpVer.setObjectName(_fromUtf8("GPIB21spinAmpVer"))
        self.gridLayout_4.addWidget(self.GPIB21spinAmpVer, 2, 4, 1, 1)
        self.GPIB6spinAmp = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB6spinAmp.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB6spinAmp.setFont(font)
        self.GPIB6spinAmp.setKeyboardTracking(False)
        self.GPIB6spinAmp.setDecimals(0)
        self.GPIB6spinAmp.setMinimum(-143.0)
        self.GPIB6spinAmp.setMaximum(13.0)
        self.GPIB6spinAmp.setProperty("value", -143.0)
        self.GPIB6spinAmp.setObjectName(_fromUtf8("GPIB6spinAmp"))
        self.gridLayout_4.addWidget(self.GPIB6spinAmp, 3, 2, 1, 1)
        self.GPIB19spinAmpDec = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB19spinAmpDec.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB19spinAmpDec.setFont(font)
        self.GPIB19spinAmpDec.setKeyboardTracking(False)
        self.GPIB19spinAmpDec.setDecimals(0)
        self.GPIB19spinAmpDec.setMinimum(-110.0)
        self.GPIB19spinAmpDec.setMaximum(0.0)
        self.GPIB19spinAmpDec.setSingleStep(10.0)
        self.GPIB19spinAmpDec.setProperty("value", -110.0)
        self.GPIB19spinAmpDec.setObjectName(_fromUtf8("GPIB19spinAmpDec"))
        self.gridLayout_4.addWidget(self.GPIB19spinAmpDec, 1, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 0, 3, 1, 1)
        self.GPIB8spinFreq = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.GPIB8spinFreq.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPIB8spinFreq.setFont(font)
        self.GPIB8spinFreq.setKeyboardTracking(False)
        self.GPIB8spinFreq.setDecimals(1)
        self.GPIB8spinFreq.setMinimum(0.1)
        self.GPIB8spinFreq.setMaximum(1030.0)
        self.GPIB8spinFreq.setSingleStep(0.1)
        self.GPIB8spinFreq.setObjectName(_fromUtf8("GPIB8spinFreq"))
        self.gridLayout_4.addWidget(self.GPIB8spinFreq, 5, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 0, 4, 1, 1)
        self.switch4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.switch4.setMinimumSize(QtCore.QSize(0, 30))
        self.switch4.setAutoFillBackground(False)
        self.switch4.setCheckable(True)
        self.switch4.setChecked(False)
        self.switch4.setAutoRepeatInterval(100)
        self.switch4.setObjectName(_fromUtf8("switch4"))
        self.gridLayout_4.addWidget(self.switch4, 6, 5, 1, 1)
        self.GPIB7switch = QtGui.QPushButton(self.gridLayoutWidget)
        self.GPIB7switch.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB7switch.setAutoFillBackground(False)
        self.GPIB7switch.setCheckable(True)
        self.GPIB7switch.setChecked(False)
        self.GPIB7switch.setAutoRepeatInterval(100)
        self.GPIB7switch.setObjectName(_fromUtf8("GPIB7switch"))
        self.gridLayout_4.addWidget(self.GPIB7switch, 4, 5, 1, 1)
        self.GPIB19switch = QtGui.QPushButton(self.gridLayoutWidget)
        self.GPIB19switch.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB19switch.setAutoFillBackground(True)
        self.GPIB19switch.setStyleSheet(_fromUtf8(""))
        self.GPIB19switch.setCheckable(True)
        self.GPIB19switch.setChecked(False)
        self.GPIB19switch.setAutoRepeatInterval(100)
        self.GPIB19switch.setDefault(False)
        self.GPIB19switch.setObjectName(_fromUtf8("GPIB19switch"))
        self.gridLayout_4.addWidget(self.GPIB19switch, 1, 5, 1, 1)
        self.GPIB6switch = QtGui.QPushButton(self.gridLayoutWidget)
        self.GPIB6switch.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB6switch.setAutoFillBackground(False)
        self.GPIB6switch.setCheckable(True)
        self.GPIB6switch.setChecked(False)
        self.GPIB6switch.setAutoRepeatInterval(100)
        self.GPIB6switch.setObjectName(_fromUtf8("GPIB6switch"))
        self.gridLayout_4.addWidget(self.GPIB6switch, 3, 5, 1, 1)
        self.GPIB8switch = QtGui.QPushButton(self.gridLayoutWidget)
        self.GPIB8switch.setMinimumSize(QtCore.QSize(0, 30))
        self.GPIB8switch.setAutoFillBackground(False)
        self.GPIB8switch.setCheckable(True)
        self.GPIB8switch.setChecked(False)
        self.GPIB8switch.setAutoRepeatInterval(100)
        self.GPIB8switch.setObjectName(_fromUtf8("GPIB8switch"))
        self.gridLayout_4.addWidget(self.GPIB8switch, 5, 5, 1, 1)
        self.spinFreq4 = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.spinFreq4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinFreq4.setFont(font)
        self.spinFreq4.setKeyboardTracking(False)
        self.spinFreq4.setObjectName(_fromUtf8("spinFreq4"))
        self.gridLayout_4.addWidget(self.spinFreq4, 6, 1, 1, 1)
        self.cool133 = QtGui.QPushButton(Form)
        self.cool133.setGeometry(QtCore.QRect(60, 490, 131, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cool133.setFont(font)
        self.cool133.setAutoFillBackground(False)
        self.cool133.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255)"))
        self.cool133.setObjectName(_fromUtf8("cool133"))
        self.heat135 = QtGui.QPushButton(Form)
        self.heat135.setGeometry(QtCore.QRect(260, 490, 131, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.heat135.setFont(font)
        self.heat135.setAutoFillBackground(False)
        self.heat135.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0)"))
        self.heat135.setObjectName(_fromUtf8("heat135"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Frequency Control", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">650-4</span></p></body></html>", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Oscillator</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">493-GPIB 19</span></p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">650-GPIB 7</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">493-GPIB 21</span></p></body></html>", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">650-GPIB 8</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">650-GPIB 6</span></p></body></html>", None))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Frequency(MHz)</span></p></body></html>", None))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Amplitude (dBm)</span></p></body></html>", None))
        self.GPIB21switch.setText(_translate("Form", "On/Off", None))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Amplitude (dBm)</span></p><p><span style=\" font-size:16pt;\">Output Range</span></p></body></html>", None))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Amplitude (dBm)</span></p><p><span style=\" font-size:16pt;\">Vernier</span></p></body></html>", None))
        self.switch4.setText(_translate("Form", "On/Off", None))
        self.GPIB7switch.setText(_translate("Form", "On/Off", None))
        self.GPIB19switch.setText(_translate("Form", "On/Off", None))
        self.GPIB6switch.setText(_translate("Form", "On/Off", None))
        self.GPIB8switch.setText(_translate("Form", "On/Off", None))
        self.cool133.setText(_translate("Form", "Cool Ba-133", None))
        self.heat135.setText(_translate("Form", "Heat Ba-135", None))

