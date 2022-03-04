#!/usr/bin/python

### QUad_Walk Forward Kinematics ###

import numpy as np
import math
from numpy import array
from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2, pprint
from sympy.matrices import Matrix
from decimal import *
import tf


if __name__ == "__main__":


	(roll,pitch,yaw) = tf.transformations.euler_from_quaternion(
                [0.343,
                 0.618,
                 0.618,
                 -0.343])
        print(roll)
	print(pitch)
	print(yaw)	
	
	x=sin(roll)*sin(yaw)+cos(roll)*sin(pitch)*cos(yaw)
	y=-cos(roll)*sin(yaw)+sin(roll)*sin(pitch)*cos(yaw)
	z=cos(pitch)*cos(yaw)
	print(x)
	print(y)
	print(z)

	(roll1,pitch1,yaw1) = tf.transformations.euler_from_quaternion(
                [0,
                 0,
                 -0.1309,
                 0.9913])
        print(roll1)
	print(pitch1)
	print(yaw1)
	
	(roll2,pitch2,yaw2) = tf.transformations.euler_from_quaternion(
                [0,
                 0,
                 -0.4683,
                 0.8835])
        print(roll2)
	print(pitch2)
	print(yaw2)

	(roll3,pitch3,yaw3) = tf.transformations.euler_from_quaternion(
                [0,
                 0,
                 0.995,
                 0.097])
        print(roll3)
	print(pitch3)
	print(yaw3)
	
	(roll4,pitch4,yaw4) = tf.transformations.euler_from_quaternion(
                [0,
                 0,
                 0,
                 1])
        print(roll4)
	print(pitch4)
	print(yaw4)


