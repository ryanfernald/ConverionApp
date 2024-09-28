# conv_selector.py

from .metric_imperial_conv import *
from .temp_conv import *
from .weight_conv import *
from .volume_conv import *

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

    ################################################################################
    ################################# Temperature ##################################
    ################################################################################

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

# Metric Ton
    elif from_unit == "Tons" and to_unit == "Kilograms":
        return ton_to_kilogram(value)
    elif from_unit == "Tons" and to_unit == "Grams":
        return ton_to_gram(value)
    elif from_unit == "Tons" and to_unit == "Milligrams":
        return ton_to_milligram(value)
    elif from_unit == "Tons" and to_unit == "Pounds":
        return ton_to_pound(value)
    elif from_unit == "Tons" and to_unit == "Ounces":
        return ton_to_ounces(value)

# Kilograms
    elif from_unit == "Kilograms" and to_unit == "Tons":
        return kilograms_to_ton(value)
    elif from_unit == "Kilograms" and to_unit == "Grams":
        return kilograms_to_gram(value)
    elif from_unit == "Kilograms" and to_unit == "Milligrams":
        return kilograms_to_milligram(value)
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        return kilograms_to_pounds(value)
    elif from_unit == "Kilograms" and to_unit == "Ounces":
        return kilograms_to_ounce(value)

# Grams
    elif from_unit == "Grams" and to_unit == "Tons":
        return grams_to_ton(value)
    elif from_unit == "Grams" and to_unit == "Kilograms":
        return grams_to_kilogram(value)
    elif from_unit == "Grams" and to_unit == "Milligrams":
        return grams_to_milligram(value)
    elif from_unit == "Grams" and to_unit == "Pounds":
        return grams_to_pounds(value)
    elif from_unit == "Grams" and to_unit == "Ounces":
        return grams_to_ounce(value)

# Milligrams
    elif from_unit == "Milligrams" and to_unit == "Tons":
        return miligrams_to_ton(value)
    elif from_unit == "Milligrams" and to_unit == "Kilograms":
        return miligrams_to_kilogram(value)
    elif from_unit == "Milligrams" and to_unit == "Grams":
        return miligrams_to_gram(value)
    elif from_unit == "Milligrams" and to_unit == "Pounds":
        return miligrams_to_pounds(value)
    elif from_unit == "Milligrams" and to_unit == "Ounces":
        return miligrams_to_ounce(value)

# Pounds
    elif from_unit == "Pounds" and to_unit == "Tons":
        return pounds_to_ton(value)
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return pounds_to_kilogram(value)
    elif from_unit == "Pounds" and to_unit == "Grams":
        return pounds_to_gram(value)
    elif from_unit == "Pounds" and to_unit == "Milligrams":
        return pounds_to_miligrams(value)
    elif from_unit == "Pounds" and to_unit == "Ounces":
        return pounds_to_ounces(value)

# Ounces
    elif from_unit == "Ounces" and to_unit == "Tons":
        return ounce_to_tons(value)
    elif from_unit == "Ounces" and to_unit == "Kilograms":
        return ounce_to_kilogram(value)
    elif from_unit == "Ounces" and to_unit == "Grams":
        return ounce_to_grams(value)
    elif from_unit == "Ounces" and to_unit == "Milligrams":
        return ounce_to_miligrams(value)
    elif from_unit == "Ounces" and to_unit == "Pounds":
        return ounce_to_poounds(value)
    
    ################################################################################
    ############################## Fluid Volume ####################################
    ################################################################################
    
# Liter to conversions
    elif from_unit == "Liter" and to_unit == "Milliliter":
        return liter_to_millileter(value)
    elif from_unit == "Liter" and to_unit == "Gallon":
        return liter_to_gallon(value)
    elif from_unit == "Liter" and to_unit == "Quart":
        return liter_to_quart(value)
    elif from_unit == "Liter" and to_unit == "Pint":
        return liter_to_pint(value)
    elif from_unit == "Liter" and to_unit == "Cup":
        return liter_to_cup(value)
    elif from_unit == "Liter" and to_unit == "Fluid Ounce":
        return liter_to_floz(value)
    elif from_unit == "Liter" and to_unit == "Tablespoon":
        return liter_to_tbsp(value)
    elif from_unit == "Liter" and to_unit == "Teaspoon":
        return liter_to_tsp(value)
    
# Milliliter to conversions
    elif from_unit == "Milliliter" and to_unit == "Liter":
        return milliliter_to_liter(value)
    elif from_unit == "Milliliter" and to_unit == "Gallon":
        return milliliter_to_gallon(value)
    elif from_unit == "Milliliter" and to_unit == "Quart":
        return milliliter_to_quart(value)
    elif from_unit == "Milliliter" and to_unit == "Pint":
        return milliliter_to_pint(value)
    elif from_unit == "Milliliter" and to_unit == "Cup":
        return milliliter_to_cup(value)
    elif from_unit == "Milliliter" and to_unit == "Fluid Ounce":
        return milliliter_to_floz(value)
    elif from_unit == "Milliliter" and to_unit == "Tablespoon":
        return milliliter_to_tbsp(value)
    elif from_unit == "Milliliter" and to_unit == "Teaspoon":
        return milliliter_to_tsp(value)
    
