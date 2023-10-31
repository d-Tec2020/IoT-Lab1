import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))

	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)
	        break

	    time.sleep(6)

	while True:
	    GPIO.output(23, GPIO.HIGH)
	    time.sleep(0.5)
	    GPIO.output(23, GPIO.LOW)
	    time.sleep(0.5)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
