from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import csv

def make_it_plus(list_given):
    my_shortcut = ''
    leng = len(list_given)
    for i in range(leng):
        my_shortcut += str(list_given[i]).capitalize() + ' + '
    return my_shortcut[:-3]

class SecondScreen(BoxLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.software = "Sublime Text"
        self.orientation = 'vertical'
        self.main_app = main_app
        self.scroll = 0
        heading = main_app.current_heading
        self.current_popup_number = None

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.heading_widget = Label(text=self.software, bold=True, font_size=20)
        self.add_widget(self.heading_widget)
        self.file_name = None

        self.data_extracted = []




        self.nine_buttons = [Button(text='First'),
                             Button(text='Second'),
                             Button(text='Third'),
                             Button(text='Fourth'),
                             Button(text='Five'),
                             Button(text='Six'),
                             Button(text='Seven'),
                             Button(text='Huit'),
                             Button(text='Nine'),
                             ]

        self.nine_popups = [Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut"),
                            Popup(title="the shortcut")]



    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == '-':
            self.scroll += 1
            try:
                self.add_data()
            except IndexError:
                return True
        if keycode[1] == '0':
            self.scroll -= 1
            try:
                self.add_data()
            except IndexError:
                return True

        # If you press esc or the same number again, you turn off the popup.
        """
        if keycode[1] in ('escape', str(self.current_popup_number)):
            if self.current_popup_number is not None:
                self.nine_popups[self.current_popup_number].dismiss()
        """
        # The previous code didn't quite work, for some reason.
        # So, I hope I fixed it.
        if ((keycode[1] == 'escape') or \
            (self.current_popup_number is not None and \
             keycode[1] == str(self.current_popup_number))):
            self.nine_popups[self.current_popup_number - 1].dismiss()
            self.current_popup_number = None

        codes = [x + 1 for x in range(9)]
        for k in codes:
            if keycode[1] == str(k):
                """
                If the popup screen is already popped up, you turn it off
                then you show the new popup screen.
                Why? Well, if you don't, to get back to the main option
                screen, you have to either press esc many times
                or press every single button you pressed so far but backwards.
                And that's a bit of a pain.
                """
                if self.current_popup_number is not None:
                    self.nine_popups[self.current_popup_number - 1].dismiss()
                self.nine_popups[k - 1].open()  # Fixed off-by-one error.
                self.current_popup_number = k
        return True

    def add_data(self):
        adder = self.scroll * 9

        for i in range(9):
            functionality, shortcut = self.data_extracted[i+adder]

            self.nine_buttons[i].text = functionality
            new = make_it_plus(shortcut)
            # Fixed popup title not matching functionality chosen
            self.nine_popups[i].title = functionality  
            self.nine_popups[i].content.text = new

    def make_data(self):
        if self.heading_widget.text == 'Sublime Text':
            self.file_name = 'sublime-win.csv'
        elif self.heading_widget.text == 'VScode':
            self.file_name = 'vscode-win.csv'
        else:
            self.file_name = 'vim.csv'

        with open('./csv-files/' + self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                func = row[1]
                keys = row[0].split('+')
                self.data_extracted.append([func, keys])
        self.data_extracted.pop(0)

        for i in range(len(self.nine_buttons)):
            inside_box = BoxLayout()

            temp_button = self.nine_buttons[i]

            temp_button.background_color = [0, 0, 0, 0]
            temp_button.text = self.data_extracted[i][0]
            temp_button.halign = 'center'
            if len(temp_button.text) > 20:
                lol = temp_button.text[20:]
                x = lol.index(' ')
                given = 20 + x
                temp_button.text = temp_button.text[:given] + '\n' + temp_button.text[given:]

            temp_popup = self.nine_popups[i]
            temp_popup.size = (200, 300)
            shortcut = self.data_extracted[i][1]
            new = make_it_plus(shortcut)
            temp_popup.content = Label(text=new, font_size=18)
            temp_popup.title = temp_button.text
            temp_popup.size_hint = (None, None)

            inside_box.add_widget(Label(text=str(i+1)))
            inside_box.add_widget(Label())
            inside_box.add_widget(temp_button)
            inside_box.add_widget(Label())

            self.add_widget(inside_box)
