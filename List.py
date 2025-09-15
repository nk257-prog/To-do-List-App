import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QComboBox, QDateEdit, QMessageBox
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtCore import QDate

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List Application') 
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.todo_list = QListWidget()

        palette = QPalette()
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        self.todo_list.setPalette(palette)

        self.todo_list.setStyleSheet("background-color: #f7f7f7; font-size: 14px; border: 1px solid #ddd;")
        self.layout.addWidget(self.todo_list)

        self.task_layout = QHBoxLayout()
        self.add_task_input = QLineEdit()
        self.add_task_input.setPlaceholderText('Add a new task')
        self.add_task_input.setStyleSheet("font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        self.add_button.setStyleSheet("background-color: #4caf50; color: white; font-size: 14px; border: none; padding: 8px 12px; border-radius: 5px;")
        self.task_layout.addWidget(self.add_task_input)
        self.task_layout.addWidget(self.add_button)
        self.layout.addLayout(self.task_layout)

        self.options_layout = QHBoxLayout()
        self.category_combo = QComboBox()
        self.category_combo.addItem('Personal')
        self.category_combo.addItem('Work')
        self.category_combo.addItem('Shopping')
        self.category_combo.setStyleSheet("font-size: 14px; border: 1px solid #ddd; border-radius: 5px;")
        self.options_layout.addWidget(self.category_combo)

        self.due_date = QDateEdit()
        self.due_date.setDate(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        self.due_date.setStyleSheet('font-size: 14px; border: 1px solid #ddd; border-radius: 5px;')
        self.options_layout.addWidget(self.due_date)

        self.remove_button = QPushButton('Remove Task')
        self.remove_button.clicked.connect(self.remove_task)
        self.remove_button.setStyleSheet("background-color: #ff5722; color: white; font-size: 14px; border: none; padding: 8px 12px; border-radius: 5px;")
        self.options_layout.addWidget(self.remove_button)

        self.layout.addLayout(self.options_layout)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.add_task_input.text()
        if task:
            category = self.category_combo.currentText()
            due_date = self.due_date.date().toString('dd/MM/yyyy') 
            task_text = f"{task} ({category}) - Due: {due_date}"   
            self.todo_list.addItem(task_text)
            self.add_task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a task.')    
    def remove_task(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            self.todo_list.takeItem(self.todo_list.row(selected_item))
        else:
            QMessageBox.warning(self, 'Warning', 'Select a Task to remove.')  

def main():
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
                  




        
