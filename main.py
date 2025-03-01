import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
import random
from ui_window import UiWindow

class CircleDrawer(UiWindow):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(self.draw_circle)  # Обработка нажатия кнопки
        self.circles = []  # Список для хранения параметров окружностей

    def draw_circle(self):
        # Генерация случайного диаметра, позиции и цвета
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Случайный цвет
        self.circles.append((x, y, diameter, color))  # Добавление окружности в список
        self.update()  # Обновление виджета

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)  # Установка случайного цвета
            painter.drawEllipse(x, y, diameter, diameter)  # Рисование окружности

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())