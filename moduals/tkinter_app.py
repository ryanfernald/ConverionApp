import tkinter as tk
import platform

from moduals.conv_selector import convert

class ConversionApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversion App")

        self.categories = {
            "Distance": ["Kilometers", "Meters", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
            "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "Weight" : ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"],
            "Fluid Volume" : ["Liter", "Milliliter", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce", "Tablespoon", "Teaspoon"]
        }

        self.category_var = tk.StringVar(master)
        self.from_var = tk.StringVar(master)
        self.to_var = tk.StringVar(master)

        # Dropdown for category
        self.category_menu = tk.OptionMenu(master, self.category_var, *self.categories.keys(), command=self.update_units)
        self.category_menu.config(font=('Comfortaa', 14), width=15)
        self.category_menu.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Dropdowns for from and to units
        self.from_menu = tk.OptionMenu(master, self.from_var, "")
        self.from_menu.config(font=('Comfortaa', 14), width=15)
        self.from_menu.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(master, text="TO", font=('Comfortaa', 14)).grid(row=1, column=1, padx=10, pady=10)

        self.to_menu = tk.OptionMenu(master, self.to_var, "")
        self.to_menu.config(font=('Comfortaa', 14), width=15)
        self.to_menu.grid(row=1, column=2, padx=10, pady=10)

        # Input box
        self.input_value = tk.Entry(master, font=('Comfortaa', 14, "bold"), width=20)
        self.input_value.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Text
        self.result_label = tk.Label(master, text="Return to convert", font=('Comfortaa', 14, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.input_value.bind('<Return>', self.perform_conversion_with_enter)

       # Create a Checkbox for "Always on Top" feature
        self.topmost_var = tk.BooleanVar(value=True)
        self.topmost_checkbox = tk.Checkbutton(master, text="Float", font=('Comfortaa', 10),
                                               variable=self.topmost_var, command=self.toggle_topmost)
        self.topmost_checkbox.grid(row=5, column=2, sticky='e', padx=10, pady=10)

        # Create a Checkbox for "Auto Copy" feature
        self.auto_copy_var = tk.BooleanVar(value=False)
        self.auto_copy_checkbox = tk.Checkbutton(master, text="Auto Copy", font=('Comfortaa', 10),
                                                  variable=self.auto_copy_var)
        self.auto_copy_checkbox.grid(row=5, column=2, sticky='w', padx=10, pady=10)

        # Create a "Copy" button in grid row=5, column=1
        self.copy_button = tk.Button(master, text="Copy", font=('Comfortaa', 10), command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=1, padx=10, pady=10)

        # Set background color
        master.configure(bg="lavender")
        self.toggle_topmost()  # Set initial topmost state

        # Update immediately if running on macOS
        if platform.system() == 'Darwin':  # Mac-specific tweaks
            self.master.update_idletasks()

    def update_units(self, category):
        units = self.categories.get(category, [])
        self.from_var.set("")  # Clear current selection
        self.to_var.set("")

        self.from_menu['menu'].delete(0, 'end')
        self.to_menu['menu'].delete(0, 'end')

        for unit in units:
            self.from_menu['menu'].add_command(label=unit, command=tk._setit(self.from_var, unit))
            self.to_menu['menu'].add_command(label=unit, command=tk._setit(self.to_var, unit))

        # Force redraw/update if on macOS
        if platform.system() == 'Darwin':
            self.master.update_idletasks()

    def perform_conversion_with_enter(self, event):
        self.convert_and_clear_focus()

    def convert_and_clear_focus(self):
        try:
            value = float(self.input_value.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            self.result = convert(value, from_unit, to_unit)
            self.result_label.config(text=f"Result: {value} {from_unit}, is {self.result} {to_unit}")
            self.input_value.delete(0, tk.END)  # Clear input after conversion
            self.input_value.focus_set()  # Set focus back to input box

            if self.auto_copy_var.get():
                self.copy_to_clipboard()
            
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            self.input_value.focus_set()  # Ensure focus is on input box for new input
    
    def toggle_topmost(self):
        """Toggle the 'Always on Top' window attribute."""
        is_topmost = self.topmost_var.get()
        self.master.attributes('-topmost', is_topmost)

    # Method to copy the result to the clipboard
    def copy_to_clipboard(self):
        if self.result is not None:
            self.master.clipboard_clear()
            self.master.clipboard_append(str(self.result))
            self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversionApp(root)
    root.mainloop()