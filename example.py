import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Starter Application")
        self.resize(400, 200)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Information label
        self.info_label = QLabel("Enter your name below:")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.info_label)

        # Input row (Horizontal Layout)
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type something here...")
        input_layout.addWidget(self.input_field)

        self.submit_btn = QPushButton("Greet Me")
        input_layout.addWidget(self.submit_btn)
        main_layout.addLayout(input_layout)

        # Reset button
        self.clear_btn = QPushButton("Clear")
        main_layout.addWidget(self.clear_btn)

        # Connect signals to slots (event handling)
        self.submit_btn.clicked.connect(self.handle_greeting)
        self.clear_btn.clicked.connect(self.handle_clear)
        self.input_field.returnPressed.connect(self.handle_greeting)

    def handle_greeting(self):
        name = self.input_field.text().strip()
        if not name:
            QMessageBox.warning(self, "Empty Input", "Please enter a name first!")
            return

        self.info_label.setText(f"Hello, {name}!")

    def handle_clear(self):
        self.input_field.clear()
        self.info_label.setText("Enter your name below:")


def main():
    # 1. Initialize the Qt Application
    app = QApplication(sys.argv)

    # 2. Instantiate and display the main window
    window = MainWindow()
    window.show()

    # 3. Start the Qt event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()