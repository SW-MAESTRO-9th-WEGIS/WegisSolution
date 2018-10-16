import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('1.h264')
camera.wait_recording(3)
camera.stop_recording()
