from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (550, 550)
Window.clearcolor = (0.98, 0.93, 0.89, 1)  

class TempApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=18)

        
        title = Label(
            text="TEMPERATURE CONVERTER!",
            font_size=34,
            bold=True,
            halign='center',
            color=(0.8, 0.2, 0.4, 1)
        )
        title.bind(size=title.setter('text_size'))
        self.layout.add_widget(title)

        
        input_row = BoxLayout(orientation='horizontal', spacing=12, size_hint_y=None, height=40)

        input_label = Label(
            text="Enter temperature:",
            font_size=15,
            color=(0.3, 0.3, 0.3, 1),
            size_hint=(0.5, 0.5),
            halign='right',
            valign='middle'
        )
        input_label.bind(size=input_label.setter('text_size'))

        self.temp_input = TextInput(
            multiline=False,
            font_size=14,
            padding=[10, 10]
        )

        input_row.add_widget(input_label)
        input_row.add_widget(self.temp_input)
        self.layout.add_widget(input_row)

        
        button_row = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=50)

        self.c2f_btn = Button(
            text="Celsius to Fahrenheit",
            background_color=(0.6, 0.8, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        self.f2c_btn = Button(
            text="Fahrenheit to Celsius",
            background_color=(0.6, 0.8, 0.7, 1),
            color=(1, 1, 1, 1)
        )

        self.c2f_btn.bind(on_press=self.convert_c2f)
        self.f2c_btn.bind(on_press=self.convert_f2c)

        button_row.add_widget(self.c2f_btn)
        button_row.add_widget(self.f2c_btn)
        self.layout.add_widget(button_row)

        
        self.result_label = Label(
            text="",
            font_size=26,
            bold=True,
            color=(0.4, 0.1, 0.4, 1),
            halign='center'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.layout.add_widget(self.result_label)

        
        self.endline = Label(
            text="",
            font_size=14,
            italic=True,
            color=(0.4, 0.4, 0.4, 1),
            halign='center'
        )
        self.endline.bind(size=self.endline.setter('text_size'))
        self.layout.add_widget(self.endline)

        return self.layout

    def highlight_button(self, active_button):
        self.c2f_btn.background_color = (0.6, 0.8, 0.7, 1)
        self.f2c_btn.background_color = (0.6, 0.8, 0.7, 1)
        active_button.background_color = (1, 0.8, 0.3, 1)

    def convert_c2f(self, instance):
        self.highlight_button(self.c2f_btn)
        try:
            value = float(self.temp_input.text)
            result = (value * 9/5) + 32
            self.result_label.text = f"{value}°C = {result:.2f}°F"
            self.endline.text = "The temperature is dressed up in Fahrenheit now!"
        except ValueError:
            self.result_label.text = ""
            self.endline.text = "Oops! Please enter a valid number."

    def convert_f2c(self, instance):
        self.highlight_button(self.f2c_btn)
        try:
            value = float(self.temp_input.text)
            result = (value - 32) * 5/9
            self.result_label.text = f"{value}°F = {result:.2f}°C"
            self.endline.text = "The Temperature is living its best Celsius life!"
        except ValueError:
            self.result_label.text = ""
            self.endline.text = "Oops! Please enter a valid number."

if __name__ == '__main__':
    TempApp().run()






# CODE LOGIC

'''

1. We import required Kivy modules:
   - App: Base class for creating the application.
   - BoxLayout: For vertically stacking our UI elements.
   - Label: To display text like titles, instructions, and results.
   - TextInput: To take user input for the temperature value.
   - Button: To create clickable options for conversion.
   - Window: To set the size and background color of the app window.

2. We configure the app window:
   - Set the window size to 550x550 and apply a peachy background using RGBA values.

3. We define a single class TempApp that inherits from App:
   - All layout creation and event handling is done inside this class.

4. In the build() method we:

   a. Create a vertical BoxLayout called 'layout' to hold all UI elements.

   b. Add a title Label:
      - Large, bold text saying "TEMPERATURE CONVERTER!".
      - Center-aligned using halign and text_size binding.

   c. Add an input row (horizontal BoxLayout):
      - A Label prompting "Enter temperature:".
      - A TextInput field beside it to accept numeric input.
      - The layout mimics a typical form input.

   d. Add a row of two buttons:
      - One labeled "Celsius to Fahrenheit".
      - One labeled "Fahrenheit to Celsius".
      - Both styled with mint green background and white text.
      - Both buttons are bound to their respective conversion functions.

   e. Add a result Label:
      - Displays the converted temperature result in large, bold font.

   f. Add a fun line Label:
      - Displays a quirky sentence after conversion or an error message if input is invalid.

5. The highlight_button() method:
   - Highlights whichever button was clicked by changing its background to yellow.
   - Resets the other button to mint green.

6. The method convert_c2f(instance):
   - Called when the "Celsius to Fahrenheit" button is clicked.
   - Reads the input, converts it using (value * 9/5) + 32.
   - Displays the result and a fun message.
   - Shows an error message if the input is not a valid number.

7. Define the method convert_f2c(instance):
   - Called when the "Fahrenheit to Celsius" button is clicked.
   - Converts the input using (value - 32) * 5/9.
   - Displays the result and a fun message.
   - Shows an error message if the input is not valid.

8. The app is run using TempApp().run():
   - This starts the Kivy event loop and displays the interface.

'''