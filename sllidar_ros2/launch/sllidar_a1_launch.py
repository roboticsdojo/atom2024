#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    channel_type = LaunchConfiguration('channel_type', default='serial')
    serial_port = LaunchConfiguration('serial_port', default='/dev/ttyUSB0')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='115200')
    frame_id = LaunchConfiguration('frame_id', default='laser')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Standard')
    range_min = LaunchConfiguration('range_min', default='0.15')
    topic_name = LaunchConfiguration('topic_name', default='scan')
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'channel_type',
            default_value=channel_type,
            description='Specifying channel type of lidar'),
        
        DeclareLaunchArgument(
            'serial_port',
            default_value=serial_port,
            description='Specifying usb port to connected lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate to connected lidar'),
        
        DeclareLaunchArgument(
            'frame_id',
            default_value=frame_id,
            description='Specifying frame_id of lidar'),

        DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data'),
            
        DeclareLaunchArgument(
            'scan_mode',
            default_value=scan_mode,
            description='Specifying scan mode of lidar'),

        DeclareLaunchArgument(
            'range_min',
            default_value=range_min,
            description='Minimum valid measurement distance (meters)'),
            
        DeclareLaunchArgument(
            'topic_name',
            default_value=topic_name,
            description='Output topic name for scan data'),
        
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='static_tf_pub_laser_to_base',
        #     arguments=['0', '0', '0.15', '0', '0', '0', 'base_link', 'laser'],
        #     output='screen'
        # ),


        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node',
            parameters=[{
                'channel_type': channel_type,
                'serial_port': serial_port, 
                'serial_baudrate': serial_baudrate, 
                'frame_id': frame_id,
                'inverted': inverted, 
                'angle_compensate': angle_compensate,
                'scan_mode': scan_mode,
                'range_min': range_min,
                'topic_name': topic_name
            }],
            output='screen',
            arguments=['--ros-args', '--log-level', 'debug']  # Add debug output
        )
    ])