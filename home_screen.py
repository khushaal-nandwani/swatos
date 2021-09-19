from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from functools import partial
from kivy.core.window import Window

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)
PURPLE = (1, 0, 1, 1)



class HomePage(BoxLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # you may ignore this for now, will be used later
        self.main_app = main_app

        instruction = Label(text="Click on the Editor Icon you are using", bold=True, font_size=17)
        self.add_widget(instruction)

        # Here are the options for screen 1. We can add some more.
        option_names = ["Sublime Text", "VScode", "Vim"]
        option_images = ["sublime_text_logo.png", "vscode_logo.png",
                         "vim_logo.png"]

        self.options = []

        # Displaying choices and logos and making buttons for each option.
        for i in range(len(option_names)):
            option_box = self.make_option(str(i + 1), option_names[i],
                                     option_images[i])
            self.options.append(option_box)
            self.add_widget(option_box)

        self.main_app = main_app

    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None

    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 's':
    #         print('I can feel it')
    #         self.options[0].button.click()
    #     elif keycode[1] == 'q':
    #         self.options[1].button.click()
    #     elif keycode[1] == 'r':
    #         self.options[2].button.click()
    #     return True

    def make_option(self, idx, option_text, img_name):
        """You make a horizontal-direction BoxLayout for each text
        editor keyboard shortcut option."""

        # You go horizontal: number, then text, then image
        option = BoxLayout(orientation="horizontal")
        option.padding = 20

        # Setting the number, text, and image
        option_number = Button(text=idx)
        option_number.background_color = [0, 0, 0, 0]
        option_text = Label(text=option_text)
        # option_img = Image(source="./logos/" + img_name, allow_stretch=True)
        option_img = Button(background_normal="./logos/" + img_name,
                            size_hint_y=None,
                            size_hint_x=0.5,
                            pos_hint = {"x":0.35, "y":0.3})

        option_img.bind(on_press=partial(self.change_screen, option_text.text))

        option.button = option_number

        option.add_widget(option_text)
        option.add_widget(option_img)

        return option

    def change_screen(self, software_name, widget):

        self.main_app.second_page.heading_widget.text = software_name
        self.main_app.second_page.make_data()
        self.main_app.second_page.add_data()
        self.main_app.screen_manager.current = "shortcuts"
        self.main_app.screen_list.append('shortcuts')




