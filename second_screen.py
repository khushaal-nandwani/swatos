from kivy.uix.boxlayout import BoxLayout

class SecondScreen(BoxLayout):
    def __init__(self, main_app, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.main_app = main_app

        heading = main_app.current_heading




