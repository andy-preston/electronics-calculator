#!/usr/bin/python

import math

# TODO: This occurs in all calculators - should be in a module
def resistorValue(val):
    for letter, power in { 'M': 6, 'K': 3, 'R': 0 }.items():
        if val.find('.') == -1:
            newVal = val.replace(letter, '.')
        else:
            newVal = val.replace(letter, '')
        if newVal != val:
            return float(newVal) * 10 ** power

resistors = [
    # www.bitsbox.co.uk 3W Carbon Film 5% Resistors
    '0R1', '0R15', '0R22', '0R33', '0R47',
    '2R2', '4R7', '18R', '33R', '47R', '56R',
    '100R', '120R', '150R', '180R', '220R', '330R', '470R', '560R',
    '1K', '1K5', '2K2', '4K7', '6K8', '10K', '12K', '22K', '47K'
]

existingResistors = [
    # what I've already got in stock
    '1K5', '4K7'
]

#resistors = [
#    # E. Bay 1W 1% resistors
#    '1R', '1.5K', '1.5M', '10R', '100R', '100K', '10K', '120R', '15R', '150R',
#    '150K', '15K', '180R', '180K', '1K', '1M', '2.2R', '2.2K', '22R', '220R',
#    '22K', '27R', '270R', '2M', '3.3K', '3.9K', '33R', '330R', '330K', '33K',
#    '39R', '390R', '39K', '4.7R', '4.7K', '47R', '470R', '470K', '47K',
#    '5.6R', '5.6K', '510R', '56R', '560K', '56K', '6.8K', '68R', '680R',
#    '680K', '68K', '7.5R', '7.5K', '75R', '75K', '8.2R', '8.2K', '82R',
#    '820R', '82K'
#]

# mean voltage in - measured by 3 different meters
vin = (49.0 + 48.6 + 48.8) / 3.0

# required voltage out
voutWant = 40

resistor1use = ''
resistor2use = ''
voutMax = 0

for resistor1 in resistors:
    R1 = resistorValue(resistor1)
    for resistor2 in existingResistors:
        R2 = resistorValue(resistor2)
        vout = (vin * R2) / (R1 + R2)
        if vout <= voutWant and vout > voutMax:
            voutMax = vout
            resistor1use = resistor1
            resistor2use = resistor2
print vin, voutMax, resistor1use, resistor2use
