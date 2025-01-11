from machine import Pin, I2C, ADC
import ssd1306
import dht
from time import sleep

# ESP32 Pin-Zuweisung für I2C und DHT
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
dht_sensor = dht.DHT22(Pin(15))  # DHT22 an Pin D15

# SSD1306 initialisieren
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Potentiometer initialisieren (an D34 = GPIO 34)
potentiometer = ADC(Pin(34))
potentiometer.atten(ADC.ATTN_11DB)  # Volle Spannungsreichweite (0 - 3.3V)
potentiometer.width(ADC.WIDTH_12BIT)  # 12-Bit-Auflösung (0-4095)

# Begrüßungstext
oled.fill(0)
oled.text("Klimachecker", 0, 10)
oled.text("P.B. Eichert", 0, 30)
oled.text("FS11.2 LF7", 0, 50)
oled.show()
sleep(5)

# Hauptanzeige
while True:
    # Potentiometerwert lesen und simulierte Luftfeuchtigkeit berechnen
    pot_value = potentiometer.read()
    hum = (pot_value / 4095) * 100  # Skaliere auf 0 % bis 100 %
    
    # Temperatur vom DHT22-Sensor lesen
    dht_sensor.measure()
    temp = dht_sensor.temperature()  # Temperatur in °C
    
    # Displayinhalt aktualisieren
    oled.fill(0)
    oled.text("Klimacheck", 0, 0)
    oled.text("Temp: {:.1f} C".format(temp), 0, 20)
    oled.text("Luftf.: {:.1f} %".format(hum), 0, 30)
    oled.text("TGBBZ1", 0, 50)
    oled.show()

    sleep(2)  # Update Intervall in s