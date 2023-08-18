import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QRect, QBasicTimer, QPoint
from PyQt5.QtGui import QPainter, QPen, QFont, QColor, QPolygon
from updated_gauge import LinearGauge


class VerticalTempLinearGauge(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumSize(60, 100)  # Increased width to accommodate the reading text
        self.value = 0
        self.max_value = 100
        self.min_value = -50
        self.value_colors = [
            (-50, Qt.red),
            (-25, Qt.yellow),
            (0, Qt.green),
            (50, Qt.yellow),
            (75, Qt.red),
            (100, Qt.red)
        ]
        self.direction = 1  # 1 for increasing, -1 for decreasing
        self.timer = QBasicTimer()
        self.timer.start(10, self)

    def setValue(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw gauge background
        gauge_rect = QRect(10, 10, self.width() - 50, self.height() - 20)  # Decreased width for the gauge
        total_range = self.max_value - self.min_value
        for i in range(len(self.value_colors) - 1):
            start_threshold, start_color = self.value_colors[i]
            end_threshold, end_color = self.value_colors[i + 1]
            start_pos = int(gauge_rect.top() + gauge_rect.height() * (start_threshold - self.min_value) / total_range)
            end_pos = int(gauge_rect.top() + gauge_rect.height() * (end_threshold - self.min_value) / total_range)
            section_rect = QRect(gauge_rect.left(), start_pos, gauge_rect.width(), end_pos - start_pos)
            painter.setPen(QPen(start_color, 2))
            painter.setBrush(start_color)
            painter.drawRect(section_rect)

        # Calculate dial position within the valid range
        dial_pos = int(gauge_rect.top() + gauge_rect.height() * (self.value - self.min_value) / total_range)
        dial_pos = max(gauge_rect.top(), min(dial_pos, gauge_rect.bottom() - 10))

        # Draw dial as a triangle
        dial_triangle = QPolygon([
            QPoint(gauge_rect.left() + 2, dial_pos),  # Left point of the triangle
            QPoint(gauge_rect.left() - 8, dial_pos + 5),  # Bottom-left point of the triangle
            QPoint(gauge_rect.left() - 8, dial_pos - 5)  # Top-left point of the triangle
        ])
        painter.setPen(QPen(Qt.black, 2))
        painter.setBrush(Qt.black)
        painter.drawPolygon(dial_triangle)

        # Draw value text beside the gauge
        value_text = f'{self.value} °C'
        font = QFont(self.font())
        font.setBold(True)
        painter.setFont(font)
        painter.setPen(QPen(Qt.black))
        text_rect = QRect(self.width() - 40, 0, 40, self.height())
        painter.drawText(text_rect, Qt.AlignCenter, value_text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linear Gauge")
        self.setGeometry(100, 100, 80, 300)  # Adjusted window size

        self.gauge = LinearGauge(self)
        self.setCentralWidget(self.gauge)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    input_value = 25
    mainWindow.gauge.setValue(input_value)

    sys.exit(app.exec_())
