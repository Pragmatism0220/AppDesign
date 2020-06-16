import sys
import UI
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(u"进制转换器")
    ui = UI.UI()
    sys.exit(app.exec_())
