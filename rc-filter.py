#!/usr/bin/python

################################################################################
#
# Calculate the resistor and capacitor to form the first stage filter
# to clip a 25Hz square wave to a sine wave
#
# This filter will probably need 4 stages but "one step at a time"
#
################################################################################

import math

def resistorValue(val):
    newVal = val.replace('M', '.')
    if newVal != val:
        return float(newVal) * 1000000.0
    newVal = val.replace('K', '.')
    if newVal != val:
        return float(newVal) * 1000.0
    newVal = val.replace('R', '.')
    if newVal != val:
        return float(newVal)

def capacitorValue(val):
    newVal = val.replace('pF', '')
    if newVal != val:
        return float(newVal) * 0.000000000001
    newVal = val.replace('nF', '')
    if newVal != val:
        return float(newVal) * 0.000000001

# www.bitsbox.co.uk 1/4W Carbon Film 5% Resistors
resistors = [
    "0R", "1R", "1R5", "1R8", "2R2", "3R3", "4R7", "5R6", "6R8", "8R2",
    "10R", "12R", "15R", "18R", "22R", "33R", "47R", "56R", "68R", "82R",
    "100R", "120R", "150R", "180R",
    "220R", "240R", "270R", "330R", "390R", "470R", "560R", "680R", "820R",
    "1K", "1K2", "1K5", "1K8",
    "2K2", "2K4", "2K7", "3K3", "3K9", "4K7", "5K6", "6K8", "8K2",
    "10K", "12K", "15K", "18K",
    "22K", "24K", "27K", "33K", "39K", "47K", "56K", "68K", "82K",
    "100K", "120K", "150K", "180K",
    "220K", "240K", "270K", "330K", "390K", "470K", "560K", "680K", "820K",
    "1M", "1M2", "1M5", "1M8",
    "2M2", "2M4", "2M7", "3M3", "3M9", "4M7", "5M6", "6M8", "8M2", "10M"
]

# www.bitsbox.co.uk Ceramic Disc Capacitors
capacitors = [
    "1pF", "2.2pF", "2.7pF", "3.3pF", "4.7pF", "5pF", "6.8pF",
    "10pF", "15pF", "18pF",
    "22pF", "25pF", "27pF", "33pF", "47pF", "50pF", "68pF",
    "100pF", "150pF",
    "220pF", "330pF", "390pF", "470pF", "500pF", "560pF", "680pF", "820pF",
    "1000pF", "1500pF", "1800pF",
    "2200pF", "2700pF", "3300pF", "3900pF", "4700pF", "6800pF",
    "10nF", "15nF",
    "22nF", "33nF", "47nF", "100nF", "220nF"
]

pi2 = 2 * math.pi
minFreq = 75.0
minResistor = ''
minCapacitor = ''

for resistor in resistors:
    R = resistorValue(resistor)
    if R > 0:
        for capacitor in capacitors:
            C = capacitorValue(capacitor)
            frequency = 1 / (pi2 * R * C)
            # We're trying to filter a square wave at 25Hz
            # The 3rd harmonic is 75Hz
            # So we need to filter somewhere below that value
            # as close to 25Hz as we can get
            if frequency > 25.0 and frequency < 75.0:
                if frequency < minFreq:
                    minFreq = frequency
                    minResistor = resistor
                    minCapacitor = capacitor
print minResistor, minCapacitor, minFreq
