cmake_minimum_required(VERSION 3.0.2)
project(bumperbot_localization)


find_package(catkin REQUIRED COMPONENTS
  rospy
  nav_msgs
  sensor_msgs
)

catkin_python_setup()


catkin_package(
  CATKIN_DEPENDS
    nav_msgs
    sensor_msgs

)


include_directories(

  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
  Nodes/kalman_filter_node.py
  Nodes/imu_republisher_node.py

  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)