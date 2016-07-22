import roslib
roslib.load_manifest('joint_states_listener')
import rospy
from joint_states_listener.srv import ReturnJointStates
import time
import sys

def call_return_joint_states(joint_names):
    rospy.wait_for_service("return_joint_states")
    try:
        s = rospy.ServiceProxy("return_joint_states", ReturnJointStates)
        resp = s(joint_names)
    except rospy.ServiceException, e:
        print "error when calling return_joint_states: %s"%e
        sys.exit(1)
    for (ind, joint_name) in enumerate(joint_names):
        if(not resp.found[ind]):
            print "joint %s not found!"%joint_name
    return (resp.position, resp.velocity, resp.effort)


#pretty-print list to string
def pplist(list):
    return ' '.join(['%2.3f'%x for x in list])


#print out the positions, velocities, and efforts of the right arm joints
if __name__ == "__main__":
    joint_names = ["yumi_joint_1_r", "yumi_joint_2_r", "yumi_joint_3_r", "yumi_joint_4_r", "yumi_joint_5_r", "yumi_joint_6_r", "yumi_joint_7_r", "gripper_r_joint"]

    while(1):
        (position, velocity, effort) = call_return_joint_states(joint_names)
        print "position:", pplist(position)
        print "velocity:", pplist(velocity)
        print "effort:", pplist(effort)
        time.sleep(1)

