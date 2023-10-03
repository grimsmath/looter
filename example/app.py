import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

from window import AppWindow

class Application(Gtk.Application):
    """ Main Aplication class """

    def __init__(self):
        super().__init__(application_id='com.davidkingjr.looter',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = AppWindow("Looter Theatre Controller",
                            width=800, 
                            height=800, 
                            application=self)
        win.present()


def main():
    """ Run the main application"""
    app = Application()
    return app.run(sys.argv)


if __name__ == '__main__':
    main()
