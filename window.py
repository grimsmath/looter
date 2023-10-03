import time
from constants import APP_MENU
from lib.rasmil.widgets import Window, Stack, MenuButton, \
    get_font_markup, SearchBar, MaterialColorDialog
from gi.repository import Gtk

class AppWindow(Window):
    def __init__(self, title, width, height, **kwargs):
        super(AppWindow, self).__init__(title, height, width, **kwargs)

        # load the custom css, so we can use it later
        self.load_css('static/css/main.css')
        self.revealer = None

        # Add Menu Button to the titlebar (Right Side)
        menu = MenuButton(APP_MENU, 'app-menu')
        self.headerbar.pack_start(menu)

        # Main content box
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Stack
        self.stack = Stack()

        