# Gallon to conversions
    elif from_unit == "Gallon" and to_unit == "Liter":
        return gallon_to_liter(value)
    elif from_unit == "Gallon" and to_unit == "Milliliter":
        return gallon_to_milliliter(value)
    elif from_unit == "Gallon" and to_unit == "Quart":
        return gallon_to_quart(value)
    elif from_unit == "Gallon" and to_unit == "Pint":
        return gallon_to_pint(value)
    elif from_unit == "Gallon" and to_unit == "Cup":
        return gallon_to_cup(value)
    elif from_unit == "Gallon" and to_unit == "Fluid Ounce":
        return gallon_to_floz(value)
    elif from_unit == "Gallon" and to_unit == "Tablespoon":
        return gallon_to_tbsp(value)
    elif from_unit == "Gallon" and to_unit == "Teaspoon":
        return gallon_to_tsp(value)
    
# Quart to conversions
    elif from_unit == "Quart" and to_unit == "Liter":
        return quart_to_liter(value)
    elif from_unit == "Quart" and to_unit == "Milliliter":
        return quart_to_milliliter(value)
    elif from_unit == "Quart" and to_unit == "Gallon":
        return quart_to_gallon(value)
    elif from_unit == "Quart" and to_unit == "Pint":
        return quart_to_pint(value)
    elif from_unit == "Quart" and to_unit == "Cup":
        return quart_to_cup(value)
    elif from_unit == "Quart" and to_unit == "Fluid Ounce":
        return quart_to_floz(value)
    elif from_unit == "Quart" and to_unit == "Tablespoon":
        return quart_to_tbsp(value)
    elif from_unit == "Quart" and to_unit == "Teaspoon":
        return quart_to_tsp(value)

# Pint to conversions
    elif from_unit == "Pint" and to_unit == "Liter":
        return pint_to_liter(value)
    elif from_unit == "Pint" and to_unit == "Milliliter":
        return pint_to_milliliter(value)
    elif from_unit == "Pint" and to_unit == "Gallon":
        return pint_to_gallon(value)
    elif from_unit == "Pint" and to_unit == "Quart":
        return pint_to_quart(value)
    elif from_unit == "Pint" and to_unit == "Cup":
        return pint_to_cup(value)
    elif from_unit == "Pint" and to_unit == "Fluid Ounce":
        return pint_to_floz(value)
    elif from_unit == "Pint" and to_unit == "Tablespoon":
        return pint_to_tbsp(value)
    elif from_unit == "Pint" and to_unit == "Teaspoon":
        return pint_to_tsp(value)

# Cup to conversions
    elif from_unit == "Cup" and to_unit == "Liter":
        return cup_to_liter(value)
    elif from_unit == "Cup" and to_unit == "Milliliter":
        return cup_to_milliliter(value)
    elif from_unit == "Cup" and to_unit == "Gallon":
        return cup_to_gallon(value)
    elif from_unit == "Cup" and to_unit == "Quart":
        return cup_to_quart(value)
    elif from_unit == "Cup" and to_unit == "Pint":
        return cup_to_pint(value)
    elif from_unit == "Cup" and to_unit == "Fluid Ounce":
        return cup_to_floz(value)
    elif from_unit == "Cup" and to_unit == "Tablespoon":
        return cup_to_tbsp(value)
    elif from_unit == "Cup" and to_unit == "Teaspoon":
        return cup_to_tsp(value)

# Fluid Ounce (floz) to conversions
    elif from_unit == "Fluid Ounce" and to_unit == "Liter":
        return floz_to_liter(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Milliliter":
        return floz_to_milliliter(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Gallon":
        return floz_to_gallon(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Quart":
        return floz_to_quart(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Pint":
        return floz_to_pint(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Cup":
        return floz_to_cup(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Tablespoon":
        return floz_to_tbsp(value)
    elif from_unit == "Fluid Ounce" and to_unit == "Teaspoon":
        return floz_to_tsp(value)

# Tablespoon (tbsp) to conversions
    elif from_unit == "Tablespoon" and to_unit == "Liter":
        return tbsp_to_liter(value)
    elif from_unit == "Tablespoon" and to_unit == "Milliliter":
        return tbsp_to_milliliter(value)
    elif from_unit == "Tablespoon" and to_unit == "Gallon":
        return tbsp_to_gallon(value)
    elif from_unit == "Tablespoon" and to_unit == "Quart":
        return tbsp_to_quart(value)
    elif from_unit == "Tablespoon" and to_unit == "Pint":
        return tbsp_to_pint(value)
    elif from_unit == "Tablespoon" and to_unit == "Cup":
        return tbsp_to_cup(value)
    elif from_unit == "Tablespoon" and to_unit == "Fluid Ounce":
        return tbsp_to_floz(value)
    elif from_unit == "Tablespoon" and to_unit == "Teaspoon":
        return tbsp_to_tsp(value)

# Teaspoon (tsp) to conversions
    elif from_unit == "Teaspoon" and to_unit == "Liter":
        return tsp_to_liter(value)
    elif from_unit == "Teaspoon" and to_unit == "Milliliter":
        return tsp_to_milliliter(value)
    elif from_unit == "Teaspoon" and to_unit == "Gallon":
        return tsp_to_gallon(value)
    elif from_unit == "Teaspoon" and to_unit == "Quart":
        return tsp_to_quart(value)
    elif from_unit == "Teaspoon" and to_unit == "Pint":
        return tsp_to_pint(value)
    elif from_unit == "Teaspoon" and to_unit == "Cup":
        return tsp_to_cup(value)
    elif from_unit == "Teaspoon" and to_unit == "Fluid Ounce":
        return tsp_to_floz(value)
    elif from_unit == "Teaspoon" and to_unit == "Tablespoon":
        return tsp_to_tbsp(value)
    
    else:
        return "Conversion not supported."
