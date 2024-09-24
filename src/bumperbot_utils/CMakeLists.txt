cmake_minimum_required(VERSION 3.0.2)
project(bumperbot_utils)


find_package(catkin REQUIRED COMPONENTS
  rospy
  nav_msgs
  geometry_msgs
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
  nav_msgs
  geometry_msgs
)

include_directories(

  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
  Nodes/trajectory_drawer_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}

)
