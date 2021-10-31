import datetime as dt
from time import sleep
from bme280 import BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

factor = 2.25
cpu_temps = [get_cpu_temperature()] * 5

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

while True:
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    temperature = bme280.get_temperature()
    comp_temp = temperature - ((avg_cpu_temp - temperature) / factor)

    sleep(5)