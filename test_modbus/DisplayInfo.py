from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class DisplayScreen(GridLayout):
    def __init__(self, **kwargs):
        super(DisplayScreen, self).__init__(**kwargs)
        self.cols = 2

        self.LEDLabel = Label(text="Receive LED")
        self.LEDLabel.size_hint = (0.3, 1.0)
        self.add_widget(self.LEDLabel)
        self.LEDinfo = TextInput(multiline=True, readonly=True)
        self.add_widget(self.LEDinfo)

        self.ExpressionLabel = Label(text="Receive Expression")
        self.ExpressionLabel.size_hint = (0.3, 1.0)
        self.add_widget(self.ExpressionLabel)
        self.ExpressionInfo = TextInput( multiline=True, readonly=True)
        self.add_widget(self.ExpressionInfo)

        self.ActionLabel = Label(text="Receive Action")
        self.ActionLabel.size_hint = (0.3, 1.0)
        self.add_widget(self.ActionLabel)
        self.ActionInfo = TextInput( multiline=True, readonly=True)
        self.add_widget(self.ActionInfo)

        self.LEDinfo.text = "receive"


class ModBusDisplayApp(App):

    def build(self):
        return DisplayScreen()


if __name__ == '__main__':
    ModBusDisplayApp().run()
