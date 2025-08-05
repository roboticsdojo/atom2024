# 🤖 ROS 2 Robot Navigation Package

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Simulated%20in-Gazebo-orange)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20%7C%20Ubuntu-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A ROS 2 package for robot simulation and real-world navigation using SLAM, localization, and joystick/keyboard teleoperation.

---

## 🛠 Installation Requirements

Install the following dependencies:

```bash
# 1. Gazebo (Simulation)
sudo apt install ros-humble-gazebo-ros-pkgs

# 2. Colcon (Build Tool)
sudo apt install python3-colcon-common-extensions

# 3. ROS 2 Control
sudo apt install ros-humble-ros2-control \
                 ros-humble-ros2-controllers \
                 ros-humble-gazebo-ros2-control

# 4. SLAM Toolbox
sudo apt install ros-humble-slam-toolbox

# 5. Navigation2 Stack
sudo apt install ros-humble-navigation2 \
                 ros-humble-nav2-bringup

# 6. Twist Mux
sudo apt install ros-humble-twist-mux

# 7. Gamepad Tools
sudo apt install joystick jstest-gtk evtest

# 8. Joystick (ROS 2 joy package)
ros2 run joy joy_enumerate_devices

# Start the joystick node and echo messages
ros2 run joy joy_node            # Terminal 1
ros2 topic echo /joy             # Terminal 2
```

## 🧪 Running in Simulation
Steps:
```bash
# 1. Launch simulation world
ros2 launch atom_qs launch_sim.launch.py world:=./src/atom_qs/worlds/obstacles.world

# 2. Launch RViz
rviz2

# 3. Teleop with keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args -r /cmd_vel:=/cmd_vel_key

# 4. Launch SLAM
ros2 launch atom_qs online_async_launch.py \
  slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml \
  use_sim_time:=true

# 5. Launch Navigation
ros2 launch atom_qs navigation_launch.py use_sim_time:=true
```

## 🤖 Running on the Actual Robot
### On the Raspberry Pi:
```bash
# 1. Start the LiDAR
ros2 launch sllidar_ros2 view_sllidar_a1_launch.py

# 2. Launch the robot
ros2 launch atom_qs launch_robot.launch.py
```
### On your Laptop:
Option 1: Keyboard Teleop
```bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```
Option 2: Joystick Teleop
```bash
ros2 launch atom_qs joystick.launch.py
```
#### SLAM & Navigation
```bash
# 1. Launch SLAM toolbox
ros2 launch atom_qs online_async_launch.py \
  slam_params_file:=./src/atom_qs/config/mapper_params_online_async.yaml \
  use_sim_time:=true

# 2. Launch Navigation
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=false

# 3. Open RViz
rviz2
```
#### 🗺️ Localization with Prebuilt Map (AMCL)
If using a pre-mapped environment:

```bash
# 1. Open RViz
rviz2

# 2. Start Localization (use_sim_time:=false)
ros2 launch atom_qs localization_launch.py map:=<your_map.yaml>

# 3. Start Navigation (use_sim_time:=false)
ros2 launch atom_qs navigation_launch.py map_subscribe_transient_local:=true
```

⚠️ Note: Only the costmap is updated; the base map remains unchanged.


🙋‍♀️ Questions or Contributions?
Feel free to open an issue or submit a pull request if you want to contribute!
