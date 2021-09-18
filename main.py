from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):

    def build(self):
        # I'm trying to make the boxes vertical.
        options = BoxLayout(orientation="vertical")

        # I'm trying to put some text in the boxes.
        # Currently not working. Can anyone more experienced show me?
        sublime = Label(text="sublime")
        options.add_widget(sublime)


if __name__ == '__main__':
    MainApp().run()


