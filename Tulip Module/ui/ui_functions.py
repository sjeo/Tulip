from PyQt5.QtGui import QIcon, QFontDatabase, QFont

GLOBAL_if_max = False


class UIFUNCTIONS:
    def __init__(self, main_window):
        self.setup = None
        self.latest = None
        self.create = None
        self.menuVisible = False
        self.setmenu = None
        self.main_window = main_window

    def uibasic(self):
        self.main_window.ui.close.clicked.connect(self.main_window.close)
        self.main_window.ui.minimize.clicked.connect(self.main_window.showMinimized)
        self.main_window.ui.magnify.clicked.connect(lambda: UIFUNCTIONS.maximize(self))
        self.main_window.ui.home_button.clicked.connect(self.show_homewidget)
        self.main_window.ui.socket_button.clicked.connect(self.show_socketwidget)
        self.font_change()
        self.set_tooltip()

    def maximize(self):
        global GLOBAL_if_max
        state = GLOBAL_if_max
        if not state:
            self.main_window.showMaximized()
            GLOBAL_if_max = True
            self.main_window.ui.magnify.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
        else:
            self.main_window.showNormal()
            GLOBAL_if_max = False
            self.main_window.ui.magnify.setIcon(QIcon(u":/icons/images/icons/mdi.square-outline.png"))

    def show_homewidget(self):
        self.main_window.ui.widget_changed.setCurrentWidget(self.main_window.ui.home)

    def show_socketwidget(self):
        self.main_window.ui.widget_changed.setCurrentWidget(self.main_window.ui.socket)

    def font_change(self):
        font_id = QFontDatabase.addApplicationFont("font/PinyonScript-Regular.ttf")
        if font_id != -1:
            # Get the font family from the loaded font
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                custom_font_family = font_families[0]

                # Apply the font using its family name
                custom_font = QFont(custom_font_family, 12)
                self.main_window.ui.name.setFont(custom_font)
        else:
            print("Not found")

    def set_tooltip(self):
        self.main_window.ui.setup_button.setToolTip("Set And Menu")
        self.main_window.ui.socket_create.setToolTip("Socket")

