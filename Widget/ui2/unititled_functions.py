class SOCKETFUNCTIONS:
    def __init__(self, main_window):
        self.main_window = main_window

    def socket_basic(self):
        self.main_window.ui.close.clicked.connect(self.main_window.close)

