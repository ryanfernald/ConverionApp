# conv_selector.py

from .metric_imperial_conv import *
from .temp_conv import *
from .weight_conv import *

def convert(value, from_unit, to_unit):

    ################################################################################
    #################################### Distance ##################################
    ################################################################################

    # Kilometers conversions
    if from_unit == "Kilometers" and to_unit == "Meters":
        return kilometers_to_meters(value)
    elif from_unit == "Kilometers" and to_unit == "Centimeters":
        return kilometers_to_centimeters(value)
    elif from_unit == "Kilometers" and to_unit == "Millimeters":
        return kilometers_to_millimeters(value)
    elif from_unit == "Kilometers" and to_unit == "Miles":
        return kilometers_to_miles(value)
    elif from_unit == "Kilometers" and to_unit == "Yards":
        return kilometers_to_yards(value)
    elif from_unit == "Kilometers" and to_unit == "Feet":
        return kilometers_to_feet(value)
    elif from_unit == "Kilometers" and to_unit == "Inches":
        return kilometers_to_inches(value)

    # Meters conversions
    elif from_unit == "Meters" and to_unit == "Kilometers":
        return meters_to_kilometers(value)
    elif from_unit == "Meters" and to_unit == "Centimeters":
        return meters_to_centimeters(value)
    elif from_unit == "Meters" and to_unit == "Millimeters":
        return meters_to_millimeters(value)
    elif from_unit == "Meters" and to_unit == "Miles":
        return meters_to_miles(value)
    elif from_unit == "Meters" and to_unit == "Yards":
        return meters_to_yards(value)
    elif from_unit == "Meters" and to_unit == "Feet":
        return meters_to_feet(value)
    elif from_unit == "Meters" and to_unit == "Inches":
        return meters_to_inches(value)

    # Centimeters conversions
    elif from_unit == "Centimeters" and to_unit == "Kilometers":
        return centimeters_to_kilometers(value)
    elif from_unit == "Centimeters" and to_unit == "Meters":
        return centimeters_to_meters(value)
    elif from_unit == "Centimeters" and to_unit == "Millimeters":
        return centimeters_to_millimeters(value)
    elif from_unit == "Centimeters" and to_unit == "Miles":
        return centimeters_to_miles(value)
    elif from_unit == "Centimeters" and to_unit == "Yards":
        return centimeters_to_yards(value)
    elif from_unit == "Centimeters" and to_unit == "Feet":
        return centimeters_to_feet(value)
    elif from_unit == "Centimeters" and to_unit == "Inches":
        return centimeters_to_inches(value)

    # Millimeters conversions
    elif from_unit == "Millimeters" and to_unit == "Kilometers":
        return millimeters_to_kilometers(value)
    elif from_unit == "Millimeters" and to_unit == "Meters":
        return millimeters_to_meters(value)
    elif from_unit == "Millimeters" and to_unit == "Centimeters":
        return millimeters_to_centimeters(value)
    elif from_unit == "Millimeters" and to_unit == "Miles":
        return millimeters_to_miles(value)
    elif from_unit == "Millimeters" and to_unit == "Yards":
        return millimeters_to_yards(value)
    elif from_unit == "Millimeters" and to_unit == "Feet":
        return millimeters_to_feet(value)
    elif from_unit == "Millimeters" and to_unit == "Inches":
        return millimeters_to_inches(value)

    # Miles conversions
    elif from_unit == "Miles" and to_unit == "Kilometers":
        return miles_to_kilometers(value)
    elif from_unit == "Miles" and to_unit == "Meters":
        return miles_to_meters(value)
    elif from_unit == "Miles" and to_unit == "Centimeters":
        return miles_to_centimeters(value)
    elif from_unit == "Miles" and to_unit == "Millimeters":
        return miles_to_millimeters(value)
    elif from_unit == "Miles" and to_unit == "Yards":
        return miles_to_yards(value)
    elif from_unit == "Miles" and to_unit == "Feet":
        return miles_to_feet(value)
    elif from_unit == "Miles" and to_unit == "Inches":
        return miles_to_inches(value)

    # Yards conversions
    elif from_unit == "Yards" and to_unit == "Kilometers":
        return yards_to_kilometers(value)
    elif from_unit == "Yards" and to_unit == "Meters":
        return yards_to_meters(value)
    elif from_unit == "Yards" and to_unit == "Centimeters":
        return yards_to_centimeters(value)
    elif from_unit == "Yards" and to_unit == "Millimeters":
        return yards_to_millimeters(value)
    elif from_unit == "Yards" and to_unit == "Miles":
        return yards_to_miles(value)
    elif from_unit == "Yards" and to_unit == "Feet":
        return yards_to_feet(value)
    elif from_unit == "Yards" and to_unit == "Inches":
        return yards_to_inches(value)

    # Feet conversions
    elif from_unit == "Feet" and to_unit == "Kilometers":
        return feet_to_kilometers(value)
    elif from_unit == "Feet" and to_unit == "Meters":
        return feet_to_meters(value)
    elif from_unit == "Feet" and to_unit == "Centimeters":
        return feet_to_centimeters(value)
    elif from_unit == "Feet" and to_unit == "Millimeters":
        return feet_to_millimeters(value)
    elif from_unit == "Feet" and to_unit == "Miles":
        return feet_to_miles(value)
    elif from_unit == "Feet" and to_unit == "Yards":
        return feet_to_yards(value)
    elif from_unit == "Feet" and to_unit == "Inches":
        return feet_to_inches(value)

    # Inches conversions
    elif from_unit == "Inches" and to_unit == "Kilometers":
        return inches_to_kilometers(value)
    elif from_unit == "Inches" and to_unit == "Meters":
        return inches_to_meters(value)
    elif from_unit == "Inches" and to_unit == "Centimeters":
        return inches_to_centimeters(value)
    elif from_unit == "Inches" and to_unit == "Millimeters":
        return inches_to_millimeters(value)
    elif from_unit == "Inches" and to_unit == "Miles":
        return inches_to_miles(value)
    elif from_unit == "Inches" and to_unit == "Yards":
        return inches_to_yards(value)
    elif from_unit == "Inches" and to_unit == "Feet":
        return inches_to_feet(value)

    # Temperature conversions (already provided)
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return celsius_to_fahrenheit(value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return fahrenheit_to_celsius(value)
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return celsius_to_kelvin(value)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return kelvin_to_celsius(value)
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return kelvin_to_celsius(value)
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return kelvin_to_celsius(value)

    ################################################################################
    #################################### Weight ####################################
    ################################################################################

    # Kilograms
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        return kilograms_to_pounds(value)
    
    # Pounds 
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return pounds_to_kilograms(value)
    
    else:
        return "Conversion not supported."
