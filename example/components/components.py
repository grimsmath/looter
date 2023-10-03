from lib.rasmil.widgets import Window, Stack, MenuButton, get_font_markup, SearchBar, \
    IconSelector, TextSelector, ListViewStrings, ListViewListStore, SwitchRow, \
    ButtonRow, MaterialColorDialog, ColumnViewListStore
from components.elements import ListElem, ColumnElem
from typing import List
import gi
from gi.repository import Gtk, GObject, Gio


class MyListView(ListViewListStore):
    """ Custom ListView """

    def __init__(self, win: Gtk.ApplicationWindow):
        # Init ListView with store model class.
        super(MyListView, self).__init__(ListElem)
        self.win = win
        self.set_valign(Gtk.Align.FILL)
        # self.set_vexpand(True)
        # put some data into the model
        self.add(ListElem("Groups", True))
        self.add(ListElem("Cues", False))
        self.add(ListElem("Patch", True))

    def factory_setup(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::setup signal callback (overloaded from parent class)
        Handles the creation widgets to put in the ListView
        """
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        label.set_margin_start(10)
        switch = Gtk.Switch()
        switch.set_halign(Gtk.Align.END)
        switch.set_margin_end(10)
        box.append(label)
        box.append(switch)
        item.set_child(box)

    def factory_bind(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::bind signal callback (overloaded from parent class)
        Handles adding data for the model to the widgets created in setup
        """
        # get the Gtk.Box stored in the ListItem
        box = item.get_child()
        # get the model item, connected to current ListItem
        data = item.get_item()
        # get the Gtk.Label (first item in box)
        label = box.get_first_child()
        # get the Gtk.Switch (next sibling to the Label)
        switch = label.get_next_sibling()
        # Update Gtk.Label with data from model item
        label.set_text(data.name)
        # Update Gtk.Switch with data from model item
        switch.set_state(data.state)
        # connect switch to handler, so we can handle changes
        switch.connect('state-set', self.switch_changed, item.get_position())
        item.set_child(box)

    def factory_unbind(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::unbind signal callback (overloaded from parent class) """
        pass

    def factory_teardown(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::teardown signal callback (overloaded from parent class """
        pass

    def selection_changed(self, widget, ndx: int):
        """ trigged when selecting in listview is changed"""
        markup = self.win._get_text_markup(
            f'Row {ndx} was selected ( {self.store[ndx]} )')
        self.win.page4_label.set_markup(markup)

    def switch_changed(self, widget, state: bool, pos: int):
        # update the data model, with current state
        elem = self.store[pos]
        elem.state = state
        markup = self.win._get_text_markup(
            f'switch in row {pos}, changed to {state}')
        self.win.page4_label.set_markup(markup)


class MyListViewStrings(ListViewStrings):
    """ Custom ListView """

    def __init__(self, win: Gtk.ApplicationWindow):
        # Init ListView with store model class.
        super(MyListViewStrings, self).__init__()
        self.win = win
        self.set_vexpand(True)
        # put some data into the model
        for i in range(1000):
            self.add(f'Item {i}')

    def factory_setup(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::setup signal callback (overloaded from parent class)
        Handles the creation widgets to put in the ListView
        """
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        label.set_margin_start(10)
        item.set_child(label)

    def factory_bind(self, widget: Gtk.ListView, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::bind signal callback (overloaded from parent class)
        Handles adding data for the model to the widgets created in setup
        """
        # get the Gtk.Label
        label = item.get_child()
        # get the model item, connected to current ListItem
        data = item.get_item()
        # Update Gtk.Label with data from model item
        label.set_text(data.get_string())
        # Update Gtk.Switch with data from model item
        item.set_child(label)

    def selection_changed(self, widget, ndx: int):
        """ trigged when selecting in listview is changed"""
        markup = self.win._get_text_markup(
            f'Row {ndx} was selected ( {self.store[ndx].get_string()} )')
        self.win.page4_label.set_markup(markup)


class MyColumnViewColumn(ColumnViewListStore):
    """ Custom ColumnViewColumn """

    def __init__(self, win: Gtk.ApplicationWindow, col_view: Gtk.ColumnView, data: List):
        # Init ListView with store model class.
        super(MyColumnViewColumn, self).__init__(ColumnElem, col_view)
        self.win = win

        # put some data into the model
        for elem in data:
            self.add(ColumnElem(elem))

    def factory_setup(self, widget, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::setup signal callback 
        Handles the creation widgets to put in the ColumnViewColumn
        """
        label = Gtk.Label()
        label.set_halign(Gtk.Align.START)
        label.set_hexpand(True)
        label.set_margin_start(10)
        item.set_child(label)

    def factory_bind(self, widget, item: Gtk.ListItem):
        """ Gtk.SignalListItemFactory::bind signal callback 
        Handles adding data for the model to the widgets created in setup
        """
        label = item.get_child()  # Get the Gtk.Label stored in the ListItem
        data = item.get_item()    # get the model item, connected to current ListItem
        label.set_text(data.name)  # Update Gtk.Label with data from model item

    def selection_changed(self, widget, ndx: int):
        """ trigged when selecting in listview is changed"""
        markup = self.win._get_text_markup(
            f'Row {ndx} was selected ( {self.store[ndx]} )')
        self.win.page4_label.set_markup(markup)