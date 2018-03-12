#!/usr/bin/env python
# license removed for brevity
import rospy
'''
usb@usb-desktop:~$ rostopic info /odom 
Type: nav_msgs/Odometry

Publishers: 
 * /gazebo (http://usb-desktop:39466/)

Subscribers: None
'''
from nav_msgs.msg import Odometry

'''
usb@usb-desktop:~$ rosmsg show nav_msgs/Odometry 
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string child_frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
geometry_msgs/TwistWithCovariance twist
  geometry_msgs/Twist twist
    geometry_msgs/Vector3 linear
      float64 x
      float64 y
      float64 z
    geometry_msgs/Vector3 angular
      float64 x
      float64 y
      float64 z
  float64[36] covariance

'''
def callback(data):
    rospy.loginfo("position: x : %f y : %f z : %f",data.pose.pose.position.x ,data.pose.pose.position.y ,data.pose.pose.position.z)


def listener():
    rospy.init_node('listener_Odometry', anonymous=False)

    rospy.Subscriber("/odom", Odometry, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()




