#!/usr/bin/env python3
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import roboticstoolbox as rtb
from spatialmath import SE3
import numpy as np

def P2P_trajectory():

    rospy.init_node('P2P_trajectory_node')
    panda_joints = ['panda_joint1','panda_joint2','panda_joint3','panda_joint4','panda_joint5'
        ,'panda_joint6','panda_joint7','panda_finger_joint1','panda_finger_joint2']
        
    waypoints_circle=[
                    [ 0.6000,         0,    1.2000],
                    [ 0.5796,    0.1553,    1.2000],
                    [ 0.5196,    0.3000,    1.2000],
                    [ 0.4243,    0.4243,    1.2000],
                    [ 0.3000,    0.5196,    1.2000],
                    [ 0.1553,    0.5796,    1.2000],
                    [ 0.0000,    0.6000,    1.2000],
                    [-0.1553,    0.5796,    1.2000],
                    [-0.3000,    0.5196,    1.2000],
                    [-0.4243,    0.4243,    1.2000],
                    [-0.5196,    0.3000,    1.2000],
                    [-0.5796,    0.1553,    1.2000],
                    [-0.6000,    0.0000,    1.2000],
                    [-0.5796,   -0.1553,    1.2000],
                    [-0.5196,   -0.3000,    1.2000],
                    [-0.4243,   -0.4243,    1.2000],
                    [-0.3000,   -0.5196,    1.2000],
                    [-0.1553,   -0.5796,    1.2000],
                    [-0.0000,   -0.6000,    1.2000],
                    [ 0.1553,   -0.5796,    1.2000],
                    [ 0.3000,   -0.5196,    1.2000],
                    [ 0.4243,   -0.4243,    1.2000],
                    [ 0.5196,   -0.3000,    1.2000],
                    [ 0.5796,   -0.1553,    1.2000],
                    [ 0.6000,   -0.0000,    1.2000],
                    ]
                
    joints_trajectory_points=[]
    panda_rtb = rtb.models.URDF.Panda()
    for i in range(len(waypoints_circle)):
        point = SE3(waypoints_circle[i])
        joints_trajectory_points.append(np.append((panda_rtb.ikine_LM(point))[0] ,[0.4,0.4]  ))
    rospy.loginfo('Inverse Kinematics Solved')
            
    panda_client = actionlib.SimpleActionClient('panda/panda_controller/follow_joint_trajectory',
                                                    FollowJointTrajectoryAction)
    panda_client.wait_for_server()
    rospy.loginfo('Connected to the server')
    rospy.sleep(1)
    for i in range(len(waypoints_circle)):
        trajectory_message = JointTrajectory()
        trajectory_message.joint_names = panda_joints
        trajectory_message.points.append(JointTrajectoryPoint())
        trajectory_message.points[0].positions = joints_trajectory_points[i]
        trajectory_message.points[0].velocities = [0.0 for i in panda_joints]
        trajectory_message.points[0].accelerations = [0.0 for i in panda_joints]
        trajectory_message.points[0].time_from_start = rospy.Duration(2.5)
        goal_positions = FollowJointTrajectoryGoal()
        goal_positions.trajectory = trajectory_message
        goal_positions.goal_time_tolerance = rospy.Duration(0)
        panda_client.send_goal(goal_positions)
        rospy.sleep(2)

   


if __name__ == '__main__':
    P2P_trajectory()