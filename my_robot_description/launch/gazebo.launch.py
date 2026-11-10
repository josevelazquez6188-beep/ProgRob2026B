# Actividad 4 - Simulacion del robot en Gazebo
# Inicia Gazebo Sim y prepara la insercion del robot.
# Requiere ROS 2, ros_gz_sim y los paquetes del robot.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable


def generate_launch_description():

    # Localizar el paquete de descripcion del robot
    package_dir = get_package_share_directory(
        'my_robot_description'
    )

    # Localizar el archivo Xacro
    xacro_file = os.path.join(
        package_dir,
        'urdf',
        'robot.urdf.xacro'
    )

    # Convertir Xacro a URDF
    robot_description = {
        'robot_description': Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file
        ])
    }

    # Publicar el modelo y las transformaciones
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # Iniciar un mundo vacio en Gazebo Sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    # Insertar el robot desde /robot_description
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_robot',
        output='screen',
        arguments=[
            '-name', 'my_robot',
            '-topic', '/robot_description',
            '-x', '0',
            '-y', '0',
            '-z', '0.5'
        ]
    )

    # Esperar unos segundos antes de insertar el robot
    delayed_spawn = TimerAction(
        period=5.0,
        actions=[spawn_robot]
    )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        delayed_spawn
    ])
