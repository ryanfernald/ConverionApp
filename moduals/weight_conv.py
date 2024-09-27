#weight_conv.py

############ WEIGHT ############

# Metric Ton
def ton_to_kilogram(ton):
    return ton * 1000

def ton_to_gram(ton):
    return ton * 1_000_000

def ton_to_milligram(ton):
    return ton * 1_000_000_000

def ton_to_pound(ton):
    return ton * 2204.62

def ton_to_ounces(ton):
    return ton * 35_274

# Kilograms
def kilograms_to_ton(kilograms):
    return kilograms / 1000

def kilograms_to_gram(kilograms):
    return kilograms * 1000

def kilograms_to_milligram(kilograms):
    return kilograms * 1_000_000

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def kilograms_to_ounce(kilograms):
    return kilograms * 35.274

# Gram
def grams_to_ton(gram):
    return gram / 1_000_000

def grams_to_kilogram(gram):
    return gram / 1000

def grams_to_milligram(gram):
    return gram * 1000

def grams_to_pounds(gram):
    return gram * 0.00220462

def grams_to_ounce(gram):
    return gram * 0.035274

# Milligram
def miligrams_to_ton(miligram):
    return miligram / 1_000_000_000

def miligrams_to_kilogram(miligram):
    return miligram / 1_000_000

def miligrams_to_gram(miligram):
    return miligram / 1000

def miligrams_to_pounds(miligram):
    return miligram * 0.00000220462

def miligrams_to_ounce(miligram):
    return miligram * 0.000035274

# Pounds
def pounds_to_ton(pounds):
    return pounds / 2204.62

def pounds_to_kilogram(pounds):
    return pounds / 2.20462

def pounds_to_gram(pounds):
    return pounds * 453.592

def pounds_to_miligrams(pounds):
    return pounds * 453_592

def pounds_to_ounces(pounds):
    return pounds * 16

# Ounce
def ounce_to_tons(ounce):
    return ounce / 35_274

def ounce_to_kilogram(ounce):
    return ounce / 35.274

def ounce_to_grams(ounce):
    return ounce * 28.3495

def ounce_to_miligrams(ounce):
    return ounce * 28_349.5

def ounce_to_poounds(ounce):
    return ounce / 16