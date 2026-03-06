#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
import visualization_msgs.msg

def poses_callback(msg: visualization_msgs.msg.MarkerArray, br: tf2_ros.TransformBroadcaster, origin_id):
        origin_marker: visualization_msgs.msg.Marker = next((marker for marker in msg.markers if marker.id == origin_id), None) 

        if origin_marker is not None:
            
            # create transform
            t = geometry_msgs.msg.TransformStamped()

            t.header.stamp = rospy.Time.now()
            t.header.frame_id = "camera"
            t.child_frame_id = f"aruco_id_{origin_id}"

            t.transform.translation.x = origin_marker.pose.position.x
            t.transform.translation.y = origin_marker.pose.position.y
            t.transform.translation.z = origin_marker.pose.position.z

            t.transform.rotation.x = origin_marker.pose.orientation.x
            t.transform.rotation.y = origin_marker.pose.orientation.y
            t.transform.rotation.z = origin_marker.pose.orientation.z
            t.transform.rotation.w = origin_marker.pose.orientation.w

            br.sendTransform(t)
    

def main():
    rospy.init_node('realsense_aruco_find_transform')
    rospy.loginfo("Find Aruco-Camera transfrom started")

    br = tf2_ros.TransformBroadcaster()

    origin_id = rospy.get_param('~origin_id', default=1)

    rospy.Subscriber('/aruco/marker_poses', visualization_msgs.msg.MarkerArray, poses_callback, br, origin_id)
    rospy.spin()

if __name__ == '__main__':
    main()