from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                             QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem,
                             QHBoxLayout, QSizePolicy)
from task_methods import get_all_tasks

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Список задач")
window.resize(600, 400)

# Главный контейнер
central_widget = QWidget()
main_layout = QVBoxLayout()
central_widget.setLayout(main_layout)
window.setCentralWidget(central_widget)

# Таблица для задач (верхняя часть)
table = QTableWidget()
main_layout.addWidget(table)

# Нижняя панель с кнопкой
bottom_panel = QWidget()
bottom_layout = QHBoxLayout()
bottom_panel.setLayout(bottom_layout)
main_layout.addWidget(bottom_panel)

# Кнопка "Создать задачу"
create_button = QPushButton("Создать задачу")
create_button.setFixedSize(150, 30)  # Устанавливаем фиксированный размер
bottom_layout.addStretch()  # Добавляем растягивающееся пространство слева
bottom_layout.addWidget(create_button)  # Добавляем кнопку
bottom_layout.addStretch()  # Добавляем растягивающееся пространство справа

# Кнопка "Показать все задачи" (оставлена наверху)
show_button = QPushButton("Показать все задачи")
main_layout.insertWidget(0, show_button)  # Добавляем в начало layout


def show_tasks():
    tasks = get_all_tasks()

    if not tasks:
        table.setRowCount(1)
        table.setColumnCount(1)
        table.setItem(0, 0, QTableWidgetItem("Нет задач"))
        return

    headers = list(tasks[0].keys())
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setRowCount(len(tasks))

    for row, task in enumerate(tasks):
        for col, (key, value) in enumerate(task.items()):
            table.setItem(row, col, QTableWidgetItem(str(value)))

    table.resizeColumnsToContents()


show_button.clicked.connect(show_tasks)

window.show()
app.exec_()