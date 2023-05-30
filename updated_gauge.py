#MUST BE PYTHON 3.8.8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QRect, QBasicTimer, QPoint  # Import QPoint
from PyQt5.QtGui import QPainter, QPen, QFont, QColor, QPolygon


class LinearGauge(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumSize(100, 60)  # Increased height to accommodate the reading text
        self.value = 0
        self.max_value = 2000
        self.value_colors = [(0, Qt.green), (1500, Qt.yellow), (1800, Qt.red), (2000, Qt.red)]
        self.direction = 1  # 1 for increasing, -1 for decreasing
        self.timer = QBasicTimer()
        self.timer.start(10, self)
        
    # def timerEvent(self, event):
    #     if self.value >= 1700:
    #         self.direction = -1
    #     elif self.value <= 1400:
    #         self.direction = 1

    #     self.value += self.direction
    #     self.update()
    
    def setValue(self, value): 
        self.value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw gauge background
        gauge_rect = QRect(10, 10, self.width() - 20, self.height() - 50)  # Decreased height for the gauge
        total_range = self.value_colors[-1][0] - self.value_colors[0][0]
        for i in range(len(self.value_colors) - 1):
            start_threshold, start_color = self.value_colors[i]
            end_threshold, end_color = self.value_colors[i + 1]
            start_pos = int(gauge_rect.left() + gauge_rect.width() * start_threshold / total_range)
            end_pos = int(gauge_rect.left() + gauge_rect.width() * end_threshold / total_range)
            section_rect = QRect(start_pos, gauge_rect.top(), end_pos - start_pos, gauge_rect.height())
            painter.setPen(QPen(start_color, 2))
            painter.setBrush(start_color)
            painter.drawRect(section_rect)

        # Calculate dial position within the valid range
        dial_pos = int(gauge_rect.left() + gauge_rect.width() * self.value / self.max_value)
        dial_pos = max(gauge_rect.left(), min(dial_pos, gauge_rect.right() - 10))

        # Draw dial as a triangle
        dial_triangle = QPolygon([
            QPoint(dial_pos, gauge_rect.bottom() - 2),  # Bottom point of the triangle
            QPoint(dial_pos + 5, gauge_rect.bottom() + 8),  # Top-right point of the triangle
            QPoint(dial_pos - 5, gauge_rect.bottom() + 8)  # Top-left point of the triangle
        ])
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(Qt.black)
        painter.drawPolygon(dial_triangle)

        # Draw value text below the gauge
        value_text = f'{self.value} PSI'
        font = QFont(self.font())
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QPen(Qt.black))
        text_rect = QRect(0, self.height() - 40, self.width(), 40)
        painter.drawText(text_rect, Qt.AlignCenter, value_text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linear Gauge")
        self.setGeometry(100, 100, 300, 80)

        self.gauge = LinearGauge(self)
        self.setCentralWidget(self.gauge)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    input_value = 423
    mainWindow.gauge.setValue(input_value)

    sys.exit(app.exec_())

