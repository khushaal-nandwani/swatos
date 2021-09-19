from kivy.app import App
from home_screen import HomePage
from second_screen import SecondScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config

Window.size = (350, 700)
Window.minimum_width, Window.minimum_height = Window.size
Window.maximum_width, Window.maximum_height = Window.size
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 0)
Config.set('graphics', 'window_state', 'hidden')


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_heading = None
        self.screen_list = []


    def build(self):
        self.screen_manager = ScreenManager()

        self.home_page = HomePage(main_app)
        screen = Screen(name='home')
        self.screen_list.append('home')
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        self.second_page = SecondScreen(main_app)
        screen = Screen(name='shortcuts')
        screen.add_widget(self.second_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager




if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()

