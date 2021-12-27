#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
    
class TurtleBot:
       def __init__(self):
           rospy.init_node('turtlebot_controller', anonymous=True)
           self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
           self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)
           self.goal_pose_subscriber = rospy.Subscriber('/cmd/goal_pose',Pose,self.destination_pose)

           self.goal_pose=Pose()
           self.pose = Pose()
           self.rate = rospy.Rate(10)

       def destination_pose(self,data):
           self.goal_pose=data

       def update_pose(self, data):
           self.pose = data
           
       def distance(self, goal_pose):
           return sqrt(pow((self.goal_pose.x - self.pose.x), 2) +pow((self.goal_pose.y - self.pose.y), 2))
                       
       def linear_vel(self, goal_pose, constant=0.5):
           return constant * self.distance(self.goal_pose)
   
       def angular_vel(self,goal_pose, constant=4):
           return constant * (atan2(self.goal_pose.y - self.pose.y, self.goal_pose.x - self.pose.x) - self.pose.theta)
      
       def move_goal(self):
           vel_msg = Twist()           
           while  not rospy.is_shutdown() :
               vel_msg.linear.x = self.linear_vel(self.goal_pose)
               vel_msg.linear.y = 0
               vel_msg.linear.z = 0
   
               vel_msg.angular.x = 0
               vel_msg.angular.y = 0
               vel_msg.angular.z = self.angular_vel(self.goal_pose)
               
               self.velocity_publisher.publish(vel_msg)
               self.rate.sleep()
   
           vel_msg.linear.x = 0
           vel_msg.angular.z = 0
           self.velocity_publisher.publish(vel_msg)
           rospy.spin()
   
if __name__ == '__main__':
       try: 
           x = TurtleBot()
           x.move_goal()
       except rospy.ROSInterruptException:
           pass
