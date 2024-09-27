# conv_selector.py

from .metric_imperial_conv import kilometers_to_miles, miles_to_kilometers
from .temp_conv import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius

def convert(value, from_unit, to_unit):
    if from_unit == "Kilometers" and to_unit == "Miles":
        return kilometers_to_miles(value)
    elif from_unit == "Miles" and to_unit == "Kilometers":
        return miles_to_kilometers(value)
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return celsius_to_fahrenheit(value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return fahrenheit_to_celsius(value)
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return celsius_to_kelvin(value)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return kelvin_to_celsius(value)
    else:
        return "Conversion not supported."