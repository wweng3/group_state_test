#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('data_recorder', String, queue_size=10)
    rospy.init_node('number_counter', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    counter = 0

    while not rospy.is_shutdown():
        rospy.loginfo(counter)
        pub.publish(str(counter))
	counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
