#!/usr/bin/env python
import time
import serial
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16MultiArray

class JoystickHandler(object):
    def __init__(self):

        rospy.init_node('joystick_handler')

        # Subscribe to the topic on which the joy_node publishes the joystick values
        sub1 = rospy.Subscriber('/joy_data', Int16MultiArray, self.joy_data_cb) 
        
        self.prev_forward = 1500
        self.prev_depth = 1500
        
        self.forward_thrust = self.depth_thrust = self.prev_forward = self.prev_depth = 1500
       
        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
            self.loop()
            rate.sleep()

    def joy_data_cb(self, msg):
        self.forward_thrust = int(1500 + (msg.axes[1] * 400))
        self.depth_thrust = int(1500 + (-msg.axes[4] * 400))
        
    def loop(self):
        print('looping')

        if(self.forward_thrust>self.prev_forward):
            char_1 = chr(97+(4*2))
            char_2 = chr(97+(5*2+1))
            char_3 = chr(97+(6*2+1))
            char_4 = chr(97+(7*2))
        elif(self.forward_thrust<self.prev_forward):
            char_1 = chr(97+(4*2+1))
            char_2 = chr(97+(5*2))
            char_3 = chr(97+(6*2))
            char_4 = chr(97+(7*2+1))
        if self.forward_thrust != self.prev_forward:
            for i in range(min(self.forward_thrust,self.prev_forward), max(self.forward_thrust,self.prev_forward), 10):
                time.sleep(0.005)
                self.ser.write(char_1.encode('utf-8'))
                print(char_1.encode('utf-8'))
                self.ser.write(char_2.encode('utf-8'))
                print(char_2.encode('utf-8'))
                self.ser.write(char_3.encode('utf-8'))
                print(char_3.encode('utf-8'))
                self.ser.write(char_4.encode('utf-8'))
                print(char_4.encode('utf-8'))
        
        if(self.depth_thrust>self.prev_depth):
            char_1 = chr(97+(0*2))
            char_2 = chr(97+(1*2+1))
            char_3 = chr(97+(2*2))
            char_4 = chr(97+(3*2))
        elif(self.depth_thrust<self.prev_depth):
            char_1 = chr(97+(0*2+1))
            char_2 = chr(97+(1*2))
            char_3 = chr(97+(2*2+1))
            char_4 = chr(97+(3*2+1))
        if self.depth_thrust != self.prev_depth:
            for i in range(min(self.depth_thrust,self.prev_depth), max(self.depth_thrust,self.prev_depth), 10):
                time.sleep(0.005)
                self.ser.write(char_1.encode('utf-8'))
                print(char_5.encode('utf-8'))
                self.ser.write(char_2.encode('utf-8'))
                print(char_6.encode('utf-8'))
                self.ser.write(char_3.encode('utf-8'))
                print(char_7.encode('utf-8'))
                self.ser.write(char_4.encode('utf-8'))
                print(char_8.encode('utf-8'))
        
        self.prev_forward = self.forward_thrust
        self.prev_depth = self.depth_thrust

if __name__ == '__main__':
    try:
        JoystickHandler()
    except rospy.ROSInterruptException:
        rospy.logerr('Could not start joystick_handler node.')
