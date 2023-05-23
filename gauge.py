import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QRect, QBasicTimer
from PyQt5.QtGui import QPainter, QPen, QFont, QColor


class LinearGauge(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumSize(120, 80)
        self.value = 0
        self.max_value = 100
        self.value_colors = [(0, Qt.green), (60, Qt.yellow), (80, Qt.red), (100, Qt.red)]
        self.direction = 1  # 1 for increasing, -1 for decreasing
        self.timer = QBasicTimer()
        self.timer.start(100, self)

    def timerEvent(self, event):
        if self.value >= 90:
            self.direction = -1
        elif self.value <= 50:
            self.direction = 1

        self.value += self.direction
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw gauge background
        gauge_rect = QRect(10, 10, self.width() - 20, self.height() - 20)
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

        # Draw dial
        dial_rect = QRect(dial_pos, gauge_rect.top(), 10, gauge_rect.height())
        painter.setPen(QPen(Qt.black, 0))
        painter.setBrush(Qt.white)
        painter.drawRect(dial_rect)

        # Draw value text
        value_text = f'{self.value} PSI'
        font = QFont(self.font())
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QPen(Qt.black))
        painter.drawText(self.rect(), Qt.AlignCenter, value_text)


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
    sys.exit(app.exec_())
