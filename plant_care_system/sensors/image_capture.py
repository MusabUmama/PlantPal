from picamera2 import Picamera2

class CameraSensor:
  """
  A class for capturing images using the Raspberry Pi camera module.
  """

  def __init__(self, resolution=(640, 480)):
    """
    Initializes the camera object with the specified resolution.

    Args:
      resolution (tuple, optional): The desired image resolution (width, height). Defaults to (640, 480).
    """
    self.camera = Picamera2()
    self.camera.resolution = resolution

  def capture_image(self, filename):
    """
    Captures an image and saves it to the specified filename.

    Args:
      filename (str): The filename (including path) to save the captured image.
    """
    capture_request = self.camera.create_still_capture_request()

    with self.camera.pipeline() as pipeline:

      still_output = pipeline.start(capture_request)

      still_output.wait_request(capture_request)

      image = still_output.result.image.planes[0].array

      with open(filename, "wb") as f:
        f.write(image.tobytes())

  def close(self):
    """
    Releases the camera resources.
    """
    self.camera.close()

camera = CameraSensor()
camera.capture_image(image)
camera.close()