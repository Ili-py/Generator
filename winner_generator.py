from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
my_win = QWidget()
my_win.show()
text = QLabel('Победитель:')
winner = QLabel('?')
def show_winner():
    number = randint(0, 999)
    winner.setText(str(number))
    text.setText
    my_win.setWindowTitle ('Определитель победителя')

button = QPushButton('Сгенерировать')
v_line = QVBoxLayout()
v_line.addWidget(text,alignment = Qt.AlignCenter)
v_line.addWidget(winner,alignment = Qt.AlignCenter)
v_line.addWidget(button,alignment = Qt.AlignCenter)
my_win.setLayout(v_line)
button.clicked.connect(show_winner)
my_win.show






app.exec_()