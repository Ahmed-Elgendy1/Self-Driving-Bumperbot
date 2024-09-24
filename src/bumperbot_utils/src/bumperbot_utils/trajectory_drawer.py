#!/usr/bin/env python3

import rospy 
from nav_msgs.msg import Odometry , Path
from geometry_msgs.msg import PoseStamped



class trajectoryDrawer (object):

    def __init__(self):

        self.odom_sub = rospy.Subscriber("/bumperbot_controller/odom" , Odometry , self.OdomCallback)
        self.path_pub = rospy.Publisher("/bumperbot_controller/trajectory" , Path , queue_size=10)
        self.trajectory = Path()


    def OdomCallback(self , msg):
        current_position = PoseStamped()
        current_position.header.frame_id = msg.header.frame_id
        current_position.pose = msg.pose.pose
        current_position.header.stamp = msg.header.stamp
        
        self.trajectory.header.stamp = current_position.header.stamp
        self.trajectory.header.frame_id = current_position.header.frame_id
        self.trajectory.poses.append(current_position)

        self.path_pub.publish(self.trajectory)

