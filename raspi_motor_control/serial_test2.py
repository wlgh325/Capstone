import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

Xposition = "0"
Yposition = "1"
i =0
time.sleep(2)
while 1:
    X = Xposition.encode('utf-8')
    Y = Yposition.encode('utf-8')
    //c=c.encode('utf-8')
    print(X,Y)
    
    arduino.write(X);
    arduino.write(Y);
    
    print("Hi python")
        #print(arduino.readline())
    time.sleep(0.01)
    i = i + 1;
    if i==360:
        break

