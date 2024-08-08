from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):
    def flip(self):
        # a function for the "flip" icon
        # changes the state of the app
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.hint_text = "enter a decimal number"
            self.mode = "rectangle"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.hint_text = "enter a binary number"
            self.mode = "rectangle"
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""

    def convert(self, args):
        # a function to fint the decimal/binary equivallent
        if self.state == 0:
            # binary to decimal
            val = str(int(self.input.text,2))
            self.label.text = "in decimal is:"
        else:
            # decimal to binary
            val = bin(int(self.input.text))[2:]
            self.label.text = "in binary is:"
        self.converted.text = val

    def build(self):
        self.state = 0 #initial state
        #self.theme_cls.primary_palette = "DeepOrange"
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)


        # logo
        screen.add_widget(Image(
            source="img.jpg",
            pos_hint = {"center_x": 0.5, "center_y":0.65},
            size_hint = (0.45,0.45)
            ))

        #collect user input
        self.input = MDTextField(
            hint_text="enter a binary number",
            mode ="rectangle",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.4},
            font_size = 22
        )
        screen.add_widget(self.input)

        #secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.25},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.20},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y":0.10},
            on_press = self.convert
        ))

        return screen

if __name__ == '__main__':
    ConverterApp().run()