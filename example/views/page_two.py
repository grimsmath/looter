from lib.rasmil.widgets import Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, ButtonRow, MaterialColorDialog, ColumnViewListStore
from gi.repository import Gtk
from .page_header import PageHeader


class PageCues():
  def setup(self, name, title):
    """ Add a page with a text selector to the stack"""
    # Content box for the page
    main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    # Add info selector
    selector = TextSelector()
    selector.add_row("Orange", "Orange")
    selector.add_row("Apple", "Apple")
    selector.add_row("Water Melon", "Water Melon")
    selector.add_row("Lollypop", "Lollypop")
    selector.set_callback(self.on_select_text_selector)
    main.append(selector)

    # Add a label with custom font in the center
    frame, content_right, label = PageHeader.setup(name, title)
    self.page2_label = label

    # Overlay
    overlay_info = Gtk.InfoBar()
    overlay_info.set_halign(Gtk.Align.FILL)
    overlay_info.set_valign(Gtk.Align.START)
    overlay_info.set_margin_top(10)
    overlay_info.set_margin_start(10)
    overlay_info.set_margin_end(10)

    lbl = Gtk.Label()
    lbl.set_halign(Gtk.Align.FILL)
    lbl.set_valign(Gtk.Align.FILL)
    lbl.set_hexpand(True)
    lbl.set_vexpand(True)
    lbl.set_markup(
        '<span foreground="#ff0000" size="xx-large">This is an Gtk.Infobar as an overlay</span>')
    overlay_info.add_child(lbl)
    self.overlay_info = overlay_info
    frame_child = Gtk.Frame()

    # TextView
    sw = Gtk.ScrolledWindow()
    text = Gtk.TextView.new()
    text.set_vexpand(True)

    # Set Wrap Mode to word
    text.set_wrap_mode(Gtk.WrapMode.WORD)

    # Add some text
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae leo ac magna lobortis maximus. ' \
          'Etiam eleifend, libero a pulvinar ornare, justo nunc porta velit, ut sodales mi est feugiat tellus. '
    text.get_buffer().set_text(txt * 10)
    sw.set_child(text)
    frame_child.set_child(sw)
    overlay = Gtk.Overlay()
    overlay.set_margin_top(20)
    overlay.set_margin_start(20)
    overlay.set_margin_end(20)
    overlay.set_margin_bottom(20)
    overlay.set_child(frame_child)
    overlay.add_overlay(overlay_info)
    content_right.append(overlay)

    # Switch to control overlay visibility
    switch_row = SwitchRow("Show Overlay")
    switch_row.set_state(True)
    switch_row.connect('state-set', self.on_switch_overlay)
    content_right.append(switch_row)
    main.append(frame)

    # Add the content box as a new page in the stack
    return self.stack.add_page(name, title, main)