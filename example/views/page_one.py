from lib.rasmil.widgets import Window, Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, ButtonRow, MaterialColorDialog, ColumnViewListStore
from gi.repository import Gtk
from .page_header import PageHeader

class PageGroups():
  def setup(self, name, title):
    """ Add a page with a icon selector to the stack"""
    # Main Content box for the page
    main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    # Add info selector
    selector = IconSelector()
    selector.add_row("row1", "dialog-information-symbolic")
    selector.add_row("row2", "software-update-available-symbolic")
    selector.add_row("row3", "drive-multidisk-symbolic")
    selector.add_row("row4", "insert-object-symbolic")
    selector.set_callback(self.on_select_icon_selector)
    main.append(selector)
    page_frame, content_right, lbl = PageHeader.setup(name, title)
    self.page1_label = lbl

    # buttoms
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    box.set_halign(Gtk.Align.CENTER)
    box.set_margin_top(20)
    box.set_spacing(10)
    for x in range(5):
        btn = Gtk.Button()
        btn.set_label(f'Button {x}')
        btn.connect('clicked', self.on_button_clicked)
        box.append(btn)
    content_right.append(box)

    # Entry
    entry = Gtk.Entry()
    entry.set_halign(Gtk.Align.FILL)
    entry.set_valign(Gtk.Align.END)
    entry.set_margin_top(20)
    entry.set_margin_start(20)
    entry.set_margin_end(20)
    entry.set_placeholder_text("Type something here ....")
    entry.connect('activate', self.on_entry_activate)
    content_right.append(entry)

    # Calendar
    calendar = Gtk.Calendar()
    calendar.set_margin_top(20)
    calendar.set_halign(Gtk.Align.CENTER)
    calendar.connect('day-selected', self.on_calendar_changed)
    content_right.append(calendar)

    # DropDown
    model = Gtk.StringList()
    for txt in ['One', 'Two', 'Three', 'Four']:
        model.append(txt)

    dropdown = Gtk.DropDown.new(model)
    dropdown.set_margin_top(20)
    dropdown.set_margin_start(20)
    dropdown.set_size_request(200, -1)
    dropdown.set_halign(Gtk.Align.START)
    content_right.append(dropdown)

    # DropDown
    dropdown = Gtk.DropDown.new_from_strings(
        ['Red', 'Green', 'Blue', 'Black', 'White'])
    dropdown.set_margin_top(20)
    dropdown.set_margin_start(20)
    dropdown.set_size_request(200, -1)
    dropdown.set_halign(Gtk.Align.START)
    content_right.append(dropdown)
    main.append(page_frame)

    # Add the content box as a new page in the stack
    return self.stack.add_page(name, title, main)