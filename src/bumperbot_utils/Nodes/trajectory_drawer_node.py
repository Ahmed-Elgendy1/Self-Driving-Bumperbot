#!/usr/bin/env python3

import rospy
from bumperbot_utils.trajectory_drawer import trajectoryDrawer



if __name__ == '__main__':
    rospy.init_node("trajectory_drawer")
    robot_path = trajectoryDrawer()
    rospy.spin()
