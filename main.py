from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)
PURPLE = (1, 0, 1, 1)

def make_option(option_text):
    """You make a horizontal-direction BoxLayout for each text
editor keyboard shortcut option."""
    option = BoxLayout(orientation="horizontal")
    option_text = Label(text=option_text)
    option.add_widget(option_text)
    return option

class MainApp(App):

    def build(self):
        # I'm trying to make the options go vertical
        options = BoxLayout(orientation="vertical")

        # And for each option, you go horizontal, text then image
        sublime = make_option("sublime")
        vscode = make_option("vscode")
        vim = make_option("vim")

        options.add_widget(sublime)
        options.add_widget(vscode)
        options.add_widget(vim)

        return options

if __name__ == '__main__':
    MainApp().run()

