#!/usr/bin/env python

import rospy
import smach
import smach_ros
from std_msgs.msg import Int16, String
import time
import threading
import numpy


# define state Foo
class LastNum(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['continue', 'done'],
                             input_keys=['sm_counter_in'],
                             output_keys=['sm_counter_out'])
	self.myvar = None
        self.sub = rospy.Subscriber("number_count", Int16, self.callback)
        self.pub = rospy.Publisher("data_recorder", String, queue_size=20)

    def callback(self, data):
        self.myvar = data

    def execute(self, userdata):
        rate = rospy.Rate(10)
        if userdata.sm_counter_in < 21:
            num = str(self.myvar)
            out = num[-1]
            rospy.loginfo('Counter = ' + str(userdata.sm_counter_in))
            rospy.loginfo(num)
            rospy.loginfo("last num: " + out + '\n')
            self.pub.publish(out)
            userdata.sm_counter_out = userdata.sm_counter_in + 1
            rate.sleep()
            return 'continue'
        print
        return 'done'


def main():
    rospy.init_node('last_num_state', anonymous=True)

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['finish'])
    sm.userdata.sm_counter = 0
    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('LastNum', LastNum(),
                               transitions={'continue': 'LastNum',
                                            'done': 'finish'},
                               remapping={'sm_counter_in': 'sm_counter',
                                          'sm_counter_out': 'sm_counter'}
                               )

    # Execute SMACH plan
    outcome = sm.execute()

    # rospy.spin()


if __name__ == '__main__':
    main()

