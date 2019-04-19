import serial
import time

ser=serial.Serial()
ser.baudrate=2400
ser.port='COM6'
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_ODD
ser.timeout=1
ser.rtscts=True
ser.dsrdtr=True
#ser.setDTR(True)
#ser.setRTS(True)

ser.open()
time.sleep(1)
print(ser.dsr)

#ser=serial.Serial(port='COM2', baudrate=2400,bytesize=serial.SEVENBITS, parity=serial.PARITY_ODD,dsrdtr=True, timeout=1)

#ser.setDTR(True)

#ser.open()

while(True):
    print(ser.dtr)
    print(ser.dsr)

    #string="Hello"
    #ser.write(string)

    zmienna=ser.readline()
    #zmienna=ser.read()
    #print(ser.readline())
    print(zmienna)
