# ROS2 Robot Navigation Package
Ensure you have installed all the required libraries:

## Installation Requirements

```bash
# 1. Gazebo
sudo apt install ros-humble-gazebo-ros-pkgs

# 2. Colcon 
sudo apt install python3-colcon-common-extensions

# 3. ROS2 Control
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control

# 4. SLAM
sudo apt install ros-humble-slam-toolbox

# 5. Install Nav2
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup

# 6. Twist Mux
sudo apt install ros-humble-twist-mux

# 7. To check our gamepad works in Linux, we want to install some useful tools:

sudo apt install joystick jstest-gtk evtest

With the controller connected (e.g. via USB or Bluetooth), we can open a terminal and run evtest.

# 8. To listen to a joystick with the new drivers, we can use the tools from the joy package. The first one will tell us which controllers ROS can see:

ros2 run joy joy_enumerate_devices

# Start the joystick node and check output
10. ros2 run joy joy_node # Terminal 1
ros2 topic echo /joy # Terminal 2

## Running Localisation in simulation
#Step 1
ros2 launch atom_qs launch_sim.launch.py world:=./src/atom_qs/worlds/obstacles

#Step 2:
rviz2

#Step 3:
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_key

#Step 4:
ros2 launch atom_qs online_async_launch.py slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml use_sim_time:=true

#Step 5: 
ros2 launch atom_qs navigation_launch.py use_sim_time:=true

#Launching the actual robot:
In the Pi launch the following:

#1. LiDAR Node: 
ros2 launch sllidar_ros2 view_sllidar_a1_launch.py

#2. Actual launch file: 
ros2 launch atom_qs launch_robot.launch.py


#On your laptop run: 
#1. Teleop with keyboard: 
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

#Alternatively you can run if connected to a joystick: 
ros2 launch atom_qs joystick.launch.py

#2. Launch slam_toolbox: 
ros2 launch atom_qs online_async_launch.py slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml use_sim_time:=true

# 3. Launch Navigation: 
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false

#4. Final step : Launch rviz with 
rviz2 

#If not using slam_toolbox and using AMCL instead follow these steps from step 2:

#2. To start localization: 
ros2 launch atom_qs localization_launch.py map:=./ (enter name of map here(should be .yaml))

#3. To start Navigation: 
ros2 launch atom_qs navigation_launch.py map_subscribe_transient_local:=true

⚠️ Note: The base map will not be updated in this mode—only the costmap is dynamically updated during navigation.