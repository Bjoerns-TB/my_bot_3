import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='pet_ros2_battery_state_pkg',
            executable='pet_battery_state_ina219_node',
            output='screen'
        )
    ])