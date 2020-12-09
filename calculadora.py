import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QLineEdit


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(300, 300)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: white; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        #linha 1
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('-'), 1, 4, 1, 1)
        #linha 2
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('*'), 2, 3, 1, 1)
        self.add_btn(QPushButton('/'), 2, 4, 1, 1)
        #linha 3
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 0, 1, 2)

        self.add_btn(
            QPushButton('C'), 3, 3, 1, 1,
            lambda: self.display.setText(''),
            'background: orange; color:white; font-weight:700; '
        )
        self.add_btn(
            QPushButton('<-'), 3, 4, 1, 1,
            lambda: self.display.setText(self.display.text()[:-1]),
            'background: red; color:white; font-weight:700; '
        )

        #linha 4
        self.add_btn(QPushButton('0'), 4, 0, 1, 2)
        self.add_btn(QPushButton('.'), 4, 2, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 3, 1, 2,
            self.eval_igual,
            'background: green; color:white; font-weight:700; '
        )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colsplan, funcao = None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colsplan)
        if not funcao:
            btn.clicked.connect(lambda: self.display.setText(self.display.text() + btn.text()))
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if style:
            btn.setStyleSheet(style)

    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))

        except Exception as erro:
            self.display.setText('conta invalida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
