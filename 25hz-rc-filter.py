#!/usr/bin/python

import math

def resistorValue(val):
    for letter, power in { 'M': 6, 'K': 3, 'R': 0 }.items():
        newVal = val.replace(letter, '.')
        if newVal != val:
            return float(newVal) * 10 ** power

def capacitorValue(val):
    for letter, power in { 'p': -12, 'n': -9, 'u': -6 }.items():
        newVal = val.replace(letter + 'F', '')
        if newVal != val:
            return float(newVal) * 10 ** power

resistors = [
    # www.bitsbox.co.uk 1/4W Carbon Film 5% Resistors
    '0R', '1R', '1R5', '1R8', '2R2', '3R3', '4R7', '5R6', '6R8', '8R2',
    '10R', '12R', '15R', '18R', '22R', '33R', '47R', '56R', '68R', '82R',
    '100R', '120R', '150R', '180R',
    '220R', '240R', '270R', '330R', '390R', '470R', '560R', '680R', '820R',
    '1K', '1K2', '1K5', '1K8',
    '2K2', '2K4', '2K7', '3K3', '3K9', '4K7', '5K6', '6K8', '8K2',
    '10K', '12K', '15K', '18K',
    '22K', '24K', '27K', '33K', '39K', '47K', '56K', '68K', '82K',
    '100K', '120K', '150K', '180K',
    '220K', '240K', '270K', '330K', '390K', '470K', '560K', '680K', '820K',
    '1M', '1M2', '1M5', '1M8',
    '2M2', '2M4', '2M7', '3M3', '3M9', '4M7', '5M6', '6M8', '8M2', '10M'
]

capacitors = [
    # www.bitsbox.co.uk Ceramic Disc Capacitors
    '1pF', '2.2pF', '2.7pF', '3.3pF', '4.7pF', '5pF', '6.8pF',
    '10pF', '15pF', '18pF',
    '22pF', '25pF', '27pF', '33pF', '47pF', '50pF', '68pF',
    '100pF', '150pF',
    '220pF', '330pF', '390pF', '470pF', '500pF', '560pF', '680pF', '820pF',
    '1000pF', '1500pF', '1800pF',
    '2200pF', '2700pF', '3300pF', '3900pF', '4700pF', '6800pF',
    '10nF', '15nF',
    '22nF', '33nF', '47nF', '100nF', '220nF',
    # www.bitsbox.co.uk 85deg Electrolytic Capacitors (skipping voltage ratings)
    '0.1uF', '0.22uF', '0.47uF', '1uF', '2.2uF', '3.3uF', '4.7uF',
    '10uF', '22uF', '33uF', '47uF',
    '100uF', '220uF', '330uF', '470uF',
    #'1000uF', '2200uF', '3300uF', '4700uF', '6800uF'
]

electros = capacitorValue('0.1uF')
pi2 = 2 * math.pi

lp1Freq = 75.0
lp1Resistor = ''
lp1Capacitor = ''

maxC = 0.0
hpFreq = 0.0
hpResistor = ''
hpCapacitor = ''

for resistor in resistors:
    R = resistorValue(resistor)
    if R > 0:
        for capacitor in capacitors:
            C = capacitorValue(capacitor)
            frequency = 1 / (pi2 * R * C)
            # We're trying to filter a square wave of 25Hz. The 3rd harmonic
            # is 75Hz. So we need to filter somewhere below that but as close
            # to 25Hz as we can get. We're also removing the DC offset with
            # a coupling capacitor / high pass filter. So we need a value which
            # will cut off below the 25Hz with the highest capacitor value we
            # can find.
            if C < electros and frequency > 25.0 and frequency < 75.0 and frequency < lp1Freq:
                lp1Freq = frequency
                lp1Resistor = resistor
                lp1Capacitor = capacitor
            if frequency < 25.0 and C > maxC:
                maxC = C
                hpFreq = frequency
                hpResistor = resistor
                hpCapacitor = capacitor
print 'Low pass filter (1):', lp1Resistor, lp1Capacitor, lp1Freq
print 'High pass filter:', hpResistor, hpCapacitor, hpFreq
