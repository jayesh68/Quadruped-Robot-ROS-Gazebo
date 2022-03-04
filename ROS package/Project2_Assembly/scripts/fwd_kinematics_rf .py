#!/usr/bin/python

### QUad_Walk Forward Kinematics ###

import numpy as np
import math
from numpy import array
from sympy import symbols, cos, sin, pi, simplify, sqrt, atan2, pprint
from sympy.matrices import Matrix
from decimal import *

# Create symbols for DH param
q1, q2, q3, q4 = symbols('q1:5')                                 # joint angles theta
d1, d2, d3, d4 = symbols('d1:5')                                 # link offsets
a0, a1, a2, a3 = symbols('a0:4')                                 # link lengths
alpha0, alpha1, alpha2, alpha3 = symbols('alpha0:4') # joint twist angles

print (sin(math.radians(90)))
print(cos(math.radians(180)))
# DH Table
dh = {alpha0:             math.radians(-93), a0:          0,  d1:     0.0421 , q1:     math.radians(0),
      alpha1:          math.radians(145.47), a1:     -0.127,  d2:     0      , q2:     math.radians(0),
      alpha2:           math.radians(-25.49), a2:          0,  d3:     0     , q3:     math.radians(0),
      alpha3:                             0, a3:    -0.0889,  d4:     0.0149 , q4:     math.radians(0)
      }

# Function to return homogeneous transform matrix
def TF_Mat1(alpha, a, d, q):
    TF = Matrix([[ cos(q),   -sin(q)*cos(alpha),   sin(q)*sin(alpha),       -0.1016+a*cos(q)],
                 [ sin(q),    cos(q)*cos(alpha),  -cos(q)*sin(alpha),       0.061714+d*0.062+a*sin(q)],
                 [      0,           sin(alpha),          cos(alpha),             -0.07874-d*0.998],
                 [      0,                    0,                   0,             1]])
    return TF

def TF_Mat(alpha, a, d, q):
    TF = Matrix([[ cos(q),   -sin(q)*cos(alpha),   sin(q)*sin(alpha),       a*cos(q)],
                 [ sin(q),    cos(q)*cos(alpha),  -cos(q)*sin(alpha),       a*sin(q)],
                 [      0,           sin(alpha),          cos(alpha),              d],
                 [      0,                    0,                   0,             1]])
    return TF

## Substiute DH_Table
T0_1 = TF_Mat1(alpha0, a0, d1, q1).subs(dh)
T1_2 = TF_Mat(alpha1, a1, d2, q2).subs(dh)
T2_3 = TF_Mat(alpha2, a2, d3, q3).subs(dh)
T3_4 = TF_Mat(alpha3, a3, d4, q4).subs(dh)
# Composition of Homogeneous Transforms
# Transform from Base link to end effector (Gripper)
T0_4 = (T0_1 * T1_2 * T2_3 * T3_4) ## (Base) Link_0 to Link_4


# Total Homogeneous Transform Between (Base) Link_0 and (End Effector) Link_2
# With orientation correction applied

T_total = T0_4

### Numerically evaluate transforms (compare this to output of tf_echo/rviz)
print("\nT0_1 = \n")
pprint(T0_1)
print("\nT1_2 = \n")
pprint(T1_2)
print("\nT2_3 = \n")
pprint(T2_3)
print("\nT3_4 = \n")
pprint(T3_4)
print("\nT0_4 = \n")
pprint(T0_4)


print("\n")
