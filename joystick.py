import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gpio_lists = [17, 27, 22]

state = [0,0,0]
try:
	for gpio in gpio_lists:
		GPIO.setup(gpio, GPIO.IN)
	cur_stat = 0

	while True:
		for i, gpio in enumerate(gpio_lists):
			state[i] = GPIO.input(gpio)

		print(state)
		time.sleep(0.1)
except:
	GPIO.cleanup()
