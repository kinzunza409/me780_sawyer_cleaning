#!/usr/bin/env python3
import rospy
import visualization_msgs.msg

def handler(msg: visualization_msgs.msg.MarkerArray):
    pass

def main():
    rospy.init_node('realsense_aruco_pose_wrt_base')
    rospy.loginfo("Find Aruco-Base pose started")

    rospy.Subscriber('/aruco/marker_poses', visualization_msgs.msg.MarkerArray, handler)
    rospy.spin()

if __name__ == '__main__':
    main()