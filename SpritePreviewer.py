#Max Feng
#u1605233
#https://github.com/z1305712215-droid/sprite-previewer
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.num_frames = 21
        self.frames = load_sprite('spriteImages', self.num_frames)
        self.current_frame = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

        self.setupUI()


    def setupUI(self):
        frame = QFrame()
        main_layout = QVBoxLayout()

        self.sprite_label = QLabel()
        self.sprite_label.setPixmap(self.frames[0])
        self.sprite_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.sprite_label)

        slider_frame = QFrame()
        slider_layout = QHBoxLayout()

        fps_text_label = QLabel("Frames per second")
        slider_layout.addWidget(fps_text_label)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        slider_layout.addWidget(self.slider)

        self.fps_label = QLabel("10")
        slider_layout.addWidget(self.fps_label)

        slider_frame.setLayout(slider_layout)
        main_layout.addWidget(slider_frame)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.start_stop)
        main_layout.addWidget(self.start_stop_button)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.pause)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.slider.valueChanged.connect(self.update_fps_label)

    def update_fps_label(self, value):
        self.fps_label.setText(str(value))
        if self.timer.isActive():
            self.timer.setInterval(int(1000 / value))

    def start_stop(self):
        if self.start_stop_button.text() == "Start":
            fps = self.slider.value()
            self.timer.start(int(1000 / fps))
            self.start_stop_button.setText("Stop")
        else:
            self.timer.stop()
            self.start_stop_button.setText("Start")

    def next_frame(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.sprite_label.setPixmap(self.frames[self.current_frame])

    def pause(self):
        self.timer.stop()
        self.start_stop_button.setText("Start")


def main():
    app = QApplication([])
    window = SpritePreview()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
