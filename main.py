import sys, time, _thread, os, threading, re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from windows import Ui_Form


class MainWindow(QWidget, Ui_Form):
    # 定义点击信号
    chooseSignal = pyqtSignal(str)
    work_dir_season = ''
    work_dir_sub = ''
    work_dir_movie = ''
    sub_lan = '.chs'

    def __init__(self, parent=None):
        # global
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # ==/ 按键信号设置 /================
        # 剧集界面按键
        self.pushButton_rename_add.clicked.connect(lambda: self.season_files_add())
        self.pushButton_rename_del_one.clicked.connect(lambda: self.season_files_del_one())
        self.pushButton_rename_del_all.clicked.connect(lambda: self.season_files_del_all())
        self.pushButton_rename_start.clicked.connect(lambda: self.season_run())
        # 字幕文件界面按键
        self.pushButton_sub_add.clicked.connect(lambda: self.sub_files_add())
        self.pushButton_sub_del_one.clicked.connect(lambda: self.sub_files_del_one())
        self.pushButton_sub_del_all.clicked.connect(lambda: self.sub_files_del_all())
        self.pushButton_sub_up.clicked.connect(lambda: self.sub_list_up())
        self.pushButton_sub_down.clicked.connect(lambda: self.sub_list_down())
        self.pushButton_sub_flash.clicked.connect(lambda: self.sub_list_flash())
        # 视频界面按键
        self.pushButton_movie_add.clicked.connect(lambda: self.movie_files_add())
        self.pushButton_movie_del_one.clicked.connect(lambda: self.movie_files_del_one())
        self.pushButton_movie_del_all.clicked.connect(lambda: self.movie_files_del_all())
        self.pushButton_movie_up.clicked.connect(lambda: self.movie_list_up())
        self.pushButton_movie_down.clicked.connect(lambda: self.movie_list_down())
        self.pushButton_movie_flash.clicked.connect(lambda: self.movie_list_flash())
        # 字幕语言按键
        self.radioButton_lan_chs.clicked.connect(lambda: self.set_sub_lan('.chs'))
        self.radioButton_lan_cht.clicked.connect(lambda: self.set_sub_lan('.cht'))
        self.radioButton_lan_eng.clicked.connect(lambda: self.set_sub_lan('.eng'))
        self.pushButton_sub_start.clicked.connect(lambda: self.sub_run())

        # ==/ 界面初始化 /==========

        # 界面更新
        # _thread.start_new_thread(lambda: self.flash(), ())

    def season_files_add(self):
        files = QFileDialog.getOpenFileNames(self, '选择需要修改的文件')
        if files[0] != []:
            files = files[0]
            if (files[0])[:files[0].rfind('/') + 1] != self.work_dir_season and self.work_dir_season != '':
                QMessageBox.warning(self, '    添加文件不符合规则', '添加的文件与已有文件不在同一文件夹，V1.0版本暂不支持同时修改，请分批修改，或等待随缘更新')
            else:
                self.work_dir_season = (files[0])[:files[0].rfind('/') + 1]
                for file in files:
                    self.listWidget_season.addItem(file[file.rfind('/') + 1:])
                self.flash()
                # self.label_number_season.setText(str(self.listWidget_season.count()))

    def season_files_del_one(self):
        try:
            file = self.listWidget_season.currentItem().text()
            self.listWidget_season.takeItem(self.listWidget_season.currentRow())
        except:
            print('error')
        self.flash()

    def season_files_del_all(self):
        try:
            self.listWidget_season.clear()
        except:
            print('error')
        self.work_dir_season = ''
        self.flash()

    def sub_files_add(self):
        files = QFileDialog.getOpenFileNames(self, '选择需要修改的字幕文件')
        if files[0] != []:
            files = files[0]
            if (files[0])[:files[0].rfind('/') + 1] != self.work_dir_sub and self.work_dir_sub != '':
                QMessageBox.warning(self, '    添加文件不符合规则', '添加的文件与已有文件不在同一文件夹，V1.0版本暂不支持同时修改，请分批修改，或等待随缘更新')
            else:
                self.work_dir_sub = (files[0])[:files[0].rfind('/') + 1]
                for file in files:
                    self.listWidget_sub.addItem(file[file.rfind('/') + 1:])
                self.flash()

    def sub_files_del_one(self):
        try:
            file = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(self.listWidget_sub.currentRow())
        except:
            print('error')
        self.flash()

    def sub_files_del_all(self):
        try:
            self.listWidget_sub.clear()
        except:
            print('error')
        self.work_dir_sub = ''
        self.flash()

    def sub_list_up(self):
        try:
            count = self.listWidget_sub.currentRow()
            uptext = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(count)
            self.listWidget_sub.insertItem(count - 1, uptext)
            if self.listWidget_sub.currentRow() > 0:
                self.listWidget_sub.setCurrentRow(count - 1)
            del count, uptext
        except:
            print('error')
        self.flash()

    def sub_list_down(self):
        try:
            count = self.listWidget_sub.currentRow()
            downtext = self.listWidget_sub.currentItem().text()
            self.listWidget_sub.takeItem(count)
            self.listWidget_sub.insertItem(count + 1, downtext)
            if self.listWidget_sub.currentRow() < self.listWidget_sub.count():
                self.listWidget_sub.setCurrentRow(count + 1)
        except:
            print('error')
        self.flash()

    def sub_list_flash(self):
        self.listWidget_sub.sortItems()
        self.flash()

    def movie_files_add(self):
        files = QFileDialog.getOpenFileNames(self, '选择需要修改的字幕文件')
        if files[0] != []:
            files = files[0]
            if (files[0])[:files[0].rfind('/') + 1] != self.work_dir_movie and self.work_dir_movie != '':
                QMessageBox.warning(self, '    添加文件不符合规则', '添加的文件与已有文件不在同一文件夹，V1.0版本暂不支持同时修改，请分批修改，或等待随缘更新')
            else:
                self.work_dir_movie = (files[0])[:files[0].rfind('/') + 1]
                for file in files:
                    self.listWidget_movie.addItem(file[file.rfind('/') + 1:])
                self.flash()

    def movie_files_del_one(self):
        try:
            file = self.listWidget_movie.currentItem().text()
            self.listWidget_movie.takeItem(self.listWidget_movie.currentRow())
        except:
            print('error')
        self.flash()

    def movie_files_del_all(self):
        try:
            self.listWidget_movie.clear()
        except:
            print('error')
        self.work_dir_movie = ''
        self.flash()

    def movie_list_up(self):
        try:
            count = self.listWidget_movie.currentRow()
            uptext = self.listWidget_movie.currentItem().text()
            self.listWidget_movie.takeItem(count)
            self.listWidget_movie.insertItem(count - 1, uptext)
            if self.listWidget_movie.currentRow() > 0:
                self.listWidget_movie.setCurrentRow(count - 1)
            del count, uptext
        except:
            print('error')
        self.flash()

    def movie_list_down(self):
        try:
            count = self.listWidget_movie.currentRow()
            downtext = self.listWidget_movie.currentItem().text()
            self.listWidget_movie.takeItem(count)
            self.listWidget_movie.insertItem(count + 1, downtext)
            if self.listWidget_movie.currentRow() < self.listWidget_movie.count():
                self.listWidget_movie.setCurrentRow(count + 1)
        except:
            print('error')
        self.flash()

    def movie_list_flash(self):
        self.listWidget_movie.sortItems()
        self.flash()

    def set_sub_lan(self, msg):
        self.sub_lan = msg

    def sub_run(self):
        self.pushButton_sub_start.setEnabled(False)
        if self.listWidget_sub.count() != self.listWidget_movie.count():
            QMessageBox.warning(self, '错误', '输入的字幕数量与视频数量不符，请检查后继续。')
        elif self.listWidget_sub.count() == 0 or self.listWidget_movie.count() == 0:  # 在无选中文件时按下运行不做反应
            self.pushButton_sub_start.setEnabled(True)
        else:
            count = self.listWidget_sub.count()
            i = 0
            list = ''
            if not self.groupBox_sub_lan.isChecked():
                sub_lan = ''
            else:
                sub_lan = self.sub_lan
            for number in range(count):
                filename = self.listWidget_sub.item(number).text()
                newname = (self.listWidget_movie.item(i).text())[
                          0:(self.listWidget_movie.item(i).text()).rfind('.')] + sub_lan + filename[
                                                                                           filename.rfind(
                                                                                               '.'):]
                i = i + 1
                list = list + newname + '\n'
            reply = QMessageBox.question(self, '请确认是否修改', '以下是修改后的字幕文件名,修改后无法回退:\n\n' + list,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                i = 0
                try:
                    for number in range(count):
                        filename = self.listWidget_sub.item(number).text()
                        os.rename(self.work_dir_sub + filename,
                                  self.work_dir_sub + (self.listWidget_movie.item(i).text())[
                                                      0:(self.listWidget_movie.item(i).text()).rfind(
                                                          '.')] + sub_lan + filename[
                                                                            filename.rfind(
                                                                                '.'):])
                        i = i + 1
                    QMessageBox.information(self, '修改成功', '字幕文件名修改成功，请继续操作或关闭本程序')
                    self.listWidget_sub.clear()
                    self.listWidget_movie.clear()
                    self.flash()
                except:
                    QMessageBox.warning(self, '修改失败', '修改字幕文件名失败')
            if reply == QMessageBox.No:
                pass
            del i, list, filename, newname
        self.pushButton_sub_start.setEnabled(True)

    def season_run(self):
        self.pushButton_rename_start.setEnabled(False)
        count = self.listWidget_season.count()
        if count > 0:
            list = ''
            for number in range(count):
                filename = self.listWidget_season.item(number).text()
                type1 = re.search(r'EP[0-9]+', filename)
                type2 = re.search(r'\[[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?\]', filename)
                type3 = re.search(r'【[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?】', filename)
                season = self.spinBox_season.text()
                if not self.groupBox_rename.isChecked():
                    if type1 != None:
                        newname = filename[:(type1.span())[0]] + 'S' + season + 'E' + filename[
                                                                                      (type1.span(0))[
                                                                                          0] + 1:]
                        list = list + newname + '\n'
                    elif type2 != None:
                        newname = filename[:(type2.span())[0] + 1] + 'S' + season + 'E' + filename[(
                                                                                                       type2.span(
                                                                                                           0))[
                                                                                                       0] + 1:]
                        list = list + newname + '\n'
                    elif type3 != None:
                        newname = filename[:(type3.span())[0] + 1] + 'S' + season + 'E' + filename[
                                                                                          (type3.span(0))[0] + 1:]
                        list = list + newname + '\n'
                    else:
                        newname = '%s --- error' & filename
                        list = list + newname + '\n'
                else:
                    if self.lineEdit_rename.text() == '':
                        QMessageBox.warning(self, '错误', '没有指定重命名后的标题！')
                        self.pushButton_rename_start.setEnabled(True)
                        return
                    if type1 != None:
                        newname = self.lineEdit_rename.text() + '[S' + season + 'E' + (type1.group())[
                                                                                      2:] + ']' + filename[(
                                                                                                               filename.rfind(
                                                                                                                   '.')):]
                        list = list + newname + '\n'
                    elif type2 != None:
                        newname = self.lineEdit_rename.text() + '[S' + season + 'E' + (type2.group()[1:]) + filename[(
                                                                                                                         filename.rfind(
                                                                                                                             '.')):]
                        list = list + newname + '\n'
                    elif type3 != None:
                        newname = self.lineEdit_rename.text() + '[S' + season + 'E' + (type3.group())[
                                                                                      1:-1] + ']' + filename[(
                                                                                                                 filename.rfind(
                                                                                                                     '.')):]
                        list = list + newname + '\n'
                    else:
                        newname = filename + ' --- error'
                        list = list + newname + '\n'
            reply = QMessageBox.question(self, '请确认是否修改', '以下是修改后的剧集文件名,修改后无法回退:\n\n' + list,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    for number in range(count):
                        filename = self.listWidget_season.item(number).text()
                        type1 = re.search(r'EP[0-9]+', filename)
                        type2 = re.search(r'\[[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?\]', filename)
                        type3 = re.search(r'【[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?】', filename)
                        season = self.spinBox_season.text()
                        if not self.groupBox_rename.isChecked():
                            if type1 != None:
                                newname = self.work_dir_season + filename[
                                                                 :(type1.span())[0]] + 'S' + season + 'E' + filename[
                                                                                                            (type1.span(
                                                                                                                0))[
                                                                                                                0] + 1:]
                                os.rename(self.work_dir_season + filename, newname)
                            elif type2 != None:
                                newname = self.work_dir_season + filename[
                                                                 :(type2.span())[
                                                                      0] + 1] + 'S' + season + 'E' + filename[(
                                                                                                                  type2.span(
                                                                                                                      0))[
                                                                                                                  0] + 1:]

                                os.rename(self.work_dir_season + filename, newname)
                            elif type3 != None:
                                newname = self.work_dir_season + filename[
                                                                 :(type3.span())[
                                                                      0] + 1] + 'S' + season + 'E' + filename[
                                                                                                     (type3.span(
                                                                                                         0))[
                                                                                                         0] + 1:]
                                os.rename(self.work_dir_season + filename, newname)
                            else:
                                print('error')
                        else:
                            if type1 != None:
                                newname = self.work_dir_season + self.lineEdit_rename.text() + '[S' + season + 'E' + (
                                                                                                                         type1.group())[
                                                                                                                     2:] + ']' + filename[
                                                                                                                                 (
                                                                                                                                     filename.rfind(
                                                                                                                                         '.')):]
                                os.rename(self.work_dir_season + filename, newname)
                            elif type2 != None:
                                newname = self.work_dir_season + self.lineEdit_rename.text() + '[S' + season + 'E' + (
                                type2.group()[1:]) + filename[(filename.rfind('.')):]
                                os.rename(self.work_dir_season + filename, newname)
                            elif type3 != None:
                                newname = self.work_dir_season + self.lineEdit_rename.text() + '[S' + season + 'E' + (
                                                                                                                         type3.group())[
                                                                                                                     1:-1] + ']' + filename[
                                                                                                                                   (
                                                                                                                                       filename.rfind(
                                                                                                                                           '.')):]
                                os.rename(self.work_dir_season + filename, newname)
                            else:
                                newname = '%s --- error' & filename
                                list = list + newname + '\n'
                    QMessageBox.information(self, '修改完成', '修改完成，请继续修改或关闭本窗口')
                    self.listWidget_season.clear()
                    self.flash()
                except:
                    pass
            if reply == QMessageBox.No:
                pass
            del newname, list
        self.pushButton_rename_start.setEnabled(True)

    def flash(self):
        self.label_number_season.setText(str(self.listWidget_season.count()))
        self.label_number_sub.setText(str(self.listWidget_sub.count()))
        self.label_number_movie.setText(str(self.listWidget_movie.count()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MainWindow()
    ma.show()
    sys.exit(app.exec_())
