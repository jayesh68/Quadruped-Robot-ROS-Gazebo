#!/usr/bin/env python

import rospy
import tf
from Project2_Assembly.srv import *
from geometry_msgs.msg import Pose
from sympy import *
import math

def callback(msg):
    # Create symbols for DH param
    q1, q2 = symbols('q1:3')                                 # joint angles theta
    d1, d2 = symbols('d1:3')                                 # link offsets
    a0, a1 = symbols('a0:2')                                 # link lengths
    alpha0, alpha1 = symbols('alpha0:2') 			 # joint twist angles
        
    # Create Modified DH parameters
    dh = {alpha0:      0, a0:      0, d1:  0.75, q1:        q1,
          alpha1: -pi/2., a1:    0.0, d2:     0, q2: -pi/2.+q2}
        
    # Define Modified DH Transformation matrix
    # Function to return homogeneous transform matrix
    def TF_Mat(alpha, a, d, q):
            TF = Matrix([[            cos(q),           -sin(q),           0,             a],
                        [ sin(q)*cos(alpha), cos(q)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                        [ sin(q)*sin(alpha), cos(q)*sin(alpha),  cos(alpha),  cos(alpha)*d],
                        [                 0,                 0,           0,             1]])
            return TF
        
    # Create individual transformation matrices
    # Substitute DH_Table
    T0_1 = TF_Mat(alpha0, a0, d1, q1).subs(dh)
    T1_2 = TF_Mat(alpha1, a1, d2, q2).subs(dh)
    # Copying for simplicity
    pose=Pose()
    pose.position.x =  msg.position.x 
    pose.position.y =  msg.position.y
    px = pose.position.x
    py = pose.position.y
    #py=0
    # Also print Roll, Pitch, Yaw
    rospy.loginfo(px)
    rospy.loginfo(py)

    # Calculate joint angles using Geometric IK method
    # Calculate theta1
    a0=-0.127
    a1=-0.0895

    phi1 = math.degrees(atan(py/px))
    rospy.loginfo(py/px)
    rospy.loginfo('phi1 %s', phi1)
    r = sqrt(pow(px,2) + pow(py,2))
    #r= (a0+a1)
    add=(-(a1*a1)+(a0*a0)+(r*r))/(2*a0*r)

    '''
    if add > 1:
	add-=1
    elif add < 1:
	add+=1
    '''	

    rospy.loginfo('add %s',add)
    phi2 = math.degrees(acos(add))
    rospy.loginfo('phi2 %s', phi2)
    theta1 = (phi1 - phi2)
    rospy.loginfo('theta1 %s', theta1)
    #Find theta2
    add2=(-(r*r)+(a1*a1)+(a0*a0))/(2*a0*a1)
     
    '''
    if add2 > 1:
	add2-=1
    elif add < -1:
	add2+=1
    '''
    rospy.loginfo('add2 %s',add2)

    phi3 = math.degrees(acos(add2))
    rospy.loginfo('phi3 %s',phi3)

    theta2 = (180 - phi3)
    rospy.loginfo(theta2)

    #theta1=math.radians(theta1)
    #theta2=math.radians(theta2)

    rospy.loginfo('theta1 %s', theta1)
    rospy.loginfo('theta2 %s', theta2)
 
def listener():
    rospy.init_node('pose_subscriber', anonymous=True)
    rospy.Subscriber('/pose', Pose, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()
