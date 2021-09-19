from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class SecondScreen(BoxLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.main_app = main_app
        self.scroll = 0
        heading = main_app.current_heading
        self.current_popup_number = None
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)



        heading_widget = Label(text="Sublime Text")
        self.add_widget(heading_widget)

        self.data_extracted = [
            ['New Window/Instance', ['Ctrl', 'Shift', '1']],
            ['New Window/Instance1', ['Ctrl', 'Shift', '2']],
            ['New Window/Instance2', ['Ctrl', 'Shift', '3']],
            ['New Window/Instance3', ['Ctrl', 'Shift', '4']],
            ['New Window/Instance4', ['Ctrl', 'Shift', '5']],
            ['New Window/Instance5', ['Ctrl', 'Shift', '6']],
            ['New Window/Instance6', ['Ctrl', 'Shift', '7']],
            ['New Window/Instance7', ['Ctrl', 'Shift', '8']],
            ['New Window/Instance8', ['Ctrl', 'Shift', '9']],
        ]



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

        for i in range(len(self.nine_buttons) - 1):
            inside_box = BoxLayout()
            temp_button = self.nine_buttons[i]
            temp_button.background_color = [0,0,0,0]
            temp_button.text = self.data_extracted[i][0]
            temp_popup = self.nine_popups[i]
            temp_popup.size = (200, 500)
            temp_popup.content = Label(text=str(self.data_extracted[i][1]))
            temp_popup.size_hint = (None, None)
            # bind the on_press event of the button to the dismiss function
            # temp_button.bind(on_press=temp_popup.open)
            inside_box.add_widget(Label(text=str(i+1)))
            inside_box.add_widget(temp_button)
            inside_box.add_widget(Label())
            self.add_widget(inside_box)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ('escape', str(self.current_popup_number)):
            if self.current_popup_number is not None:
                self.nine_popups[self.current_popup_number].dismiss()

        codes = [x + 1 for x in range(9)]
        for k in codes:
            if keycode[1] == str(k):
                self.nine_popups[k].open()
                self.current_popup_number = k
        return True



    def extract_data(self):
        """Fetches data from the csv and assigns it
         to <self.data_extracted> dict"""
        # TODO: Complete this function
        return None

    def add_data(self):
        adder = self.scroll * 9
        index = 0 + adder
        return None








