from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from task_methods import *  # Импортируем нашу функцию

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Пример PyQt")

# Создаем центральный виджет и layout
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Создаем кнопку и метку для вывода текста
button = QPushButton("Нажми меня")
result_label = QLabel("Здесь будет результат")
layout.addWidget(button)
layout.addWidget(result_label)

result = get_all_tasks()

# Связываем кнопку с функцией
button.clicked.connect(lambda: result_label.setText('Hfsfasdd'))

window.show()
app.exec()