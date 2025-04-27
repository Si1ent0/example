
from example.pages.UI.main_page import MainPage
from example.pages.UI.quick_auth import QuickAuth


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.quick_auth = QuickAuth()

app = Application()