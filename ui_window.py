from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class UiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 400, 300)

        # Создание кнопки
        self.pushButton = QPushButton("Draw Circle", self)
        self.pushButton.setFixedSize(100, 30)

        # Размещение кнопки на форме
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)