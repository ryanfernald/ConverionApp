# __init__.py

from .conv_selector import *
from .metric_imperial_conv import *
from .temp_conv import *
from .weight_conv import *

__all__ = [

    "convert_units",

    #distance
    "kilometers_to_meters",
    "kilometers_to_centimeters",
    "kilometers_to_millimeters",
    "kilometers_to_miles",
    "kilometers_to_yards",
    "kilometers_to_feet",
    "kilometers_to_inches",

    "meters_to_kilometers",
    "meters_to_centimeters",
    "meters_to_millimeters",
    "meters_to_miles",
    "meters_to_yards",
    "meters_to_feet",
    "meters_to_inches",

    "centimeters_to_kilometers",
    "centimeters_to_meters",
    "centimeters_to_millimeters",
    "centimeters_to_miles",
    "centimeters_to_yards",
    "centimeters_to_feet",
    "centimeters_to_inches",

    "millimeters_to_kilometers",
    "millimeters_to_meters",
    "millimeters_to_centimeters",
    "millimeters_to_miles",
    "millimeters_to_yards",
    "millimeters_to_feet",
    "millimeters_to_inches",

    "miles_to_kilometers",
    "miles_to_meters",
    "miles_to_centimeters",
    "miles_to_millimeters",
    "miles_to_yards",
    "miles_to_feet",
    "miles_to_inches",

    "yards_to_kilometers",
    "yards_to_meters",
    "yards_to_centimeters",
    "yards_to_millimeters",
    "yards_to_miles",
    "yards_to_feet",
    "yards_to_inches",

    "feet_to_kilometers",
    "feet_to_meters",
    "feet_to_centimeters",
    "feet_to_millimeters",
    "feet_to_miles",
    "feet_to_yards",
    "feet_to_inches",

    "inches_to_kilometers",
    "inches_to_meters",
    "inches_to_centimeters",
    "inches_to_millimeters",
    "inches_to_miles",
    "inches_to_yards",
    "inches_to_feet",
    
    #temperature
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "celsius_to_kelvin",
    "kelvin_to_celsius",
    "fahrenheit_to_kelvin",
    "kelvin_to_fahrenheit",

    #weight
    "ton_to_kilogram",
    "ton_to_gram",
    "ton_to_milligram",
    "ton_to_pound",
    "ton_to_ounces",

    "kilograms_to_ton",
    "kilograms_to_gram",
    "kilograms_to_milligram",
    "kilograms_to_pounds",
    "kilograms_to_ounce",

    "grams_to_ton",
    "grams_to_kilogram",
    "grams_to_milligram",
    "grams_to_pounds",
    "grams_to_ounce",

    "miligrams_to_ton",
    "miligrams_to_kilogram",
    "miligrams_to_gram",
    "miligrams_to_pounds",
    "miligrams_to_ounce",

    "pounds_to_ton",
    "pounds_to_kilogram",
    "pounds_to_gram",
    "pounds_to_miligrams",
    "pounds_to_ounces",

    "ounce_to_tons",
    "ounce_to_kilogram",
    "ounce_to_grams",
    "ounce_to_miligrams",
    "ounce_to_poounds"

]

