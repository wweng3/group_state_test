#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16
import time


def talker():
    pub = rospy.Publisher('number_count', Int16, queue_size=10)
    rospy.init_node('number_counter', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    counter = 0
    elapsed_time = 0
    start_time = time.time()
    while elapsed_time < 120:
        rospy.loginfo(counter)
        pub.publish(counter)
	counter += 1
        rate.sleep()
	elapsed_time = time.time() - start_time

    exit()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
