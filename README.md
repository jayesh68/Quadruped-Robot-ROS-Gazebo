# Gait Implementation on a QuadrupedRobot using Forward & Inverse Kinematics

## Project Details
1. The CAD model os a Quadruped robot was designed in SolidWorks and exported as a URDF  to create a ROS package.  
2. The  forward  kinematics  of  the robot  is  simulated  in  RVIZ  using  the  joint  state  publisher  GUI  and  validated  with  the  end  effector coordinates obtained through a python script. The inverse kinematics is validated by 
running  a  python  script  which  computes  the  respective  joint  angles  for  the  end  effector positions previously obtained. 
3. A crawl gait and a trot gait was successfully  simulated  in  Gazebo.


## Project Tasks
1. Creates a 3d SolidWorks assembly of the different parts of the robot. The different parts of the robot include the legs, the body of the robot, the manipulators, and the platform.  
2. Exported the model as a URDF by defining the axes for the different joints as depicted in the above diagram.  
3.  Created a file to launch the robot in RVIZ by establishing  relationships as in the URDF file to perform forward kinematics.
4.  Obtained the end effector values in the RVIZ world frame for all the legs by publishing different angles using the joint state publisher GUI. 
5.  Developed  a  python  script  to  validate  the  forward  kinematics  by  creating  a  DH  table  and computing the transformation matrices as in the RVIZ world frame. 
6.  Validated  the  forward  kinematics  of  the  end  effector  positions  obtained  in RVIZ  with  the  values 
obtained through the python script for different joint angles and observed the differences between the two. 
7.  Developed  a  script  to  compute  the  inverse  kinematics.  Created  a  publisher  script  which 
publishes the end effector positions and a subscriber script to compute the joint angles. 
8. Validated the angles obtained through the scripts with the angles for the different end effector positions in 
RVIZ. 
9. Developed  scripts  to implement gaits for the  robot  in  gazebo. Walk  and trot gaits  were analyzed and 
simulated. 


