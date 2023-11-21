import Adafruit_DHT
import time
import datetime
import RPi.GPIO as GPIO  # GPIOモジュールを追加

# センサーのタイプとピン番号を指定
sensor = Adafruit_DHT.DHT11  # センサータイプをDHT11に変更
pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)


try:
    print("first valid input: " + str(datetime.datetime.now()))
    while True:
        # センサーデータを取得
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # データの表示
        if humidity is not None and temperature is not None:
            print("Last valid input: " + str(datetime.datetime.now()))
            print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
            break
        else:
            print('Failed to retrieve data from the sensor.')

        # 一定の待機時間（ここでは6秒）を挟む
        time.sleep(6)
	
    print('LED lights up')
	
    while True:
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program terminated by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleaning up GPIO")
    # プログラム終了時にGPIOをクリーンアップ
    GPIO.cleanup()
