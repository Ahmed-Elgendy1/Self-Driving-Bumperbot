#!/usr/bin/env python3

import rospy
from bumperbot_examples.srv import AddTwoints , AddTwointsResponse


def add_two_intsCallback(req):
    rospy.loginfo("the service is ready to sum %d and %d " , req.a , req.b)
    return AddTwointsResponse(req.a + req.b)





if __name__ == '__main__':
    rospy.init_node("simple_service_server")
    service = rospy.Service("add_two_ints" , AddTwoints , add_two_intsCallback)
    rospy.loginfo("the service is ready to add ints")
    rospy.spin()