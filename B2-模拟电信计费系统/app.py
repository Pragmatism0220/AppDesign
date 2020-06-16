import sys
import threading
import UI
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(u"模拟电信计费系统")
    ui = UI.UI()
    t = threading.Thread(target=ui.charging)
    t.setDaemon(True)
    t.start()
    sys.exit(app.exec_())
