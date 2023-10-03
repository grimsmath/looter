from gi.repository import Gtk, GObject, Gio


class ColumnElem(GObject.GObject):
    """ custom data element for a ColumnView model (Must be based on GObject) """

    def __init__(self, name: str):
        super(ColumnElem, self).__init__()
        self.name = name

    def __repr__(self):
        return f'ColumnElem(name: {self.name})'


class ListElem(GObject.GObject):
    """ custom data element for a ListView model (Must be based on GObject) """

    def __init__(self, name: str, state: bool):
        super(ListElem, self).__init__()
        self.name = name
        self.state = state

    def __repr__(self):
        return f'ListElem(name: {self.name} state: {self.state})'