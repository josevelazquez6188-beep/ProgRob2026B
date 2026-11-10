# Actividad 4 - Configuracion de instalacion del paquete ROS 2
# Incluye los modelos URDF/Xacro y archivos de lanzamiento.

import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.1',

    # Archivos que se instalaran con el paquete
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*')
        ),
        (
            os.path.join('share', package_name, 'rviz'),
            glob('rviz/*')
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='Estudiante',
    maintainer_email='estudiante@example.com',

    description='Descripcion de un brazo robotico con URDF/Xacro',

    license='Apache-2.0',

    tests_require=['pytest'],

    entry_points={
        'console_scripts': [],
    },
)
