import sys, time, _thread, os, subprocess, shutil
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from windows import Ui_Form


class MainWindow(QWidget, Ui_Form):
    # 定义点击信号
    chooseSignal = pyqtSignal(str)


    work_dir_season = ''

    def __init__(self, parent=None):
        global control_data, status_flag
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowTitle('片库管理助手 V1.0')
        # ==/ Icon设置 /===
        # self.setWindowIcon(QIcon('icon/256x256.ico'))
        # ==/ 按键信号设置 /================
        self.pushButton_rename_add.clicked.connect(lambda: self.season_files_add())
        self.pushButton_rename_del_one.clicked.connect(lambda: self.season_files_del_one())
        self.pushButton_rename_del_all.clicked.connect(lambda: self.season_files_del_all())
        self.pushButton_sub_add.clicked.connect(lambda: self.sub_files_add())
        self.pushButton_sub_del_one.clicked.connect(lambda: self.sub_files_del_one())
        self.pushButton_sub_del_all.clicked.connect(lambda: self.sub_files_del_all())
        self.pushButton_sub_up.clicked.connect(lambda: self.sub_list_up())
        self.pushButton_sub_down.clicked.connect(lambda: self.sub_list_down())
        # self.bt_start.clicked.connect(lambda: self.start())
        # ==/ 界面初始化 /==========
        # 界面更新
        #_thread.start_new_thread(lambda: self.flash(), ())

    def season_files_add(self):
        files = QFileDialog.getOpenFileNames(self, '选择需要修改的文件')
        if files[0] != []:
            files = files[0]
            self.work_dir_season = (files[0])[:files[0].rfind('/')+1]
            print(self.work_dir_season)
            for file in files:
                self.listWidget_season.addItem(file[file.rfind('/')+1:])
            self.flash()
            #self.label_number_season.setText(str(self.listWidget_season.count()))

    def season_files_del_one(self):
        try:
            file = self.listWidget_season.currentItem().text()
            self.listWidget_season.takeItem(self.listWidget_season.currentRow())

            #获取列表中的所有数据
            #count = self.listWidget_season.count()
            #for i in range(count):
            #    print(self.listWidget_season.item(i).text())
        except:
            print('error')
        self.flash()

    def season_files_del_all(self):
        try:
            self.listWidget_season.clear()
        except:
            print('error')
        self.flash()

    def sub_files_add(self):
        files = QFileDialog.getOpenFileNames(self, '选择需要修改的字幕文件')
        if files[0] != []:
            files = files[0]
            self.work_dir_season = (files[0])[:files[0].rfind('/') + 1]
            print(self.work_dir_season)
            for file in files:
                self.listWidget_sub.addItem(file[file.rfind('/') + 1:])
            self.flash()

    def sub_files_del_one(self):
        try:
            file = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(self.listWidget_sub.currentRow())
            #获取列表中的所有数据
            #count = self.listWidget_season.count()
            #for i in range(count):
            #    print(self.listWidget_season.item(i).text())
        except:
            print('error')
        self.flash()

    def sub_files_del_all(self):
        try:
            self.listWidget_sub.clear()
        except:
            print('error')
        self.flash()

    def sub_list_up(self):
        try:
            count = self.listWidget_sub.currentRow()
            uptext = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(count)
            self.listWidget_sub.insertItem(count-1, uptext)
            if self.listWidget_sub.currentRow() > 0:
                self.listWidget_sub.setCurrentRow(count-1)
            del count, uptext
        except:
            print('error')
        self.flash()

    def sub_list_down(self):
        try:
            count = self.listWidget_sub.currentRow()
            downtext = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(count)
            self.listWidget_sub.insertItem(count+1, downtext)
            if self.listWidget_sub.currentRow() < self.listWidget_sub.count():
                self.listWidget_sub.setCurrentRow(count+1)
        except:
            print('error')
        self.flash()

    def flash(self):
        self.label_number_season.setText(str(self.listWidget_season.count()))
        self.label_number_sub.setText(str(self.listWidget_sub.count()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MainWindow()
    ma.show()
    sys.exit(app.exec_())
