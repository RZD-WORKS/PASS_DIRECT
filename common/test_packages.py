import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

class ImageView(QWidget):
   def __init__(self, parent = None):
      super().__init__(parent)

      self.setWindowTitle("Картинка")
      self.setGeometry(100, 100, 800, 600)

      label = QLabel(self)
      pixmap = QPixmap('123.jpeg')

      label.setPixmap(pixmap)


class MyWindow(QMainWindow):
   def __init__(self, parent = None):
      super().__init__(parent)

      self.setupUi()
   
   def setupUi(self):
      self.setWindowTitle("NAVBANK")
      self.resize(1280, 720)

      central_widget = QWidget()

      self.setCentralWidget(central_widget)

      layout = QVBoxLayout(central_widget)

      # CSS
      self.setStyleSheet("background-color: #806087")

      self.stacked_image = QStackedWidget()
      layout.addWidget(self.stacked_image)

      self.lbl = QLabel("Добро пожаловать, богач", self)
      self.lbl_font = QFont()
      # self.lbl_font.setFamily("")
      self.lbl_font.setPointSize(15)
      self.lbl.setStyleSheet("color: white")


      self.lbl.setFont(self.lbl_font)
      # self.lbl.move(100, 50)

      self.lbl.adjustSize()
      self.lbl.setAlignment(Qt.AlignCenter | Qt.AlignTop)

      horizont_spacer = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
      layout.addItem(horizont_spacer)

      layout.setSpacing(10)
      layout.setContentsMargins(400, 0, 400, 100)
      # layout.addStretch(1)
      
      self.lbl_name = QLabel("Введите свое имя пользователя", self)
      self.lbl_name.setFont(self.lbl_font)

      self.input1 = QLineEdit(self)
      self.input1.setFont(self.lbl_font)

      self.lbl_password = QLabel("Введите свой пароль", self)
      self.lbl_password.setFont(self.lbl_font)

      self.input2 = QLineEdit(self)
      self.input2.setFont(self.lbl_font)

      self.button = QPushButton("Войти", self)
      self.button.setFont(self.lbl_font)
      self.button.setStyleSheet("color: white")
      self.button.clicked.connect(self.login)

      self.lbl_status = QLabel("", self)
      self.lbl_status.setFont(self.lbl_font)

      layout.addWidget(self.lbl)
      layout.addWidget(self.lbl_name)
      layout.addWidget(self.input1)
      layout.addWidget(self.lbl_password)
      layout.addWidget(self.input2)
      layout.addWidget(self.button)
      layout.addWidget(self.lbl_status)

      self.image_w = QDialog()
      self.stacked_image.addWidget(self.image_w)

      image_layout = QVBoxLayout(self.image_w)

      self.image_lable = QLabel(self.image_w)
      pixmap = QPixmap('common/123.jpeg')

   def login(self):
      username = self.input1.text()
      password = self.input2.text()

      if username != "123" or password != "123":
         self.lbl_status.setText("Данные введены неверно")
         self.lbl_status.setStyleSheet("color: red")
         image = ImageView
         print("Данные введены неверно")
      else:
         self.lbl_status.setText("Добро пожаловать")
         self.lbl_status.setStyleSheet("color: green")

         timer = QTimer(self)
         timer.singleShot(3000, self.close_app)
         print("Добро пожаловать")

   def close_app(self):
      self.close()


app = QApplication(sys.argv)
win = MyWindow()

win.show()

sys.exit(app.exec_())