from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QLineEdit,
    QWidget,
    QPushButton,
    QComboBox,
    QLabel,
)

from file_utils import Folder
from file_utils import SortType
from ui_event import eventSetFolderPath, eventSetPage, eventSearchFolderPath
from utils import FrameUtil


class EasyRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.button_ok: QPushButton = QPushButton()
        self.combobox_type: QComboBox = QComboBox()
        self.button_search: QPushButton = QPushButton()
        self.input_path: QLineEdit = QLineEdit()
        self.label_path: QLabel = QLabel()
        self.current_page: int = 0
        self.folder: Folder = Folder("")
        self.sort_type = SortType.NAME
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Renamer")
        self.resize(1080, 720)

        font = QFont()
        font.setPointSize(14)

        self.label_path = QLabel("폴더 경로", self)
        self.label_path.setObjectName("label_path")
        self.label_path.setGeometry(QRect(200, 10, 81, 35))
        self.label_path.setFont(font)
        self.label_path.setScaledContents(False)
        self.label_path.setAlignment(Qt.AlignCenter)

        self.input_path = QLineEdit(self)
        self.input_path.setObjectName("input_path")
        self.input_path.setGeometry(QRect(300, 10, 500, 35))
        self.input_path.setFont(font)
        self.input_path.setAlignment(Qt.AlignCenter)

        self.button_search = QPushButton("Search", self)
        self.button_search.setObjectName("Search")
        self.button_search.setGeometry(QRect(810, 10, 75, 35))
        self.button_search.clicked.connect(lambda checked: eventSearchFolderPath(self))

        self.button_ok = QPushButton("OK", self)
        self.button_ok.setObjectName("OK")
        self.button_ok.setGeometry(QRect(890, 10, 75, 35))
        self.button_ok.clicked.connect(lambda checked: eventSetFolderPath(self))

        self.combobox_type = QComboBox(self)
        self.combobox_type.setObjectName("input_Type")
        self.combobox_type.setGeometry(QRect(370, 70, 350, 35))
        self.combobox_type.setFont(font)
        self.combobox_type.addItems(["확장자 변경", "번호 붙이기"])
        self.combobox_type.activated[int].connect(
            lambda index: eventSetPage(self, index)
        )

        FrameUtil.initFrame(self)

        self.show()
