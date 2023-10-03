from lib.rasmil.widgets import Window, Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, ButtonRow, MaterialColorDialog, ColumnViewListStore
from gi.repository import Gtk


class PageHeader():
  def setup(name, title):
    """ setup the common widgets for each page """
    # Content box for the page
    frame = Gtk.Frame()

    # Set Frame Margins
    frame.set_margin_top(15)
    frame.set_margin_start(15)
    frame.set_margin_end(15)
    frame.set_margin_bottom(15)

    # Content box for the page
    content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    # Add a label with custom font in the center
    label = Gtk.Label()
    label.set_margin_top(20)
    markup = get_font_markup('Noto Sans Regular 20', f'This is {title}')
    label.set_markup(markup)
    label.set_valign(Gtk.Align.CENTER)
    content.append(label)

    # Output label to write user action on the page
    label = Gtk.Label()
    label.set_margin_top(20)
    label.set_margin_start(20)
    label.set_hexpand(True)
    label.set_halign(Gtk.Align.CENTER)
    label.set_xalign(0.0)
    content.append(label)
    frame.set_child(content)

    return frame, content, label