import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
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
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
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

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        self.slider.valueChanged.connect(self.update_fps_label)

    def update_fps_label(self, value):
        self.fps_label.setText(str(value))


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
