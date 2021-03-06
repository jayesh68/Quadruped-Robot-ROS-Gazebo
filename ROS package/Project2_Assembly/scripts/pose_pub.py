#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose

def publisher():
    pub = rospy.Publisher('pose', Pose, queue_size=1)
    rospy.init_node('pose_publisher', anonymous=True)
    rate = rospy.Rate(2) # Hz
    while not rospy.is_shutdown():
        p = Pose()
        p.position.x =  -0.112
        p.position.y = -0.1016
        p.position.z = -0.1989
        # Make sure the quaternion is valid and normalized
        p.orientation.x = -0.5264
        p.orientation.y = -0.47204
        p.orientation.z = -0.47204
        p.orientation.w = 0.5264
        pub.publish(p)
	print(p)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy:
        pass
