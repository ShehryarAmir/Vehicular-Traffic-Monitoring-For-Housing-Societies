import sys

from PyQt5.QtWidgets import QApplication
import qdarkstyle

from MainWindow import MainWindow



def main():
    app = QApplication(sys.argv)
    win = MainWindow()

    # Setup style
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # Show main window
    win.show()

    # Start event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




def show_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

show_frame()