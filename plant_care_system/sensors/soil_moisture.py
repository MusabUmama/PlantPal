import RPi.GPIO as GPIO
import time

SOIL_MOISTURE_PIN = 21

def read_soil_moisture():
  """
  Reads the soil moisture level from the sensor and returns a value.

  Returns:
      float: A value between 0.0 (dry) and 1.0 (wet) representing the soil moisture level.
  """

  GPIO.setmode(GPIO.BCM)

  GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)

  if GPIO.input(SOIL_MOISTURE_PIN):
    output = 0.0
  else:
    output = 1.0

  GPIO.cleanup()

  return output
