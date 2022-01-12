from typing import List

from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QMessageBox,
    QFrame,
    QTextEdit,
    QLabel,
    QCheckBox,
    QTextBrowser,
    QComboBox,
    QLineEdit,
)

import ui_event
from file_utils import Sort
from file_utils import SortType


class FrameUtil:
    @staticmethod
    def initFrame(base):
        FrameUtil.createExtensionFrame(base)

    @staticmethod
    def getFrameByPage(base, page_number: int, old_page_number: int):
        if page_number == old_page_number:
            return
        if page_number == 0:
            base.frame_change_ext.show()

        if old_page_number == 0:
            base.frame_change_ext.hide()

    @staticmethod
    def createExtensionFrame(base):
        font = QFont()
        font.setPointSize(14)

        base.frame_change_ext = QFrame(base)
        base.frame_change_ext.setObjectName("frame_change_ext")
        base.frame_change_ext.setGeometry(QRect(200, 110, 700, 600))
        base.frame_change_ext.setFrameShape(QFrame.StyledPanel)
        base.frame_change_ext.setFrameShadow(QFrame.Raised)

        base.ext_frame_input_old_ext = QLineEdit(base.frame_change_ext)
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
        base.ext_frame_text_browser_result.setGeometry(QRect(55, 240, 580, 320))
        base.ext_frame_text_browser_result.setFont(font)

        base.ext_frame_checkbox_all = QCheckBox("전체 파일", base.frame_change_ext)
        base.ext_frame_checkbox_all.setObjectName("input_all")
        base.ext_frame_checkbox_all.setEnabled(True)
        base.ext_frame_checkbox_all.setGeometry(QRect(520, 40, 100, 32))
        base.ext_frame_checkbox_all.setIconSize(QSize(32, 32))
        base.ext_frame_checkbox_all.setChecked(False)
        base.ext_frame_checkbox_all.setFont(font)
        base.ext_frame_checkbox_all.clicked[bool].connect(
            lambda check: ui_event.eventSetExtFrameInput(base, check)
        )

        base.ext_frame_combobox_sort = QComboBox(base.frame_change_ext)
        base.ext_frame_combobox_sort.setObjectName("input_sort")
        base.ext_frame_combobox_sort.setGeometry(QRect(240, 170, 350, 35))
        base.ext_frame_combobox_sort.setFont(font)
        base.ext_frame_combobox_sort.addItems(["이름", "파일 크기", "생성 날짜"])
        base.ext_frame_combobox_sort.activated[int].connect(
            lambda index: ui_event.eventSetSortType(base, index)
        )
        base.ext_frame_combobox_sort.activated[int].connect(
            lambda index: ui_event.eventUpdateExtFrameText(base)
        )

        base.ext_frame_label_path = QLabel("정렬 방법", base.frame_change_ext)
        base.ext_frame_label_path.setObjectName("label_path")
        base.ext_frame_label_path.setGeometry(QRect(120, 170, 81, 35))
        base.ext_frame_label_path.setFont(font)
        base.ext_frame_label_path.setScaledContents(False)
        base.ext_frame_label_path.setAlignment(Qt.AlignCenter)


def find_files_with_ext(ext: str, files: List[str]) -> List[str]:
    files_with_ext = list()

    ext = "." + ext

    for file_name in files:
        if file_name.endswith(ext):
            files_with_ext.append(file_name)

    return files_with_ext


def getErrorMessageBox(base, error_message) -> QMessageBox:
    message_box = QMessageBox(base)
    message_box.setWindowTitle("Error")
    message_box.setIcon(QMessageBox.Warning)
    message_box.setText(error_message)
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.setDefaultButton(QMessageBox.Ok)

    return message_box


def sortFiles(base, files: List[str]) -> List[str]:
    if base.sort_type == SortType.NAME:
        return Sort.sort_file_name(files)
    elif base.sort_type == SortType.SIZE:
        return Sort.sort_file_size(files)
    elif base.sort_type == SortType.TIME:
        return Sort.sort_file_time(files)
