from kivy.app import App
from home_screen import HomePage
from kivy.uix.screenmanager import ScreenManager, Screen



class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_heading = None

    def build(self):

        self.screen_manager = ScreenManager()

        self.home_page = HomePage(main_app)
        screen = Screen(name='home')
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()

