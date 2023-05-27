import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow


class calculator(QMainWindow):
	def __init__(self):
		super(calculator, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

		#digits
		self.ui.btn_0.clicked.connect(lambda: self.add_digital("0"))
		self.ui.btn_1.clicked.connect(lambda: self.add_digital("1"))
		self.ui.btn_5.clicked.connect(lambda: self.add_digital("5"))
		self.ui.btn_6.clicked.connect(lambda: self.add_digital("6"))
		self.ui.btn_7.clicked.connect(lambda: self.add_digital("7"))
		self.ui.btn_8.clicked.connect(lambda: self.add_digital("8"))
		self.ui.btn_9.clicked.connect(lambda: self.add_digital("9"))

	def add_digital(self, btn_text: str) -> None:
		if self.ui.le_entry.text() == "0":
			self.ui.le_entry.setText(btn_text)
		else:
			self.ui.le_entry.setText(btn_text)

if __name__ =="__main__":
	app = QApplication(sys.argv)

	window = calculator()
	window.show()

	sys.exit(app.exec())
