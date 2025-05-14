
from ui.pages.main_page import MainPage
from ui.pages.quick_auth import QuickAuth


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.quick_auth = QuickAuth()

app = Application()