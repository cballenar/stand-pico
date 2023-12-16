from machine import Pin
import time
import utime

# Factor used to calculate ADC reading to voltage
FACTOR = 3.3 / 65535 * 100

# Number of polls to average
POLLS = 300 

# Frequency of readings
FREQ = 0.984

# initialize an ADC object for pin 26 / ADC channel 0
SENSOR = machine.ADC(0)

# initialize LED pins
LEDA = Pin(18, Pin.OUT)
LEDB = Pin(19, Pin.OUT)
LEDC = Pin(20, Pin.OUT)
LEDD = Pin(21, Pin.OUT)

# Sitting time will be counted as if it were a glass of water
# The more you sit, the more it fills up (1 per second)
# Time standing will subtract from it at a faster rate (4 per second)
# This will result in 1hr being cleared with 15mins of standing
time_sitting = 0

# Delta is used to count the number of times the sensor has been polled
# Used for reference only. Probably will be removed.
delta = 0

def avgReadings(sensor):
    readings = []
    while (len(readings) < POLLS):
        reading = sensor.read_u16() * FACTOR
        readings.append(reading)
    
    average = sum(readings) / len(readings)
    return average

# Map Reading to a 1-100 value
def mapReading(reading):
    # Quadratic equation was calculated from collected data
    value = (12.6 * reading * reading) - (3.95 * reading) + 1.35
    # truncate value and return
    return min(max(value, 0), 100)

# Analyze data and print to console
# Mostly keeping for archivable purposes
MIN = 100
MAX = 0
def analyzeData():
    reading = avgReadings(SENSOR)
    MIN = min(reading,MIN)
    MAX = max(reading,MAX)
    print(f"Count {delta:>{3}}: {reading:.2f}. Min: {MIN:.2f} Max: {MAX:.2f}")
    delta+=1
    time.sleep(FREQ)

while True:
    reading = mapReading(avgReadings(SENSOR))
    sitting = True if (reading < 50) else False
    current_time = utime.ticks_ms() / 1000
    
    if (sitting):
        time_sitting += 1
    else:
        time_sitting = 0 if time_sitting < 4 else time_sitting-4
    
    if (time_sitting > 3600):
        LEDA.value(1)
        LEDB.value(1)
        LEDC.value(1)
        LEDD.value(1)
    elif (time_sitting > 2700):
        LEDA.value(1)
        LEDB.value(1)
        LEDC.value(1)
        LEDD.value(0)
    elif (time_sitting > 1800):
        LEDA.value(1)
        LEDB.value(1)
        LEDC.value(0)
        LEDD.value(0)
    elif (time_sitting > 900):
        LEDA.value(1)
        LEDB.value(0)
        LEDC.value(0)
        LEDD.value(0)
    else:
        LEDA.value(0)
        LEDB.value(0)
        LEDC.value(0)
        LEDD.value(0)

    print(f"[{delta:>{4}}] {sitting} {time_sitting:.0f}")
    delta+=1
    time.sleep(FREQ)
