#!/usr/bin/env python
# license removed for brevity
import rospy
'''
$ rostopic info /turtle1/cmd_vel 
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /turtlesim (http://usb-desktop:40195/)

'''
'''
$ rosmsg list | grep Twist
geometry_msgs/Twist
geometry_msgs/TwistStamped
geometry_msgs/TwistWithCovariance
geometry_msgs/TwistWithCovarianceStamped
'''
from geometry_msgs.msg import Twist
'''
$ rosmsg show geometry_msgs/Twist
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
'''
def callback(data):
    rospy.loginfo("leaner: x : %d y : %d z : %d",data.linear.x ,data.linear.y ,data.linear.z)
    rospy.loginfo("angular: x : %d y : %d z : %d",data.angular.x ,data.angular.y ,data.angular.z)

def listener():
    rospy.init_node('listener_Twist', anonymous=False)

    rospy.Subscriber("cmd_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()

