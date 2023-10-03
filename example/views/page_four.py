from lib.rasmil.widgets import Window, Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, ButtonRow, MaterialColorDialog, ColumnViewListStore
from gi.repository import Gtk
from components.elements import ColumnElem, ListElem
from components.components import MyColumnViewColumn, MyListView, MyListViewStrings
from .page_header import PageHeader


class PageSetup():
  def setup(self, name, title):
    """ Add a page with a text selector to the stack"""
    # Content box for the page
    frame, content, label = PageHeader.setup(name, title)
    self.page4_label = label

    # ColumnView with custom columns
    self.columnview = Gtk.ColumnView()
    self.columnview.set_show_column_separators(True)
    data = [f'Data Row: {row}' for row in range(50)]
    for i in range(4):
        column = MyColumnViewColumn(self, self.columnview, data)
        column.set_title(f"Column {i}")
        self.columnview.append_column(column)
    lw_frame = Gtk.Frame()
    lw_frame.set_valign(Gtk.Align.FILL)
    lw_frame.set_vexpand(True)
    lw_frame.set_margin_start(20)
    lw_frame.set_margin_end(20)
    lw_frame.set_margin_top(10)
    lw_frame.set_margin_bottom(10)
    sw = Gtk.ScrolledWindow()
    sw.set_child(self.columnview)
    lw_frame.set_child(sw)
    content.append(lw_frame)

    # Listview with switches
    self.listview = MyListView(self)
    lw_frame = Gtk.Frame()
    lw_frame.set_valign(Gtk.Align.FILL)
    lw_frame.set_vexpand(True)
    lw_frame.set_margin_start(20)
    lw_frame.set_margin_end(20)

    # lw_frame.set_margin_top(10)
    lw_frame.set_margin_bottom(10)
    sw = Gtk.ScrolledWindow()
    sw.set_child(self.listview)
    lw_frame.set_child(sw)
    content.append(lw_frame)

    # Simple Listview with strings
    self.listview_str = MyListViewStrings(self)
    lw_frame = Gtk.Frame()
    lw_frame.set_valign(Gtk.Align.FILL)
    lw_frame.set_vexpand(True)
    lw_frame.set_margin_start(20)
    lw_frame.set_margin_end(20)

    # lw_frame.set_margin_top(10)
    lw_frame.set_margin_bottom(10)
    sw = Gtk.ScrolledWindow()

    # Create Gtk.Listview
    lw = self.listview_str
    sw.set_child(lw)
    lw_frame.set_child(sw)
    content.append(lw_frame)
    frame.set_child(content)

    # Add the content box as a new page in the stack
    return self.stack.add_page(name, title, frame)