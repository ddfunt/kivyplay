from kivy.app import App
from kivy.uix.widget import Widget


class MainScreen(Widget):
    pass


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
