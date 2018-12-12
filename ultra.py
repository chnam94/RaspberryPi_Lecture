import time
import RPi.GPIO as GPIO

trig = 13
echo = 19

print("Start")

GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
	while True:
		gpio.output(trig, False)
		time.sleep(0.5)
		gpio.output(trig, True)
		time.sleep(0.00001)
		gpio.output(trig, False)
		while gpio.input(echo) == 0:
			pulse_start = time.time()

		while gpio.input(echo) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17000
		distance = round(distance, 2)

		print("Distance : " + str(distance) +  "cm")
except:
	gpio.cleanup()
