class LoginPage:
    pass


class CabinetPage:
    pass


class SearchPage:
    pass


class PageFactory:
    def __init__(self, page_name):
        if 'login' in page_name:
            return LoginPage()
        elif 'cabinet' in page_name:
            return CabinetPage()


