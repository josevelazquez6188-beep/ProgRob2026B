# Actividad 4 - Visualizacion del robot en RViz2
# Este archivo inicia los nodos necesarios para visualizar
# el robot y controlar sus articulaciones.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable


def generate_launch_description():

    # Localizar el paquete del robot
    package_dir = get_package_share_directory(
        'my_robot_description'
    )

    # Ruta del modelo Xacro
    xacro_file = os.path.join(
        package_dir,
        'urdf',
        'robot.urdf.xacro'
    )

    # Ruta de configuracion de RViz2
    rviz_config = os.path.join(
        package_dir,
        'rviz',
        'robot.rviz'
    )

    # Convertir Xacro a URDF
    robot_description = {
        'robot_description': Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file
        ])
    }

    # Publicar las transformaciones del robot
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # Interfaz para mover las articulaciones
    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # Abrir RViz2 con la configuracion personalizada
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz_node
    ])
