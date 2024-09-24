#!/usr/bin/env python3

import rospy
from bumperbot_examples.srv import AddTwoints
import sys


if __name__  == '__main__':
    if len(sys.argv) == 3 :    #to insure that only two numbers is sent to the server
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("requesting" , a , b)
        rospy.wait_for_service('add_two_ints') #to wait for the service add_two_ints is available if it is not running
        add_two_ints = rospy.ServiceProxy('add_two_ints' , AddTwoints) #library used to call a server
        response = add_two_ints(a , b) #the function passes the arguments to the server and retrieve it in a variable
        print('Service response' , response)
    else:
        print("Requested 2 arguments")
        sys.exit(-1)