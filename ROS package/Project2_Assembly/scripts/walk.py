#!/usr/bin/env python

import rospy
import sys, select, termios, tty
import math
from std_msgs.msg import Float64
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from sympy import *

global sub_once
pub_right_front_hip = rospy.Publisher('/quad_walk/right_front_hip_control/command', Float64, queue_size=1)
pub_right_rear_hip  = rospy.Publisher('/quad_walk/right_rear_hip_control/command', Float64, queue_size=1)
pub_right_front_knee = rospy.Publisher('/quad_walk/right_front_knee_control/command', Float64, queue_size=1)
pub_right_rear_knee = rospy.Publisher('/quad_walk/right_rear_knee_control/command', Float64, queue_size=1)
pub_left_front_hip = rospy.Publisher('/quad_walk/left_front_hip_control/command', Float64, queue_size=1)
pub_left_rear_hip  = rospy.Publisher('/quad_walk/left_rear_hip_control/command', Float64, queue_size=1)
pub_left_front_knee = rospy.Publisher('/quad_walk/left_front_knee_control/command', Float64, queue_size=1)
pub_left_rear_knee = rospy.Publisher('/quad_walk/left_rear_knee_control/command', Float64, queue_size=1)
pub_left_arm1 = rospy.Publisher('/quad_walk/left_arm_control1/command', Float64, queue_size=1)
pub_right_arm1 = rospy.Publisher('/quad_walk/right_arm_control1/command', Float64, queue_size=1)
pub_left_arm3 = rospy.Publisher('/quad_walk/left_arm_control3/command', Float64, queue_size=1)
pub_right_arm3 = rospy.Publisher('/quad_walk/right_arm_control3/command', Float64, queue_size=1)
pub_left_arm5 = rospy.Publisher('/quad_walk/left_arm_control5/command', Float64, queue_size=1)
pub_right_arm5 = rospy.Publisher('/quad_walk/right_arm_control5/command', Float64, queue_size=1)

def init_stance():
    rospy.init_node('rrbot_talker',anonymous=True)
    pos = -0.69
    pos1 = 1.54
    pos2 = 0
    position = pos  
    rate=rospy.Rate(4)

    i=0
    j=0
    while not rospy.is_shutdown(): 
	rospy.loginfo(position)

	pos3 = -0.70
        if i==0:
	 print('in i=0')
	 print('right_front')
         pub_right_front_hip.publish(position)
	 rospy.sleep(2.)
	 print('right_rear')
         pub_right_rear_hip.publish(position)
	 rospy.sleep(2.)
	 print('left_front')
    	 pub_left_front_hip.publish(position)
	 rospy.sleep(2.)
	 print('left_rear')
    	 pub_left_rear_hip.publish(position)
	 rospy.sleep(2.)
	 print('right_front')
    	 pub_right_front_knee.publish(pos1)
	 rospy.sleep(2.)
	 print('right_rear')
    	 pub_right_rear_knee.publish(pos1)
    	 rospy.sleep(2.)
	 print('left_front')
    	 pub_left_front_knee.publish(pos1)
 	 rospy.sleep(2.)
	 print('left_rear')
    	 pub_left_rear_knee.publish(pos1)
	 rospy.sleep(2.)

	 if j==0:
    	  pub_right_arm1.publish(pos2)
	  rospy.sleep(1.)
    	  pub_left_arm1.publish(pos2)
	  rospy.sleep(1.)
    	  pub_right_arm3.publish(pos2) 
	  rospy.sleep(1.)
    	  pub_left_arm3.publish(pos2)
	  rospy.sleep(1.)
    	  pub_right_arm5.publish(pos2)
	  rospy.sleep(1.)
    	  pub_left_arm5.publish(pos2)
	  rospy.sleep(1.)
 	  j=1
	 i=1	
	

	elif i==1:
	 print('in i=5')
	 pos4=-0.71
	 pub_right_front_knee.publish(1.64)
	 pub_right_front_hip.publish(pos4)
	 pub_left_rear_knee.publish(1.64)
	 pub_left_rear_hip.publish(pos4)
	 rospy.sleep(2.)
	 pub_right_rear_knee.publish(1.64)
         pub_right_rear_hip.publish(pos4)
	 pub_left_front_knee.publish(1.64)
    	 pub_left_front_hip.publish(pos4)
	 rospy.sleep(2.)
	 i=0


if __name__=="__main__":
    try:
	init_stance()
    except rospy.ROSInterruptException:
	pass
    
