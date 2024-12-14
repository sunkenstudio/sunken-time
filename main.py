import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QLabel,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from models.Split import Split
from models.Task import Task

# 1 - isRecording -> Pause, Complete : Start Recording
# 2 - onStartRecording -> new Split, set start time (ISO)
# 3 - onStopRecording -> set end time (ISO)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.task = Task()
        self.current_split: Split | None = None
        self.record_button: QPushButton | None = None
        self.pause_button: QPushButton | None = None
        self.complete_button: QPushButton | None = None

        self.initialize_window()
        self.add_window_widgets()

        
    def initialize_window(self):
        self.setWindowTitle("Sunken Time")
        self.setWindowIcon(QIcon("maps.ico"))
        self.resize(640, 480)
    
    def add_window_widgets(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Define GUI components
        self.record_button = QPushButton(
            icon=QIcon("./assets/play-circle-fill.svg"),
            parent=self,
            clicked=self.start_recording,
        )
        self.pause_button = QPushButton(
            icon=QIcon("./assets/pause-circle-fill.svg"),
            parent=self,
            clicked=self.stop_recording,
        )
        self.pause_button.setEnabled(False)

        for b in [self.record_button, self.pause_button]:
            b.setFixedSize(100, 60)
            b.setIconSize(QSize(40, 40))
            
        self.complete_button = QPushButton("&Finish Task", clicked=self.start_recording)
        description_input_label = QLabel("What I Did")
        self.description_input = QTextEdit()

        # self.text_input = QLineEdit()
        widgets = [
            self.record_button,
            self.pause_button,
            description_input_label,
            self.description_input,
            self.complete_button,
        ]
        
        for w in widgets:
            layout.addWidget(w)
        
    def start_recording(self):
        self.current_split = Split()
        self.toggle_buttons(True)
        print(self.current_split.start_time)
        
    def stop_recording(self):
        self.current_split.complete()
        self.task.add_split(self.current_split)
        self.toggle_buttons(False)
        print(self.current_split.end_time)
    
    def toggle_buttons(self, is_recording):
        if is_recording:
            self.record_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.complete_button.setEnabled(False)
        else:
            self.record_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.complete_button.setEnabled(True)


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
