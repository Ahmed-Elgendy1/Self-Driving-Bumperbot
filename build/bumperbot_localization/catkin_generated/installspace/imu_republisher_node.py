#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

def ImuCallback(imu):
    imu.header.frame_id = "base_footprint_ekf"
    imu_pub.publish(imu)



if __name__ =='__main__':
    rospy.init_node('imu_republisher_node')
    imu_sub = rospy.Subscriber("imu" , Imu , ImuCallback)
    imu_pub = rospy.Publisher("imu_ekf" , Imu , queue_size=10)
    rospy.spin()