#!/usr/bin/env python
import time
import serial
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16MultiArray

class JoystickPub(object):
    def __init__(self):

        rospy.init_node('joystick_handler')

        # Subscribe to the topic on which the joy_node publishes the joystick values
        sub1 = rospy.Subscriber('/joy', Joy, self.joy_cb) 
        
        # Publish Twist values to represent joystick axes movement
        self.joy_pub = rospy.Publisher('/joy_data', Int16MultiArray, queue_size=1)

    def joy_cb(self, msg):
        
        self.forward_thrust = int(1500 + (msg.axes[1] * 400))
        self.depth_thrust = int(1500 + (-msg.axes[4] * 400))
        self.joy_pub.publish([forward_thrust, depth_thrust])
        

if __name__ == '__main__':
    try:
        JoystickPub()
    except rospy.ROSInterruptException:
        rospy.logerr('Could not start joystick_handler node.')
