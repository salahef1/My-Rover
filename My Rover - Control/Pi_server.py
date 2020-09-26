import RoverControl
from socket import *
from time import ctime
import pigpio

#setup Motors
pi = pigpio.pi()
CameraServo = RoverControl.CameraServo(pi, 13, 12)
RoverMotors = RoverControl.RoverMotors(pi, 14, 18, 23, 24)

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

closed = False
while True:
    print ('Waiting for connection')
    tcpCliSock,addr = tcpSerSock.accept()
    print ('...connected from : ', addr)
    while True:
        data = ''
        data = tcpCliSock.recv(BUFSIZE).decode()
        data = data[2:]
        print ('DATA: ', data)
        #Camera
        if data == 'camera_UP':
            CameraServo.moveUP()
            print ('UP')
        elif data == 'camera_Left':
            CameraServo.moveLeft()
            print ('Left')
        elif data == 'camera_Down':
            CameraServo.moveDown()
            print ('Down')
        elif data == 'camera_Right':
            CameraServo.moveRight()
            print ('Right')
        elif data == 'camera_ResetPos':
            CameraServo.reset()
            print ('Reset Position')
        #Rover
        elif data == 'rover_UP':
            RoverMotors.moveUP()
            print ('UP')
        elif data == 'rover_Left':
            RoverMotors.moveLeft()
            print ('Left')
        elif data == 'rover_Down':
            RoverMotors.moveDown()
            print ('Down')
        elif data == 'rover_Right':
            RoverMotors.moveRight()
            print ('Right')
        elif data == 'rover_Stop':
            RoverMotors.stop()
            print ('Reset Position')
        #General
        elif data == 'StopGPIO':
            CameraServo.reset()
            pi.stop()
            print ('Stoped GPIO')
        elif data == 'StopServer':
            closed = True
        else:
            break
    if closed:
        break
tcpSerSock.close()
        