

"""
File: chapter02/button_gpiozero.py

Turn on and off an LED with a Button using GPIOZero.

Dependencies:
  pip3 install gpiozero pigpio

Built and tested with Python 3.7 on Raspberry Pi 4 Model B
"""
from gpiozero import Device, LED, Button                                                 # (1)
from gpiozero.pins.pigpio import PiGPIOFactory
import signal                                                                            # (2)

LED_GPIO_PIN = 21
BUTTON_GPIO_PIN = 23

Device.pin_factory = PiGPIOFactory() #set gpiozero to use pigpio by default.

def held():
	light_control(1)

def released():
	light_control(0)

def light_control(value):
	led.value = value
	report_state(value)

def report_state(value):
	if value == 1:
		state = 'on'
	else:
		state = 'off'
	print("Button was used, LED is now " + state)


led = LED(LED_GPIO_PIN)
led.off()


button = Button(BUTTON_GPIO_PIN, pull_up=True, bounce_time=0.1) # Bounce time in seconds # (6)

button.hold_time = 0
button.when_held = held
button.when_released = released

print("Press button to turn LED on and off.")

signal.pause() # Stops program from exiting.                                             # (8)
