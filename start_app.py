import sys
from PyQt5.QtWidgets import QApplication
from MainWindowBiblio import MainWindowBiblio

app = QApplication(sys.argv)
mainWindowBiblio = MainWindowBiblio()
mainWindowBiblio.show()
rc = app.exec_()
sys.exit(rc)

