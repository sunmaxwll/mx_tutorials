#!/usr/bin/env python
# license removed for brevity
import rospy
'''
$ rostopic info /roi
Type: sensor_msgs/RegionOfInterest

Publishers: 
 * /camshift (http://aicuijie-usb:41133/)

Subscribers: None

'''
from sensor_msgs.msg import RegionOfInterest
'''
$ rosmsg show sensor_msgs/RegionOfInterest 
uint32 x_offset
uint32 y_offset
uint32 height
uint32 width
bool do_rectify
'''
def callback(data):
    rospy.loginfo("roi: x : %d y : %d h : %d w : %d",data.x_offset ,data.y_offset ,data.height ,data.width)

def listener():
    rospy.init_node('listener_ROI', anonymous=False)

    rospy.Subscriber("roi", RegionOfInterest, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
