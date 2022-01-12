import sys

from PyQt5.QtWidgets import (
    QApplication,
)

from ui_template import EasyRenamer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    renamer = EasyRenamer()
    sys.exit(app.exec_())
