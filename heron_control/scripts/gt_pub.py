#!/usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Odometry

def callback(msg):
    br = tf.TransformBroadcaster()
    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation
    br.sendTransform((position.x, position.y, position.z),
                     (orientation.x, orientation.y, orientation.z, orientation.w),
                     rospy.Time.now(),
                     msg.child_frame_id,
                     "world")

def main():
    rospy.init_node('odom_to_tf', anonymous=True)
    rospy.Subscriber("/pose_gt", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()