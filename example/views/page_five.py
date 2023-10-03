from lib.rasmil.widgets import Window, Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, ButtonRow, MaterialColorDialog, ColumnViewListStore
from gi.repository import Gtk
from components.elements import ColumnElem, ListElem
from components.components import MyColumnViewColumn, MyListView, MyListViewStrings
from .page_header import PageHeader


class PageFive():
  def setup(self, name, title):
    """ Add a new page to the stack"""
    # Content box for the page
    frame, content, label = PageHeader.setup(name, title)
    self.page5_label = label

    # Material Color button
    btn_row = ButtonRow(["Material Color"], self.on_button_chooser)
    content.append(btn_row)

    # Add the content box as a new page in the stack
    return self.stack.add_page(name, title, frame)