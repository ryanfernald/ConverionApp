import tkinter as tk
from moduals.conv_selector import convert

class ConversionApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversion App")

        # Dropdown menus
        self.from_var = tk.StringVar(master)
        self.to_var = tk.StringVar(master)

        # Sample options for conversion
        self.options = ["Kilometers", "Meters", "Centimeters", "Millimeters","Miles", "Yards", "Feet", "Inches", "Celsius", "Fahrenheit", "Kelvin"]

        # Grid layout for dropdown menus
        self.from_menu = tk.OptionMenu(master, self.from_var, *self.options)
        self.from_menu.config(font=('Comfortaa', 14), width=15)
        self.from_menu.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(master, text="TO", font=('Comfortaa', 14)).grid(row=0, column=1, padx=10, pady=10)

        self.to_menu = tk.OptionMenu(master, self.to_var, *self.options)
        self.to_menu.config(font=('Comfortaa', 14), width=15)
        self.to_menu.grid(row=0, column=2, padx=10, pady=10)

        # Input text box
        self.input_value = tk.Entry(master, font=('Comfortaa', 14, "bold"), width=20)
        self.input_value.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Return to Convert label
        self.return_label = tk.Label(master, text="Return to Convert", font=('Comfortaa', 14))
        self.return_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Result label
        self.result_label = tk.Label(master, text="", font=('Comfortaa', 14, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Bind the Enter key to perform conversion
        self.input_value.bind('<Return>', self.perform_conversion_with_enter)

    def perform_conversion_with_enter(self, event):
        self.convert_and_clear_focus()

    def convert_and_clear_focus(self):
        try:
            value = float(self.input_value.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            result = convert(value, from_unit, to_unit)
            self.result_label.config(text=f"Result: {value} {from_unit}, is {result:.5f} {to_unit}")
            self.input_value.delete(0, tk.END)  # Clear input after conversion
            self.input_value.focus_set()  # Set focus back to input box
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            self.input_value.focus_set()  # Ensure focus is on input box for new input

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversionApp(root)
    root.mainloop()