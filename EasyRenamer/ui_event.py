import os
from typing import Final

from PyQt5.QtWidgets import QFileDialog

import utils
from file_utils import Folder
from file_utils import SortType


def eventSetPage(base, index: int):
    old_page_number = base.current_page
    base.current_page = index
    utils.FrameUtil.getFrameByPage(base, base.current_page, old_page_number)


def eventSetFolderPath(base):
    path = base.input_path.text()

    if not isFolderExist(path):
        execMessageBox(base, "폴더의 경로가 올바르지 않습니다.")
    else:
        base.folder = Folder(path)


def isFolderExist(path: str):
    return os.path.isdir(path)


def execMessageBox(base, error_message):
    message_box = utils.getErrorMessageBox(base, error_message)
    message_box.exec()


def eventSetExtFrameInput(base, checked):
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


def eventSetSortType(base, index: int):
    if index == 0:
        base.sort_type = SortType.NAME
    elif index == 1:
        base.sort_type = SortType.TIME
    elif index == 2:
        base.sort_type = SortType.SIZE


def eventSearchFolderPath(base):
    path = QFileDialog.getExistingDirectory(base, "Select Folder")
    base.input_path.setText(path)


def eventUpdateExtFrameText(base):
    try:
        files_in_folder = base.folder.get_file_relative_paths()
    except Exception as e:
        execMessageBox(base, str(e))
        return

    if isExtFrameAll(base):
        files = files_in_folder
    else:
        new_extension = getExtFrameExtension(base)
        files = utils.find_files_with_ext(new_extension, files_in_folder)

    result = ""
    file_count = len(files)
    MAX_RESULT: Final[int] = 13

    if file_count == 0:
        result = "변경할 파일이 없습니다"
    elif file_count <= MAX_RESULT:
        for i in range(file_count):
            result += files[i] + "\n"
    else:
        for i in range(MAX_RESULT):
            result += files[i] + "\n"
        result += f" + {len(files) - MAX_RESULT}개의 파일들"

    base.ext_frame_text_browser_result.clear()
    base.ext_frame_text_browser_result.append(result)


def isExtFrameAll(base) -> bool:
    return base.ext_frame_checkbox_all.isChecked()


def getExtFrameExtension(base) -> str:
    return base.ext_frame_input_old_ext.text()
