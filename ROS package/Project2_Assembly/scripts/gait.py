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

pub_left_front = rospy.Publisher('/gazebo/my_robot_left_front_knee_link1',Pose, queue_size=1)

def callback(msg):
    i=0
    p=Pose()
    p.position.x =  msg.position.x 
    p.position.y =  msg.position.y
    p.orientation.x = msg.orientation.x
    p.orientation.y = msg.orientation.y
    p.orientation.z = msg.orientation.z
    p.orientation.w = msg.orientation.w

    p.position.x += 0.01

    px = p.position.x
    py = p.position.y
    print('pose:', p) 
	
    a0=-0.127
    a1=-0.0895

    phi1 = math.degrees(atan2(py,px))
    rospy.loginfo('phi1 %s', phi1)

    r = sqrt(pow(px,2) + pow(py,2))
    add=-(a1*a1)+(a0*a0)+(r*r)/(2*a0*r)

    if add > 1:
	add-=1
    elif add < -1:
	add+=1

    rospy.loginfo('add %s',add)
    phi2 = math.degrees(acos(add))

    rospy.loginfo('phi2 %s', phi2)
    theta1 = phi1 - phi2
    rospy.loginfo('theta1 %s', theta1)
    
    #Find theta2
    add2=-(r*r)+(a1*a1)+(a0*a0)/(2*a0*a1)
    rospy.loginfo('add2 %s',add2)

    if add2 > 1:
	add2-=1
    elif add < -1:
	add2+=1

    phi3 = math.degrees(acos(add2))
    rospy.loginfo('phi3 %s',phi3)

    theta2 = math.pi - phi3
    rospy.loginfo(theta2)

    theta1=math.radians(theta1)
    theta2=math.radians(theta2)
    
    if i==0:
    	pub_left_front_hip.publish(theta1)
    	rospy.sleep(4)
    	pub_left_front_knee.publish(theta2)
        i=1
	sub_once.unregister()
    elif i==1: 
 	pub_right_front_hip.publish(theta1)
    	rospy.sleep(4)
    	pub_right_front_knee.publish(theta2)
        i=2
	sub_once.unregister()
    elif i==2: 
 	pub_left_rear_hip.publish(theta1)
    	rospy.sleep(4)
    	pub_left_rear_knee.publish(theta2)
        i=3
	sub_once.unregister()
    elif i==3: 
 	pub_right_rear_hip.publish(theta1)
    	rospy.sleep(4)
    	pub_right_rear_knee.publish(theta2)
        i=0
	sub_once.unregister()

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
	#rospy.loginfo(pos1)

	pos3 = -0.54
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
    	 pub_right_front_knee.publish(pos1)
	 rospy.sleep(2.)
    	 pub_right_rear_knee.publish(pos1)
    	 rospy.sleep(2.)
    	 pub_left_front_knee.publish(pos1)
 	 rospy.sleep(2.)
    	 pub_left_rear_knee.publish(pos1)
	 rospy.sleep(2.)

	 if j==0:
    	  pub_right_arm1.publish(pos2)
	  #rospy.sleep(1.)
    	  pub_left_arm1.publish(pos2)
	  #rospy.sleep(1.)
    	  pub_right_arm3.publish(pos2) 
	  #rospy.sleep(1.)
    	  pub_left_arm3.publish(pos2)
	  #rospy.sleep(1.)
    	  pub_right_arm5.publish(pos2)
	  #rospy.sleep(1.)
    	  pub_left_arm5.publish(pos2)
    	  #rospy.sleep(1.)
	  j=1

         sub_once = rospy.Subscriber('/gazebo/my_robot_left_front_knee_link1',Pose,callback)
         #sub_left_front.shutdown()
	 sub_right_front = rospy.Subscriber('/gazebo/my_robot_right_front_knee_link1',Pose,callback)
         #sub_right_front.shutdown()
	 sub_left_rear = rospy.Subscriber('/gazebo/my_robot_left_rear_knee_link1',Pose,callback)
	 #sub_left_rear.shutdown()
         sub_right_rear = rospy.Subscriber('/gazebo/my_robot_right_rear_knee_link1',Pose,callback)
	 #sub_right_rear.shutdown()
	
 	'''  
        elif i==1:
	 print('in i=1')
         pub_right_front_knee.publish(1.64)
	 rospy.sleep(2.)
   	 pub_right_front_hip.publish(pos3)
    	 rospy.sleep(2.)
	 i=2
         
	elif i==2:
 	 print('in i=2')
	 pub_left_front_knee.publish(1.64)
	 rospy.sleep(2.)
    	 #pub_right_front_hip.publish(pos3)
    	 pub_left_front_hip.publish(pos3)
	 rospy.sleep(2.)
	 i=3

	elif i==3:
	 print('in i=3')
	 pub_right_rear_knee.publish(1.64)
	 rospy.sleep(2.)
	 #pub_right_front_hip.publish(position)
         #pub_right_rear_hip.publish(position)
 	 pub_right_rear_hip.publish(pos3)
	 rospy.sleep(2.)
	 i=4

	elif i==4:
	 print('in i=4')
	 pub_left_rear_knee.publish(1.64)
	 rospy.sleep(2.)
    	 pub_left_rear_hip.publish(pos3)
	 rospy.sleep(2.)
	 #pub_left_rear_knee.publish(1.13)
	 #rospy.sleep(3.)
	 i=0
	
	elif i==5:
	 print('in i=5')
	 pos4=-0.71
	 pub_right_front_hip.publish(-0.59)
	 rospy.sleep(2.)
	 pub_left_rear_hip.publish(-0.59)
	 rospy.sleep(2.)
         pub_right_rear_hip.publish(-0.59)
	 rospy.sleep(2.)
    	 pub_left_front_hip.publish(-0.59)
	 rospy.sleep(2.)
	 i=1
	 '''

if __name__=="__main__":
    try:
	init_stance()
    #Stance time
    #wait
    #swing diagonal 
    #wait 
    #swing other diagonal
    #wait
    except rospy.ROSInterruptException:
	pass
    
