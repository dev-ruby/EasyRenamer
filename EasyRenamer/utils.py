import os

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QFrame, QTextEdit, QLabel, QCheckBox, QTextBrowser

from file_utils import Folder
from PyQt5.QtCore import Qt, QRect, QSize


class FrameUtil:
    @staticmethod
    def initFrame(base):
        FrameUtil.createExtensionFrame(base)

    @staticmethod
    def getFrameByPage(base: QWidget, page_number: int, old_page_number: int):
        if page_number == old_page_number:
            return
        if page_number == 0:
            base.frame_change_ext.show()
            print("show ext page")
        if old_page_number == 0:
            base.frame_change_ext.hide()
            print("hide ext page")

    @staticmethod
    def createExtensionFrame(base: QWidget):
        font = QFont()
        font.setPointSize(14)

        base.frame_change_ext = QFrame(base)
        base.frame_change_ext.setObjectName("frame_change_ext")
        base.frame_change_ext.setGeometry(QRect(200, 110, 700, 500))
        base.frame_change_ext.setFrameShape(QFrame.StyledPanel)
        base.frame_change_ext.setFrameShadow(QFrame.Raised)

        base.ext_frame_input_old_ext = QTextEdit(base.frame_change_ext)
        base.ext_frame_input_old_ext.setObjectName("ext_frame_input_old_ext")
        base.ext_frame_input_old_ext.setGeometry(QRect(350, 40, 150, 35))
        base.ext_frame_input_old_ext.setFont(font)

        base.ext_frame_label_old_ext = QLabel("바꿀 확장자", base.frame_change_ext)
        base.ext_frame_label_old_ext.setObjectName("label_old_ext")
        base.ext_frame_label_old_ext.setGeometry(QRect(210, 40, 111, 35))
        base.ext_frame_label_old_ext.setScaledContents(False)
        base.ext_frame_label_old_ext.setAlignment(Qt.AlignCenter)
        base.ext_frame_label_old_ext.setFont(font)

        base.ext_frame_input_new_ext = QTextEdit(base.frame_change_ext)
        base.ext_frame_input_new_ext.setObjectName("input_new_ext")
        base.ext_frame_input_new_ext.setGeometry(QRect(350, 90, 150, 35))
        base.ext_frame_input_new_ext.setFont(font)

        base.ext_frame_label_new_ext = QLabel("새 확장자", base.frame_change_ext)
        base.ext_frame_label_new_ext.setObjectName("label_new_ext")
        base.ext_frame_label_new_ext.setGeometry(QRect(220, 90, 111, 35))
        base.ext_frame_label_new_ext.setFont(font)
        base.ext_frame_label_new_ext.setScaledContents(False)
        base.ext_frame_label_new_ext.setAlignment(Qt.AlignCenter)

        base.ext_frame_text_browser_result = QTextBrowser(base.frame_change_ext)
        base.ext_frame_text_browser_result.setObjectName("textBrowser")
        base.ext_frame_text_browser_result.setGeometry(QRect(55, 180, 580, 320))
        base.ext_frame_text_browser_result.setFont(font)

        base.ext_frame_checkbox_all = QCheckBox("전체 파일", base.frame_change_ext)
        base.ext_frame_checkbox_all.setObjectName("input_all")
        base.ext_frame_checkbox_all.setEnabled(True)
        base.ext_frame_checkbox_all.setGeometry(QRect(520, 40, 100, 32))
        base.ext_frame_checkbox_all.setIconSize(QSize(32, 32))
        base.ext_frame_checkbox_all.setChecked(False)
        base.ext_frame_checkbox_all.setFont(font)
        base.ext_frame_checkbox_all.clicked[bool].connect(setExtFrameInput)


def find_files_with_ext(ext: str, files: list) -> list:
    files_with_ext = list()

    for file_name in files:
        if file_name.endswith(ext):
            files_with_ext.append(file_name)

    return files_with_ext


def getPathWarningBox() -> QMessageBox:
    message_box = QMessageBox()
    message_box.setWindowTitle("Error")
    message_box.setIcon(QMessageBox.Warning)
    message_box.setText("폴더의 경로가 올바르지 않습니다.")
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.setDefaultButton(QMessageBox.Ok)
    return message_box


def setFolderPath(base):
    path = base.input_path.text()
    is_folder_exist = os.path.isdir(path)
    if not is_folder_exist:
        message_box = base.getPathWarningBox()
        message_box.exec_()
    else:
        base.folder = Folder(path)


def searchFolderPath(base):
    path = QFileDialog.getExistingDirectory(base, "Select Folder")
    base.input_path.setText(path)


def setPage(base, index):
    old_page_number = base.current_page
    base.current_page = index
    FrameUtil.getFrameByPage(base, base.current_page, old_page_number)


def setExtFrameInput(base, checked):
    if checked:
        setExtFrameInputDisable(base)
    else:
        setExtFrameInputEnable(base)


def setExtFrameInputDisable(base):
    base.ext_frame_input_old_ext.setDisabled(True)
    base.ext_frame_label_old_ext.setDisabled(True)


def setExtFrameInputEnable(base):
    base.ext_frame_input_old_ext.setEnabled(True)
    base.ext_frame_label_old_ext.setEnabled(True)
