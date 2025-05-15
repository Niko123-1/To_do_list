from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                             QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem)
from task_methods import get_all_tasks

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Список задач")
window.resize(600, 400)

# Создаем центральный виджет и layout
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Создаем кнопку и таблицу для вывода результатов
button = QPushButton("Показать все задачи")
table = QTableWidget()
layout.addWidget(button)
layout.addWidget(table)


def show_tasks():
    tasks = get_all_tasks()

    if not tasks:
        table.setRowCount(1)
        table.setColumnCount(1)
        table.setItem(0, 0, QTableWidgetItem("Нет задач"))
        return

    # Настраиваем таблицу
    headers = list(tasks[0].keys())
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setRowCount(len(tasks))

    # Заполняем таблицу данными
    for row, task in enumerate(tasks):
        for col, (key, value) in enumerate(task.items()):
            table.setItem(row, col, QTableWidgetItem(str(value)))

    # Ресайзим колонки по содержимому
    table.resizeColumnsToContents()


button.clicked.connect(show_tasks)

window.show()
app.exec_()