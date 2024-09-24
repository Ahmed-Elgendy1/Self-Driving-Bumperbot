#!/usr/bin/env python3

import rospy
from bumperbot_controller.noisy_controller import NoisyController


if  __name__ == '__main__':
    rospy.init_node('noisy_controller')
    wheel_separation = rospy.get_param('~wheel_separation')
    wheel_radius = rospy.get_param('~wheel_radius')
    controller = NoisyController(wheel_radius , wheel_separation)
    rospy.spin()