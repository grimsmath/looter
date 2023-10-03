from lib.rasmil.widgets import get_font_markup
from gi.repository import Gtk


class PagePatch():
  def setup(self, name, title):
    self.load_css('../static/css/main.css')

    """ Add a page with css styled content to the stack"""
    # Content box for the page
    frame = Gtk.Frame()

    # Set Frame Margins
    frame.set_margin_top(15)
    frame.set_margin_start(15)
    frame.set_margin_end(15)
    frame.set_margin_bottom(15)

    # Left/Right Paned
    # Orientation is the ways the separator is moving, not the way it is facing
    # So HORIZONTAL split in Left/Right and VERTICAL split in Top/Down
    self.left_right_paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)

    # Left Side
    left_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    left_box.set_vexpand(True)
    left_box.set_spacing(5)
    left_label = Gtk.Label.new("LEFT")
    left_label.set_valign(Gtk.Align.START)
    left_label.set_halign(Gtk.Align.START)
    left_box.append(left_label)

    # Add Progress Bar
    progress = Gtk.ProgressBar()
    progress.set_fraction(.75)
    left_box.append(progress)

    # Add Scale
    scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 5)
    scale.set_value(25)
    left_box.append(scale)

    # sepatator
    separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    left_box.append(separator)
    self.left_right_paned.set_start_child(left_box)
    self.left_right_paned.set_shrink_start_child(False)  # Can't shrink

    # Right Side
    right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    right_label = Gtk.Label.new("RIGHT")
    right_label.set_valign(Gtk.Align.START)
    right_label.set_halign(Gtk.Align.START)
    right_box.append(right_label)

    # TexkView
    text = Gtk.TextView.new()

    # Set the default width
    text.set_size_request(150, -1)

    # Set Wrap Mode to word
    text.set_wrap_mode(Gtk.WrapMode.WORD)

    # Add some text
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vitae leo ac magna lobortis maximus. Etiam eleifend, libero a pulvinar ornare, justo nunc porta velit, ut sodales mi est feugiat tellus.'
    text.get_buffer().set_text(txt)
    right_box.append(text)

    # Add Switches
    for txt in ['Reveal', 'Yet Another Option']:
        grid = Gtk.Grid()
        grid.set_column_spacing(30)
        grid.insert_row(0)
        grid.insert_column(0)
        grid.insert_column(1)
        grid.insert_column(2)
        grid.set_row_homogeneous(True)
        label = Gtk.Label.new(txt)
        label.set_hexpand(True)
        label.set_xalign(0.0)
        label.set_valign(Gtk.Align.CENTER)
        switch = Gtk.Switch()
        if txt == "Reveal":
            switch.connect('state-set', self.on_switch_activate)
            switch.set_state(True)
        grid.attach(label, 0, 1, 2, 1)
        grid.attach(switch, 2, 1, 1, 1)
        right_box.append(grid)

    # Some bottoms
    lock_btn = Gtk.LockButton.new()
    right_box.append(lock_btn)

    # Add the box to paned
    self.left_right_paned.set_end_child(right_box)
    self.left_right_paned.set_shrink_end_child(False)  # Can't shrink

    # Top/Down Paned
    self.top_botton_paned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)

    # Top
    self.top_botton_paned.set_start_child(self.left_right_paned)
    self.top_botton_paned.set_shrink_start_child(False)

    # Bottom
    self.bottom_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.bottom_box.set_vexpand(False)

    # Add a label with custom font in the center
    label = Gtk.Label()
    markup = get_font_markup(
        'Noto Sans Regular 24', f'This page is styled using main.css')
    label.set_markup(markup)

    # fill the whole page, will make the Label centered.
    label.set_halign(Gtk.Align.CENTER)
    label.set_vexpand(False)
    self.bottom_box.append(label)
    label = Gtk.Label()
    markup = get_font_markup(
        'Noto Sans Regular 18', f'UGLY AS HELL, but shows how it is working')
    label.set_markup(markup)

    # fill the whole page, will make the Label centered.
    label.set_halign(Gtk.Align.CENTER)
    label.set_vexpand(False)
    self.bottom_box.append(label)

    # Revealer
    self.revealer = Gtk.Revealer()
    self.revealer.set_valign(Gtk.Align.END)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label = Gtk.Label.new("This is a revlealer")
    box.append(label)
    self.revealer.set_child(box)
    self.revealer.set_transition_type(Gtk.RevealerTransitionType.CROSSFADE)
    self.revealer.set_transition_duration(200)
    self.revealer.set_reveal_child(True)
    self.bottom_box.append(self.revealer)
    self.top_botton_paned.set_end_child(self.bottom_box)
    self.top_botton_paned.set_shrink_end_child(False)  # Can't shrink
    frame.set_child(self.top_botton_paned)
    self.page3_label = label

    # add custom styling to widgets
    self.add_custom_styling(frame)

    # Add the content box as a new page in the stack
    return self.stack.add_page(name, title, frame)