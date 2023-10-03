import time
from ..lib.rasmil.widgets import Window, Stack, MenuButton, \
    get_font_markup, SearchBar, MaterialColorDialog
from views.page_one import PageGroups
from views.page_two import PageCues
from views.page_three import PagePatch 
from views.page_four import PageSetup
from views.page_five import PageFive
from constants import APP_MENU
from gi.repository import Gtk


class AppWindow(Window):
    def __init__(self, title, width, height, **kwargs):
        super(AppWindow, self).__init__(title, height, width, **kwargs)

        # load the custom css, so we can use it later
        self.load_css('static/css/main.css')
        self.revealer = None

        # Add Menu Button to the titlebar (Right Side)
        menu = MenuButton(APP_MENU, 'app-menu')
        self.headerbar.pack_end(menu)

        # Create actions to handle menu actions
        self.create_action('new', self.menu_handler)
        self.create_action('about', self.menu_handler)
        self.create_action('quit', self.menu_handler)
        self.create_action('shortcuts', self.menu_handler)

        # make a new title label and add it to the left.
        # So we kan place the stack switcher in the middle
        label = Gtk.Label()
        label.set_text(title)

        # add 2 chars indent on the label for better looks
        label.set_halign(Gtk.Align.END)
        label.set_width_chars(len(title) + 2)
        self.headerbar.pack_start(label)

        # Main content box
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Search Bar
        self.search = SearchBar(self)
        content.append(self.search)

        # search bar is active by default
        self.search.set_callback(self.on_search)

        # Stack
        self.stack = Stack()

        # Stack Pages
        self.page1 = PageGroups.setup(self, 'page1', 'Groups')
        self.page2 = PageCues.setup(self, 'page2', 'Cues')
        self.page3 = PagePatch.setup(self, 'page3', 'Patch')
        self.page4 = PageSetup.setup(self, 'page4', 'Setup')
        self.page5 = PageFive.setup(self, 'page5', 'Page 5')

        # add stack switcher to center of titlebar
        self.headerbar.set_title_widget(self.stack.switcher)

        # Add stack to window
        content.append(self.stack)

        # Add main content box to window
        self.set_child(content)

    def setup_page_five(self, name, title):
        PageFive.setup(self, name, title)

    def _get_text_markup(self, txt):
        txt = f'<span foreground="#BF360C" weight="bold">{txt}</span>'
        markup = get_font_markup('Noto Sans Regular 14', txt)
        return markup

    def show_shortcuts(self):
        builder = Gtk.Builder.new_from_file('shortcuts.ui')
        shortcuts = builder.get_object('shortcuts')
        shortcuts.present()

    # ---------------------- Handlers --------------------------
    def menu_handler(self, action, state):
        """ Callback for  menu actions"""
        name = action.get_name()
        print(f'active : {name}')
        if name == 'quit':
            self.close()
        elif name == 'shortcuts':
            self.show_shortcuts()

    def on_color_selected(self, widget):
        selected_color = self.chooser.get_rgba()
        color_txt = selected_color.to_string()
        markup = self._get_text_markup(
            f'{widget.get_label()} was pressed. {color_txt}')
        self.page5_label.set_markup(markup)

    def on_button_chooser(self, widget):
        """ callback for buttom clicked (Page1) """
        dialog = MaterialColorDialog("Select Color", self)
        dialog.connect('response', self.on_dialog_response)
        dialog.show()

    def on_search(self, widget):
        """ callback for the searchbar entry """
        print(f'Searching for : {widget.get_text()}')

    def on_select_icon_selector(self, name):
        """ called when icon_selector selection is changed (Page1) """
        markup = self._get_text_markup(f'{name} is selected')
        self.page1_label.set_markup(markup)

    def on_select_text_selector(self, name):
        """ called when text_selector is changed (Page2) """
        markup = self._get_text_markup(f'{name} is selected')
        self.page2_label.set_markup(markup)

    def on_switch_activate(self, widget, state):
        """ callback for reveal switch (Page3) """
        if self.revealer:
            self.revealer.set_reveal_child(state)
            time.sleep(.5)
            self.top_botton_paned.set_position(1000)

    def on_switch_overlay(self, widget, state):
        """ callback for overlay switch (Page2) """
        if self.overlay_info:
            self.overlay_info.set_revealed(state)

    def on_button_clicked(self, widget):
        """ callback for buttom clicked (Page1) """
        markup = self._get_text_markup(f'{widget.get_label()} was pressed')
        self.page1_label.set_markup(markup)

    def on_calendar_changed(self, widget):
        """ callback for calendar selection (Page1) """
        date = widget.get_date().format('%F')
        txt = f'{date} was selected in calendar'
        markup = self._get_text_markup(txt)
        self.page1_label.set_markup(markup)

    def on_entry_activate(self, widget):
        """ callback for entry actication (Page1) """
        txt = f'{widget.get_buffer().get_text()} was typed in entry'
        markup = self._get_text_markup(txt)
        self.page1_label.set_markup(markup)

    def on_dialog_response(self, widget, response_id):
        if response_id == Gtk.ResponseType.OK:
            # get selected color in hex format
            color = widget.get_color()
            markup = f'<span size="xx-large" foreground="{color}">the color {color} was selected</span>'
            self.page5_label.set_markup(markup)
        elif response_id == Gtk.ResponseType.CANCEL:
            print("cancel")
            # if the messagedialog is destroyed (by pressing ESC)
        elif response_id == Gtk.ResponseType.DELETE_EVENT:
            print("dialog closed or cancelled")
        widget.destroy()
