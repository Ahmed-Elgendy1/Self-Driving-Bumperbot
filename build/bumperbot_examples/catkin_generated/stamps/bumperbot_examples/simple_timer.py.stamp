#!/usr/bin/env python3

import rospy


def timerCallback(event = None):
    rospy.loginfo("called timer callback function")


if __name__ == '__main__':

    rospy.init_node('simple_timer')
    duration = rospy.Duration(1)          #the rate in which the callback function to be executed 1 second
    rospy.Timer(duration , timerCallback)
    rospy.spin()
    
