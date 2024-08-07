from picamera2 import Picamera2

import numpy as np



class CameraSensor:



  def __init__(self, resolution=(640, 480)):



    self.camera = Picamera2()

    self.camera.configure(self.camera.create_still_configuration(main={"size": resolution}))



  def capture_image(self):

    

    self.camera.start()

    

    image_array = self.camera.capture_array()

    

    self.camera.stop()

    

    return image_array



  def close(self):



    self.camera.close()

