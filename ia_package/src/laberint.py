#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import tf

flag = 0
primera = 0
init = Odometry()
yi = 0.0

def callback(msg):
    global flag
    global primera
    global init
    global yi
    (r ,p ,y ) = tf.transformations.euler_from_quaternion([msg.pose.pose.orientation.x ,msg.pose.pose.orientation.y ,msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])
    
    if primera == 0:
        init = msg
        primera = 1
        (ri ,pi ,yi) = tf.transformations.euler_from_quaternion([init.pose.pose.orientation.x,init.pose.pose.orientation.y,init.pose.pose.orientation.z,init.pose.pose.orientation.w])
	    
	
    if ((abs(msg.pose.pose.position.x-init.pose.pose.position.x)) >= 0.5 or abs(msg.pose.pose.position.y-init.pose.pose.position.y) >= 0.5) and flag == 1:
        flag = 10
        primera = 0

    if (abs(y-yi)) >= 1.57 and flag == 2:
        flag = 1
        primera = 0
        
    if (abs(y-yi)) >= 1.57 and flag == 4:
        flag = 1
        primera = 0
        
    if (abs(y-yi)) >= 1.57 and flag == 6:
        flag = 4
        primera = 0

    
rospy.init_node('IA')
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
sub = rospy.Subscriber('/odom', Odometry, callback)
vel = Twist()
rate = rospy.Rate(1)
aux = []
i = 0
flag = 0
seguentCasella = 1

with open("accions.txt", "r") as ins:
    for line in ins:
        aux.append(line)
ins.close()

#Endless loop
while not rospy.is_shutdown():
    
    if flag == 10:
        i = i + 1
        seguentCasella = 1
        if i == len(aux):
            flag = 11
            seguentCasella = 0
    
    if seguentCasella == 1:
        seguentCasella = 0
        if(aux[i] == "forward\n"):
            print("Endavant")
            flag = 1
        elif(aux[i] == "right-forward\n"):
            print("Dreta-Endavant")
            flag = 2
        elif(aux[i] == "left-forward\n"):
            print("Esquerra-Endavant")
            flag = 4
        elif(aux[i] == "180-forward\n"):
            print("Gira180-Endavant")
            flag = 6
        
        
    if flag == 1:
        vel.angular.z = 0.0
        vel.linear.x = 0.2
    elif flag == 2:
        vel.angular.z = -0.3
        vel.linear.x = 0.0
    elif flag == 3:
        vel.angular.z = 0.0
        vel.linear.x = 0.2
    elif flag == 4:
        vel.angular.z = 0.3
        vel.linear.x = 0.0
    elif flag == 5:
        vel.angular.z = 0.0
        vel.linear.x = 0.2
    elif flag == 6:
        vel.angular.z = 0.3
        vel.linear.x = 0.0
    elif flag == 11:
        vel.angular.z = 0.0
        vel.linear.x = 0.0

    pub.publish(vel)
    rate.sleep()
    