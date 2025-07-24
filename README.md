Ensure you have installed all the required libraries:

1. Gazebo
sudo apt install ros-humble-gazebo-ros-pkgs

2. Colcon 
sudo apt install python3-colcon-common-extensions

3. Remap teleop twist 
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

4. ROS2 Control
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control

5. (A.)SLAM
sudo apt install ros-humble-slam-toolbox

(B) Copy the online async config file to your package
cp /opt/ros/humble/share/slam_toolbox/config/mapper_params_online_async.yaml ./src/config/

(C)Launch the file
ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml use_sim_time:=true

6. Install Nav2
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup

Running Nav2 (Yet to add the map)
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=my_map_save.yaml -p use_sim_time:=true

Activate the node:
ros2 run nav2_util lifecycle_bringup map_server

Run AMCL
ros2 run nav2_amcl amcl --ros-args -p use_sim_time:=true

Activate the node
ros2 run nav2_util lifecycle_bringup amcl

7. Twist Mux
sudo apt install ros-humble-twist-mux

Running twist mux
ros2 run twist_mux twist_mux --ros-args --params-file ./src/atom_qs/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped

Remap cmd_vel from teleop_twist_keyboard to cmd_vel_key
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_key

8. To check our gamepad works in Linux, we want to install some useful tools:

sudo apt install joystick jstest-gtk evtest

With the controller connected (e.g. via USB or Bluetooth), we can open a terminal and run evtest.

9. To listen to a joystick with the new drivers, we can use the tools from the joy package. The first one will tell us which controllers ROS can see:

ros2 run joy joy_enumerate_devices

10. ros2 run joy joy_node # <-- Run in first terminal
ros2 topic echo /joy # <-- Run in second terminal

# Running Localisation
Step 1
ros2 launch atom_qs launch_sim.launch.py world:=./src/atom_qs/worlds/dojo2024

Step 2:
rviz2

Step 3:
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel_key

Step 4:
ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml use_sim_time:=true

Step 5: 
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true