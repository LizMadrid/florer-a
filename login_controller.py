from PyQt6 import QtWidgets, uic

class LoginController:
    def __init__(self,window, model):
        self.window = window
        self.model =model
        self.window.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        username= self.window.txt_username.text()
        password = self.window.txt_password.text()
        if username == "admin" and password == "123":
         self.window.login_successfull.emit()
         print("Login button clicked")
        else:
           #print("Login incorrecto")
           QtWidgets.QMessageBox.warning(
              self.window,
              "Floreria login -ERROR",
              "Login incorrecto"
           )
           