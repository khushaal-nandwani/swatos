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

        heading_widget = Label(text="Sublime Text")
        self.add_widget(heading_widget)


        self.popup1 = Popup(Title="the shortcut", auto_dismiss=False)
        self.popup2 = Popup(Title="the shortcut")
        self.popup3 = Popup(Title="the shortcut")
        self.popup4 = Popup(Title="the shortcut")
        self.popup5 = Popup(Title="the shortcut")
        self.popup6 = Popup(Title="the shortcut")
        self.popup7 = Popup(Title="the shortcut")
        self.popup8 = Popup(Title="the shortcut")
        self.popup9 = Popup(Title="the shortcut")

        self.button1 = Button(text='First')
        self.button2 = Button(text='Second')
        self.button3 = Button(text='Third')
        self.button4 = Button(text='Fourth')
        self.button5 = Button(text='Five')
        self.button6 = Button(text='Six')
        self.button7 = Button(text='Seven')
        self.button8 = Button(text='Huit')
        self.button9 = Button(text='Nine')

        self.nine_button = [self.button1,
                            self.button2,
                            self.button3,
                            self.button4,
                            self.button5,
                            self.button6,
                            self.button7,
                            self.button8,
                            self.button9]

        self.nine_popups = [self.popup1,
                            self.popup2,
                            self.popup3,
                            self.popup4,
                            self.popup5,
                            self.popup6,
                            self.popup7,
                            self.popup8,
                            self.popup9]


    data_extracted =  [
        ['New Window/Instance', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance1', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance2', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance3', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance4', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance5', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance6', ['Ctrl', 'Shift', 'N']],
        ['New Window/Instance7', ['Ctrl', 'Shift', 'N']],
                        ]

    def extract_data(self):
        """Fetches data from the csv and assigns it
         to <data_extracted> dict"""
        # TODO: Complete this function

    def add_data(self):
        adder = self.scroll * 9
        index = 0 + adder
        for i in range(9):
            index += i
            temp_button = self.nine_button[index]
            temp_button.text = self.data_extracted[index][0]
            temp_popup = self.nine_popups[index]
            temp_popup.title = str(self.data_extracted[index][1])
            # put data into button and its popup








