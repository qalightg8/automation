class LoginPage:
    def set_login(self, login):
        """вводимо логін"""

        return self

    def set_password(self, password):
        """вводимо пароль"""
        return self

    def submit(self):
        """тиснемо SUBMIT"""


LoginPage().set_login('Vasya').set_password('123').submit()