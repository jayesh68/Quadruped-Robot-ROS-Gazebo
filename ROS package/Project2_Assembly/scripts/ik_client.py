#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from Project2_Assembly.srv import *
from sympy import *

def CalculateIK_client(x):
    print("waiting1")
    rospy.wait_for_service('calculate_ik',timeout=2)
    print("waiting")
    try:
       calculate_ik = rospy.ServiceProxy('calculate_ik', CalculateIK)
       resp1 = calculate_ik(x)
       return resp1.points
    except rospy.ServiceException as e:
       print("Service call failed: %s"%e)
   
def usage():
       return x
   
if __name__ == "__main__":
       x = Matrix([ 1,   1,   1])
       print(usage())
       #sys.exit(1)
       print("Requesting %s"%(x))
       print("calling %s = %s"%(x, CalculateIK_client(x)))
