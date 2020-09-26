import pigpio
import time

class RoverMotors:
    def __init__(self, pi, RightMotor_1, RightMotor_2, LeftMotor_1, LeftMotor_2):
        self.pi = pi
        self.RightMotor_1 = RightMotor_1
        self.RightMotor_2 = RightMotor_2
        self.LeftMotor_1 = LeftMotor_1
        self.LeftMotor_2 = LeftMotor_2
        pi.set_mode(RightMotor_1, pigpio.OUTPUT)
        pi.set_mode(RightMotor_2, pigpio.OUTPUT) 
        pi.set_mode(LeftMotor_1, pigpio.OUTPUT) 
        pi.set_mode(LeftMotor_2, pigpio.OUTPUT) 
    def moveUP(self):
        self.pi.write(self.RightMotor_1, 1)
        self.pi.write(self.RightMotor_2, 0)
        self.pi.write(self.LeftMotor_1, 1)
        self.pi.write(self.LeftMotor_2, 0)
    def moveDown(self):
        self.pi.write(self.RightMotor_1, 0)
        self.pi.write(self.RightMotor_2, 1)
        self.pi.write(self.LeftMotor_1, 0)
        self.pi.write(self.LeftMotor_2, 1)
    def moveLeft(self):
        self.pi.write(self.RightMotor_1, 1)
        self.pi.write(self.RightMotor_2, 0)
        self.pi.write(self.LeftMotor_1, 0)
        self.pi.write(self.LeftMotor_2, 1)
    def moveRight(self):
        self.pi.write(self.RightMotor_1, 0)
        self.pi.write(self.RightMotor_2, 1)
        self.pi.write(self.LeftMotor_1, 1)
        self.pi.write(self.LeftMotor_2, 0)
    def stop(self):
        self.pi.write(self.RightMotor_1, 0)
        self.pi.write(self.RightMotor_2, 0)
        self.pi.write(self.LeftMotor_1, 0)
        self.pi.write(self.LeftMotor_2, 0)

class CameraServo:
    def __init__(self, pi, servo_X, servo_Y):
        self.pi = pi
        self.servo_X = servo_X
        self.servo_Y = servo_Y
        pi.set_mode(servo_X, pigpio.OUTPUT)
        pi.set_mode(servo_Y, pigpio.OUTPUT)
        #init frequency
        pi.set_PWM_frequency(servo_X, 50)
        pi.set_PWM_frequency(servo_Y, 50)
        #init dutycycle
        self.current_X = 21
        self.current_Y = 11
        pi.set_PWM_dutycycle(servo_X, self.current_X)
        pi.set_PWM_dutycycle(servo_Y, self.current_Y)
        time.sleep(1)
    def moveUP(self):
        self.current_Y = self.current_Y - 2
        if self.current_Y < 5:
            self.current_Y = 5
        self.pi.set_PWM_dutycycle(self.servo_Y, self.current_Y)
        print("current_Y: ", self.current_Y)
        time.sleep(0.5)
    def moveDown(self):
        self.current_Y = self.current_Y + 2
        if self.current_Y > 19:
            self.current_Y = 19
        self.pi.set_PWM_dutycycle(self.servo_Y, self.current_Y)
        print("current_Y: ", self.current_Y)
        time.sleep(0.5)
    def moveLeft(self):
        self.current_X = self.current_X + 2
        if self.current_X > 33:
            self.current_X = 33
        self.pi.set_PWM_dutycycle(self.servo_X, self.current_X)
        print("current_X: ", self.current_X)
        time.sleep(0.5)
    def moveRight(self):
        self.current_X = self.current_X - 2
        if self.current_X < 8:
            self.current_X = 8
        self.pi.set_PWM_dutycycle(self.servo_X, self.current_X)
        print("current_X: ", self.current_X)
        time.sleep(0.5)
    def reset(self):
        self.current_X = 21
        self.current_Y = 11
        self.pi.set_PWM_dutycycle(self.servo_X, self.current_X)
        self.pi.set_PWM_dutycycle(self.servo_Y, self.current_Y)
        time.sleep(0.5)
        
class DistanceSensor:
    def __init__(self, pi, TRIG, ECHO):
        self.pi = pi
        self.TRIG = TRIG
        self.ECHO = ECHO
        pi.set_mode(TRIG, pigpio.OUTPUT)
        pi.set_mode(ECHO, pigpio.INPUT)
    def getDistance(self):
        global startTime
        global endTime
        global waitTime
        startTime = 0
        endTime = 0
        waitTime =0
        self.pi.write(self.TRIG, 1)
        time.sleep(0.2)
        self.pi.write(self.TRIG, 0)

        waitTime = time.time()
        while self.pi.read(self.ECHO) == False:
            startTime = time.time()
            if(startTime-waitTime > 0.45):
                return 0
            
        waitTime = time.time()
        while self.pi.read(self.ECHO) == True:
            endTime = time.time()
            if(endTime-waitTime > 0.45):
                return 0
            
        sig_time = endTime - startTime
        #Distance in CM
        distance = sig_time * 17150
        if distance < 0:
            return 0
        else :
            return distance
            
