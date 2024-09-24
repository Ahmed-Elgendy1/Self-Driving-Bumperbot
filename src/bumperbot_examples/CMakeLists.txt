cmake_minimum_required(VERSION 3.0.2)
project(bumperbot_examples)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  turtlesim
  geometry_msgs
  tf2_ros
  message_generation
)

catkin_python_setup()

add_service_files(
  FILES
  AddTwoints.srv
  GetTransform.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
  CATKIN_DEPENDS
  turtlesim
  geometry_msgs
  tf2_ros

)



include_directories(

  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS 
Nodes/simple_publisher.py 
Nodes/simple_subscriber.py
Nodes/turtlesim_kinematics_node.py
Nodes/tf_examples_node.py
Nodes/simple_timer.py
Nodes/simple_service_server.py
Nodes/simple_service_client.py

DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})