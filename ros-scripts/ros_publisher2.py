#!/usr/bin/env python
import roslib; #roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter2', String)
    rospy.init_node('talker2')
    while not rospy.is_shutdown():
        str = "Hallo Welt %s" % rospy.get_time()
        rospy.loginfo(str)
        pub.publish(String(str))
        rospy.sleep(1.0)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
