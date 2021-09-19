from kivy.app import App
from home_screen import HomePage
from second_screen import SecondScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (300, 700)


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: the self.current heading should be assigned a string which is
        #  the software which the user choses to see the shortcut of, after
        #  selecting the one
        self.current_heading = None

    def build(self):

        self.screen_manager = ScreenManager()

        # self.home_page = HomePage(main_app)
        # screen = Screen(name='home')
        # screen.add_widget(self.home_page)
        # self.screen_manager.add_widget(screen)

        self.second_page = SecondScreen(main_app)
        self.second_page.extract_data()
        self.second_page.add_data()
        screen = Screen(name='shortcuts')
        screen.add_widget(self.second_page)
        self.screen_manager.add_widget(screen)


        return self.screen_manager


if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()

