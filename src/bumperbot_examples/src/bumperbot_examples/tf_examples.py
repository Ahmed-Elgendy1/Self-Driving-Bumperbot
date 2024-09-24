#!/usr/bin/env python3

import rospy
from tf2_ros import StaticTransformBroadcaster , TransformBroadcaster , TransformListener , Buffer
from geometry_msgs.msg import TransformStamped
from bumperbot_examples.srv import GetTransform , GetTransformResponse
from tf.transformations import quaternion_from_euler , quaternion_multiply , quaternion_inverse

class TfExamples(object):

    def __init__ (self):
        self.static_broadcaster = StaticTransformBroadcaster()
        self.static_transform_stamped = TransformStamped()
        self.dynamic_broadcaster = TransformBroadcaster()
        self.dynamic_transform_stamped = TransformStamped()

        self.timer = rospy.Timer(rospy.Duration(0.1) , self.timerCallback)
        self.x_increment = 0.05
        self.x_last = 0
        self.rotations_counter = 0


        self.static_transform_stamped.header.stamp = rospy.Time.now()

        self.static_transform_stamped.header.frame_id = "bumperbot_base"
        self.static_transform_stamped.child_frame_id = "bumperbot_top"

        self.static_transform_stamped.transform.translation.x = 0
        self.static_transform_stamped.transform.translation.y = 0
        self.static_transform_stamped.transform.translation.z = 0.3

        self.static_transform_stamped.transform.rotation.x = 0
        self.static_transform_stamped.transform.rotation.y = 0
        self.static_transform_stamped.transform.rotation.z = 0
        self.static_transform_stamped.transform.rotation.w = 1

        self.static_broadcaster.sendTransform(self.static_transform_stamped)
        rospy.loginfo("publishing static transform between %s and %s" , self.static_transform_stamped.header.frame_id ,
                      self.static_transform_stamped.child_frame_id)
        
        self.get_transform_srv = rospy.Service("get_transform" , GetTransform , self.getTransformCallback)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer)

        self.last_orientation = quaternion_from_euler(0 , 0 , 0)
        self.orientation_increment = quaternion_from_euler(0 , 0 , 0.05)

        

    def timerCallback(self , event):
        self.dynamic_transform_stamped.header.frame_id = "odom"
        self.dynamic_transform_stamped.child_frame_id = "bumperbot_base"

        self.dynamic_transform_stamped.header.stamp = rospy.Time.now()

        self.dynamic_transform_stamped.transform.translation.x = self.x_last + self.x_increment
        self.dynamic_transform_stamped.transform.translation.y = 0
        self.dynamic_transform_stamped.transform.translation.z = 0
        
        # self.dynamic_transform_stamped.transform.rotation.x = 0
        # self.dynamic_transform_stamped.transform.rotation.y = 0
        # self.dynamic_transform_stamped.transform.rotation.z = 0
        # self.dynamic_transform_stamped.transform.rotation.w = 1

        q = quaternion_multiply(self.last_orientation , self.orientation_increment)
        

        self.dynamic_transform_stamped.transform.rotation.x = q[0]
        self.dynamic_transform_stamped.transform.rotation.y = q[1]
        self.dynamic_transform_stamped.transform.rotation.z = q[2]
        self.dynamic_transform_stamped.transform.rotation.w = q[3]


        self.dynamic_broadcaster.sendTransform(self.dynamic_transform_stamped)
        self.x_last = self.dynamic_transform_stamped.transform.translation.x
        self.last_orientation = q
        self.rotations_counter += 1

        if self.rotations_counter >= 100:
            self.orientation_increment = quaternion_inverse(self.orientation_increment)
            self.rotations_counter = 0


    def getTransformCallback(self , req):
        rospy.loginfo("requesting transform between %s and %s" , req.frame_id , req.child_frame_id) 
        res = GetTransformResponse()
        requested_transform = TransformStamped()
        try:
            requested_transform = self.tf_buffer.lookup_transform(req.frame_id , req.child_frame_id , rospy.Time())

        except Exception as e:
            rospy.logerr("error while transforming between %s and %s as: %s" , req.frame_id , req.child_frame_id , e)
            res.success = False
            return res
        
        rospy.loginfo ("the requested transform between is %s" , requested_transform)
        res.transform = requested_transform
        res.success = True
        return res
        

            



