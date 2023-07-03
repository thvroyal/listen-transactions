from main_app.views.controller.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())