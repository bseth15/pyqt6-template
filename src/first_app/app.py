import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# You need on (and only  one) QApplication instance per application.
# If command line arguments will not be used, QApplication([]) works too.
app = QApplication(sys.argv)

window = QMainWindow()
window.show()  # IMPORTANT!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
