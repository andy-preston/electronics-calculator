#!/usr/bin/python

import math

# TODO: This occurs in all calculators - should be in a module
def resistorValue(val):
    for letter, power in { 'M': 6, 'K': 3, 'R': 0 }.items():
        newVal = val.replace(letter, '.')
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
        if vout < voutWant and vout > voutMax:
            voutMax = vout
            resistor1use = resistor1
            resistor2use = resistor2
print vin, voutMax, resistor1use, resistor2use
