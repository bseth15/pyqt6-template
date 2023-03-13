from PyQt6.QtWidgets import QApplication, QWidget

# for command line arguments
import sys

# You need on (and only  one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you known you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
