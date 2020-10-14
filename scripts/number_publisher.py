#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('number_count', Int16, queue_size=10)
    rospy.init_node('number_counter', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    counter = 0

    while not rospy.is_shutdown():
        rospy.loginfo(counter)
        pub.publish(counter)
	counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
