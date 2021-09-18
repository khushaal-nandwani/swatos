from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)
PURPLE = (1, 0, 1, 1)

def make_option(idx, option_text, img_name):
    """You make a horizontal-direction BoxLayout for each text
    editor keyboard shortcut option."""
    option = BoxLayout(orientation="horizontal")
    option.padding = 20

    option_number = Label(text=idx)
    option_text = Label(text=option_text)
    option_img = Image(source="./logos/" + img_name, allow_stretch=True)

    option.add_widget(option_number)
    option.add_widget(option_text)
    option.add_widget(option_img)

    return option

class HomePage(BoxLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # you may ignore this for now, will be used later
        self.main_app = main_app

        instruction = Label(text="Select the software you are using.")
        self.add_widget(instruction)

        option_names = ["sublime", "vscode", "vim"]
        option_images = ["sublime_text_logo.png", "vscode_logo.png", "vim_logo.png"]

        for i in range(len(option_names)):
            # And for each option, you go horizontal, text then image
            option_box = make_option(str(i + 1), option_names[i], option_images[i])
            self.add_widget(option_box)

        self.main_app = main_app




