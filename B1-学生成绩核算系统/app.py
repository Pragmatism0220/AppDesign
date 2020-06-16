import sys
import UI
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(u"学生成绩核算系统")
    ui = UI.UI()
    sys.exit(app.exec_())
