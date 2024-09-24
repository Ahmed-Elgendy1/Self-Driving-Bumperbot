#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
import math

class TurtlesimKinematics(object):

    def __init__(self):
        self.pose_turtle1_sub = rospy.Subscriber("/turtle1/pose" , Pose ,self.turtle1callback)
        self.pose_turtle2_sub = rospy.Subscriber("/turtle2/pose" , Pose ,self.turtle2callback)

        self.last_pose_turtle1 = Pose()
        self.last_pose_turtle2 = Pose()


    
    def turtle1callback(self , pose):
        self.last_pose_turtle1 = pose


    def turtle2callback(self , pose):
        self.last_pose_turtle2 = pose

        Tx = self.last_pose_turtle2.x - self.last_pose_turtle1.x
        Ty = self.last_pose_turtle2.y - self.last_pose_turtle1.y

        theta_rad = self.last_pose_turtle2.theta -self.last_pose_turtle1.theta
        theta_deg = theta_rad *180 / 3.14

        rospy.loginfo ("""------------------------------------\n
                      Translation Vector turtle1 -> turtle2\n
                      Tx: %f\n
                      Ty: %f\n
                      Rotation Matrix turtle1 -> turtle2\n 
                      theta (rad): %f\n
                      theta (deg): %f\n
                      |R11   R12|:  |%f %f|\n
                      |R21   R22|   |%f %f|\n""",
                      Tx, Ty, theta_rad, theta_deg,
                      math.cos(theta_rad), -math.sin(theta_rad),
                      math.sin(theta_rad), math.cos(theta_rad))
