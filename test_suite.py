import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=200  # change this value
sound_treshold=200 # change this value


  #GPIO.output(pin, GPIO.HIGH)
  #GPIO.output(pin, GPIO.LOW)

  # get reading from adc 
  # mcp.read_adc(adc_channel)

while True: 
  # 1. Blink the LED 5 times (500 ms on/off)
  for i in range(5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)
  
  # 2. Read light sensor for ~5 seconds every 100 ms (50 total readings)
  for i in range(50):
    light_val = mcp.read_adc(0) # light sensor on channel 0
    if light_val > lux_treshold:
      state = "bright"
    else: 
      state = "dark"
    print("Light:", light_val, state)
    time.sleep(0.1)

  # 3. Blink LED 4 times (200 ms on/off)
  for i in range(4):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.2)
  
  # 4. Read sound sensor for ~5 seconds every 100 ms (50 total readings
  for i in range(50):
    sound_val = mcp.read_adc(1) # sound sensor on channel 1
    print("Sound:", sound_val)
    if sound_val > sound_treshold:
      GPIO.output(11, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(11, GPIO.LOW)
    time.sleep(0.1)
