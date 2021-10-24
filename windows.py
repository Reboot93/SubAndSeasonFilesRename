# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(893, 446)
        Form.setMinimumSize(QtCore.QSize(893, 446))
        Form.setMaximumSize(QtCore.QSize(893, 446))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 896, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft Yi Baiti")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStatusTip("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 6, 581, 395))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 354, 31, 31))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/icon/icon/movie.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(50, 354, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setObjectName("label_14")
        self.label_number_season = QtWidgets.QLabel(self.groupBox_3)
        self.label_number_season.setGeometry(QtCore.QRect(110, 354, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_number_season.setFont(font)
        self.label_number_season.setTextFormat(QtCore.Qt.AutoText)
        self.label_number_season.setObjectName("label_number_season")
        self.pushButton_rename_del_all = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_rename_del_all.setGeometry(QtCore.QRect(540, 354, 31, 31))
        self.pushButton_rename_del_all.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rename_del_all.setIcon(icon1)
        self.pushButton_rename_del_all.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_rename_del_all.setObjectName("pushButton_rename_del_all")
        self.pushButton_rename_add = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_rename_add.setGeometry(QtCore.QRect(460, 354, 31, 31))
        self.pushButton_rename_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rename_add.setIcon(icon2)
        self.pushButton_rename_add.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_rename_add.setObjectName("pushButton_rename_add")
        self.pushButton_rename_del_one = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_rename_del_one.setGeometry(QtCore.QRect(500, 354, 31, 31))
        self.pushButton_rename_del_one.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rename_del_one.setIcon(icon3)
        self.pushButton_rename_del_one.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_rename_del_one.setObjectName("pushButton_rename_del_one")
        self.listWidget_season = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_season.setGeometry(QtCore.QRect(10, 24, 561, 321))
        self.listWidget_season.setObjectName("listWidget_season")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 10, 284, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.spinBox_season = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_season.setMinimum(0)
        self.spinBox_season.setObjectName("spinBox_season")
        self.horizontalLayout_3.addWidget(self.spinBox_season)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox_rename = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_rename.setCheckable(True)
        self.groupBox_rename.setChecked(False)
        self.groupBox_rename.setObjectName("groupBox_rename")
        self.label_17 = QtWidgets.QLabel(self.groupBox_rename)
        self.label_17.setGeometry(QtCore.QRect(30, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_rename = QtWidgets.QLineEdit(self.groupBox_rename)
        self.lineEdit_rename.setGeometry(QtCore.QRect(10, 80, 261, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit_rename.setFont(font)
        self.lineEdit_rename.setObjectName("lineEdit_rename")
        self.verticalLayout.addWidget(self.groupBox_rename)
        self.pushButton_rename_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("华康方圆体W7(P)")
        font.setPointSize(20)
        self.pushButton_rename_start.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rename_start.setIcon(icon4)
        self.pushButton_rename_start.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_rename_start.setObjectName("pushButton_rename_start")
        self.verticalLayout.addWidget(self.pushButton_rename_start)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 6, 431, 351))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_sub_up = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_up.setGeometry(QtCore.QRect(390, 110, 31, 31))
        self.pushButton_sub_up.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sub_up.setIcon(icon6)
        self.pushButton_sub_up.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_sub_up.setFlat(False)
        self.pushButton_sub_up.setObjectName("pushButton_sub_up")
        self.pushButton_sub_down = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_down.setGeometry(QtCore.QRect(390, 150, 31, 31))
        self.pushButton_sub_down.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sub_down.setIcon(icon7)
        self.pushButton_sub_down.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_sub_down.setFlat(False)
        self.pushButton_sub_down.setObjectName("pushButton_sub_down")
        self.pushButton_sub_del_one = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_del_one.setGeometry(QtCore.QRect(350, 310, 31, 31))
        self.pushButton_sub_del_one.setText("")
        self.pushButton_sub_del_one.setIcon(icon3)
        self.pushButton_sub_del_one.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_sub_del_one.setFlat(False)
        self.pushButton_sub_del_one.setObjectName("pushButton_sub_del_one")
        self.pushButton_sub_add = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_add.setGeometry(QtCore.QRect(310, 310, 31, 31))
        self.pushButton_sub_add.setText("")
        self.pushButton_sub_add.setIcon(icon2)
        self.pushButton_sub_add.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_sub_add.setFlat(False)
        self.pushButton_sub_add.setObjectName("pushButton_sub_add")
        self.pushButton_sub_del_all = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_del_all.setGeometry(QtCore.QRect(390, 310, 31, 31))
        self.pushButton_sub_del_all.setText("")
        self.pushButton_sub_del_all.setIcon(icon1)
        self.pushButton_sub_del_all.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_sub_del_all.setFlat(False)
        self.pushButton_sub_del_all.setObjectName("pushButton_sub_del_all")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_number_sub = QtWidgets.QLabel(self.groupBox)
        self.label_number_sub.setGeometry(QtCore.QRect(110, 310, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_number_sub.setFont(font)
        self.label_number_sub.setTextFormat(QtCore.Qt.AutoText)
        self.label_number_sub.setObjectName("label_number_sub")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icon/icon/subtitles.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.listWidget_sub = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_sub.setGeometry(QtCore.QRect(10, 20, 371, 281))
        self.listWidget_sub.setObjectName("listWidget_sub")
        self.pushButton_sub_flash = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub_flash.setGeometry(QtCore.QRect(390, 220, 31, 31))
        self.pushButton_sub_flash.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sub_flash.setIcon(icon8)
        self.pushButton_sub_flash.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_sub_flash.setDefault(False)
        self.pushButton_sub_flash.setFlat(False)
        self.pushButton_sub_flash.setObjectName("pushButton_sub_flash")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 6, 431, 351))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_movie_up = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_up.setGeometry(QtCore.QRect(390, 110, 31, 31))
        self.pushButton_movie_up.setText("")
        self.pushButton_movie_up.setIcon(icon6)
        self.pushButton_movie_up.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_movie_up.setFlat(False)
        self.pushButton_movie_up.setObjectName("pushButton_movie_up")
        self.pushButton_movie_down = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_down.setGeometry(QtCore.QRect(390, 150, 31, 31))
        self.pushButton_movie_down.setText("")
        self.pushButton_movie_down.setIcon(icon7)
        self.pushButton_movie_down.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_movie_down.setFlat(False)
        self.pushButton_movie_down.setObjectName("pushButton_movie_down")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(50, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_number_movie = QtWidgets.QLabel(self.groupBox_2)
        self.label_number_movie.setGeometry(QtCore.QRect(110, 310, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_number_movie.setFont(font)
        self.label_number_movie.setTextFormat(QtCore.Qt.AutoText)
        self.label_number_movie.setObjectName("label_number_movie")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icon/icon/movie.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_movie_del_one = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_del_one.setGeometry(QtCore.QRect(350, 310, 31, 31))
        self.pushButton_movie_del_one.setText("")
        self.pushButton_movie_del_one.setIcon(icon3)
        self.pushButton_movie_del_one.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_movie_del_one.setFlat(False)
        self.pushButton_movie_del_one.setObjectName("pushButton_movie_del_one")
        self.pushButton_movie_del_all = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_del_all.setGeometry(QtCore.QRect(390, 310, 31, 31))
        self.pushButton_movie_del_all.setText("")
        self.pushButton_movie_del_all.setIcon(icon1)
        self.pushButton_movie_del_all.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_movie_del_all.setFlat(False)
        self.pushButton_movie_del_all.setObjectName("pushButton_movie_del_all")
        self.pushButton_movie_add = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_add.setGeometry(QtCore.QRect(310, 310, 31, 31))
        self.pushButton_movie_add.setText("")
        self.pushButton_movie_add.setIcon(icon2)
        self.pushButton_movie_add.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_movie_add.setFlat(False)
        self.pushButton_movie_add.setObjectName("pushButton_movie_add")
        self.listWidget_movie = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_movie.setGeometry(QtCore.QRect(10, 20, 371, 281))
        self.listWidget_movie.setObjectName("listWidget_movie")
        self.pushButton_movie_flash = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_movie_flash.setGeometry(QtCore.QRect(390, 220, 31, 31))
        self.pushButton_movie_flash.setText("")
        self.pushButton_movie_flash.setIcon(icon8)
        self.pushButton_movie_flash.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_movie_flash.setFlat(False)
        self.pushButton_movie_flash.setObjectName("pushButton_movie_flash")
        self.pushButton_sub_start = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_sub_start.setGeometry(QtCore.QRect(720, 366, 161, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_sub_start.setFont(font)
        self.pushButton_sub_start.setIcon(icon4)
        self.pushButton_sub_start.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_sub_start.setObjectName("pushButton_sub_start")
        self.groupBox_sub_lan = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_sub_lan.setGeometry(QtCore.QRect(10, 360, 701, 41))
        self.groupBox_sub_lan.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox_sub_lan.setFlat(False)
        self.groupBox_sub_lan.setCheckable(True)
        self.groupBox_sub_lan.setChecked(False)
        self.groupBox_sub_lan.setObjectName("groupBox_sub_lan")
        self.label_18 = QtWidgets.QLabel(self.groupBox_sub_lan)
        self.label_18.setGeometry(QtCore.QRect(220, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setObjectName("label_18")
        self.radioButton_lan_eng = QtWidgets.QRadioButton(self.groupBox_sub_lan)
        self.radioButton_lan_eng.setGeometry(QtCore.QRect(480, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.radioButton_lan_eng.setFont(font)
        self.radioButton_lan_eng.setText("eng")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/eng.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_lan_eng.setIcon(icon9)
        self.radioButton_lan_eng.setIconSize(QtCore.QSize(23, 23))
        self.radioButton_lan_eng.setChecked(False)
        self.radioButton_lan_eng.setObjectName("radioButton_lan_eng")
        self.radioButton_lan_cht = QtWidgets.QRadioButton(self.groupBox_sub_lan)
        self.radioButton_lan_cht.setGeometry(QtCore.QRect(390, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.radioButton_lan_cht.setFont(font)
        self.radioButton_lan_cht.setText("cht")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icon/cht.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_lan_cht.setIcon(icon10)
        self.radioButton_lan_cht.setIconSize(QtCore.QSize(23, 23))
        self.radioButton_lan_cht.setChecked(False)
        self.radioButton_lan_cht.setObjectName("radioButton_lan_cht")
        self.radioButton_lan_chs = QtWidgets.QRadioButton(self.groupBox_sub_lan)
        self.radioButton_lan_chs.setGeometry(QtCore.QRect(300, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.radioButton_lan_chs.setFont(font)
        self.radioButton_lan_chs.setToolTip("")
        self.radioButton_lan_chs.setText("chs")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icon/chs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_lan_chs.setIcon(icon11)
        self.radioButton_lan_chs.setIconSize(QtCore.QSize(23, 23))
        self.radioButton_lan_chs.setChecked(True)
        self.radioButton_lan_chs.setObjectName("radioButton_lan_chs")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/subtitles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon12, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(670, 350, 51, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icon/icon/Python.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(530, 350, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(730, 350, 151, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(370, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(380, 20, 121, 121))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/icon/icon/logo.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(340, 240, 291, 41))
        font = QtGui.QFont()
        font.setFamily("华康少女文字W5-A")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(160, 230, 101, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/icon/github.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(280, 290, 431, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/icon/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon13, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "剧集与字幕批量改名"))
        self.groupBox_3.setTitle(_translate("Form", "剧集文件"))
        self.label_14.setText(_translate("Form", "文件数量："))
        self.label_number_season.setText(_translate("Form", "0"))
        self.pushButton_rename_del_all.setToolTip(_translate("Form", "清除全部"))
        self.pushButton_rename_add.setToolTip(_translate("Form", "添加"))
        self.pushButton_rename_del_one.setToolTip(_translate("Form", "清除选中"))
        self.label_16.setToolTip(_translate("Form", "修改为 [SxxExx] 格式"))
        self.label_16.setText(_translate("Form", "      第"))
        self.spinBox_season.setToolTip(_translate("Form", "修改为 [SxxExx] 格式"))
        self.label_15.setToolTip(_translate("Form", "修改为 [SxxExx] 格式"))
        self.label_15.setText(_translate("Form", "     季"))
        self.groupBox_rename.setTitle(_translate("Form", "重命名剧集"))
        self.label_17.setText(_translate("Form", "重命名为："))
        self.lineEdit_rename.setPlaceholderText(_translate("Form", "集数信息将会以 [SxxExx] 格式添加在末尾"))
        self.pushButton_rename_start.setToolTip(_translate("Form", "开始修改"))
        self.pushButton_rename_start.setText(_translate("Form", "批量修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "剧集文件批量重命名"))
        self.groupBox.setTitle(_translate("Form", "字幕文件"))
        self.pushButton_sub_up.setToolTip(_translate("Form", "上移一位"))
        self.pushButton_sub_down.setToolTip(_translate("Form", "下移一位"))
        self.pushButton_sub_del_one.setToolTip(_translate("Form", "清除选中"))
        self.pushButton_sub_add.setToolTip(_translate("Form", "添加"))
        self.pushButton_sub_del_all.setToolTip(_translate("Form", "清除全部"))
        self.label.setText(_translate("Form", "文件数量："))
        self.label_number_sub.setText(_translate("Form", "0"))
        self.pushButton_sub_flash.setToolTip(_translate("Form", "重新排序"))
        self.groupBox_2.setTitle(_translate("Form", "视频文件"))
        self.pushButton_movie_up.setToolTip(_translate("Form", "上移一位"))
        self.pushButton_movie_down.setToolTip(_translate("Form", "下移一位"))
        self.label_2.setText(_translate("Form", "文件数量："))
        self.label_number_movie.setText(_translate("Form", "0"))
        self.pushButton_movie_del_one.setToolTip(_translate("Form", "清除选中"))
        self.pushButton_movie_del_all.setToolTip(_translate("Form", "清除全部"))
        self.pushButton_movie_add.setToolTip(_translate("Form", "添加"))
        self.pushButton_movie_flash.setToolTip(_translate("Form", "重新排序"))
        self.pushButton_sub_start.setToolTip(_translate("Form", "开始修改"))
        self.pushButton_sub_start.setText(_translate("Form", "批量修改"))
        self.groupBox_sub_lan.setTitle(_translate("Form", "添加字幕语言标注"))
        self.label_18.setText(_translate("Form", "字幕语言"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "字幕文件批量重命名"))
        self.label_8.setText(_translate("Form", "Power by"))
        self.label_9.setText(_translate("Form", "Python PyQt5"))
        self.label_10.setText(_translate("Form", "Reboot93"))
        self.label_11.setText(_translate("Form", "版本:   V1.0"))
        self.label_3.setText(_translate("Form", "我想要星星⭐⭐，请点我"))
        self.label_19.setText(_translate("Form", "https://github.com/Reboot93/SubAndSeasonFilesRename"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "关于"))


import qt_rc
