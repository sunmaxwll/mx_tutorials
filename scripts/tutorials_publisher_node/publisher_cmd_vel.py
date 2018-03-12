#!/usr/bin/env python
# license removed for brevity
import rospy

'''
$ rostopic info /turtle1/cmd_vel 
Type: geometry_msgs/Twist

Publishers: None

Subscribers: 
 * /turtlesim (http://aicuijie-usb:34947/)

'''

from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('publisher_Twist', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    cmd_vel_pub = Twist()
    cmd_vel_pub.linear.x = 1
    cmd_vel_pub.linear.y = 0
    cmd_vel_pub.linear.z = 0

    cmd_vel_pub.angular.x = 0
    cmd_vel_pub.angular.y = 0
    cmd_vel_pub.angular.z = 1

    while not rospy.is_shutdown():
        rospy.loginfo("Go go go! turtle is runing!")
        pub.publish(cmd_vel_pub)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
