import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from Split import Split

# 1 - isRecording -> Pause, Complete : Start Recording
# 2 - onStartRecording -> new Split, set start time (ISO)
# 3 - onStopRecording -> set end time (ISO)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize Window
        self.setWindowTitle("Sunken Time")
        self.setWindowIcon(QIcon("maps.ico"))
        self.resize(640, 480)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Define GUI components
        record_button = QPushButton(
            icon=QIcon("./assets/play-circle-fill.svg"),
            parent=self,
            clicked=self.start_recording,
        )
        pause_button = QPushButton(
            icon=QIcon("./assets/pause-circle-fill.svg"),
            parent=self,
            clicked=self.start_recording,
        )
        for b in [record_button, pause_button]:
            b.setFixedSize(100, 60)
            b.setIconSize(QSize(40, 40))
            
        complete_button = QPushButton("&Finish Task", clicked=self.start_recording)
        self.description_input = QTextEdit()

        # self.text_input = QLineEdit()
        widgets = [
            record_button,
            pause_button,
            self.description_input,
            complete_button,
        ]
        
        for w in widgets:
            layout.addWidget(w)

    def start_recording(self):
        self.description_input.setText(f"Hello world")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #                   QPushButton {
    #                       border: 1px solid green;
    #                   }
    #                   ''')
    window = MyApp()
    window.show()

    app.exec()
