from gpiozero import Button



SOIL_MOISTURE_PIN = 21



def read_soil_moisture():

  

  sensor = Button(SOIL_MOISTURE_PIN)

  

  if sensor.is_pressed:

    output = 0.0

  else:

    output = 1.0

    

  return output

