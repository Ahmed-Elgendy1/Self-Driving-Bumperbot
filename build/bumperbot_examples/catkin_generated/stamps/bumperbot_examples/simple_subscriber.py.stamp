#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(self):
    rospy.loginfo("Be carefull sergeant %s", self.data)




if  __name__ == '__main__':
    rospy.init_node("simple_sub_python" , anonymous=True)
    rospy.Subscriber("chatter" , String , callback)
    rospy.spin()