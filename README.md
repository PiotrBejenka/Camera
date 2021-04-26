# Camera
A program that transforms a Raspberry Pi into a camera.

### Needed stuff:
- Raspberry Pi (I used RPi 4b)
- camera (I tested the code with the RPi Camera v2 but any camera using CSI connector and supported by picamera library should be fine)
- display (I connected the monitor via hdmi, but displays prepared to work with RPi via the DSI connector should also work with the code. As I know, the libraries used do not support the preview from the camera on displays connected to RPi via GPIO)<br /> <br />

### ! I was starting the program in the terminal and finishing its work with the shortcut ctrl+c. So if you are going to run the program, eg in Thonny, it is worth adding one more button finishing camera preview and ending the program. Currently I don't have any more buttons, but as soon as I have another one I will test and update the code. !<br /> <br /> 

## How the program works:
After starting the program, the camera preview will appear on the screen and you will be able to record images using the buttons. One of them starts video recording, pressing the other one stops recording, and the last one is for taking a photo. Files are saved under a name consisting of the date and time the photo was taken or the video recording started.
