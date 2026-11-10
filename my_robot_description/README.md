# Actividad 4: Descripción de un robot mediante URDF/Xacro y Gazebo

## 1. Introducción

En esta actividad se desarrolló una propuesta de descripción de un brazo robótico utilizando ROS 2, URDF y Xacro.

El objetivo principal es comprender la estructura de un robot mediante eslabones y articulaciones, así como conocer las herramientas utilizadas para su visualización y simulación.

Se prepararon archivos de configuración para RViz2 y Gazebo, además de las propiedades geométricas y físicas del modelo.

## 2. Objetivo

Desarrollar la estructura de un paquete ROS 2 que contenga la descripción de un robot con al menos cuatro articulaciones y un efector final, utilizando URDF/Xacro.

## 3. Marco teórico

### Eslabones y articulaciones

Los eslabones, conocidos como links, representan los componentes rígidos que forman un robot.

Las articulaciones, llamadas joints, permiten establecer las conexiones y movimientos entre los diferentes eslabones.

En URDF, los componentes se organizan mediante una estructura jerárquica que describe la relación entre ellos.

### Árbol de transformaciones TF2

TF2 es una herramienta de ROS 2 que permite conocer las posiciones y orientaciones relativas entre los diferentes sistemas de coordenadas de un robot.

Su funcionamiento es importante para representar los movimientos de las articulaciones y calcular la ubicación de los componentes.

### Propiedades inerciales

Las propiedades inerciales permiten describir el comportamiento físico de los eslabones.

Incluyen la masa, el centro de masa y los momentos de inercia.

Estas propiedades son fundamentales para realizar simulaciones físicas estables y calcular correctamente el movimiento del robot.

### Diferencias entre RViz2 y Gazebo

RViz2 es una herramienta de visualización que permite observar el modelo del robot y sus transformaciones.

Gazebo es un simulador que incorpora características físicas como gravedad, colisiones y fuerzas.

Por lo tanto, RViz2 permite inspeccionar la representación del robot, mientras que Gazebo permite estudiar su comportamiento dinámico.

## 4. Desarrollo

Se creó un paquete llamado `my_robot_description`, organizado mediante las carpetas `urdf`, `launch`, `rviz` y `resource`.

El modelo propuesto contiene:

- Una base.
- Cuatro eslabones móviles.
- Cuatro articulaciones revolutas.
- Un efector final.
- Geometrías visuales.
- Geometrías de colisión.
- Propiedades de masa e inercia.

El archivo `robot.urdf.xacro` contiene la descripción del robot.

El archivo `display.launch.py` está diseñado para iniciar RViz2 junto con los nodos `robot_state_publisher` y `joint_state_publisher_gui`.

El archivo `gazebo.launch.py` está diseñado para iniciar Gazebo Sim e insertar el robot mediante `ros_gz_sim`.

## 5. Exploración del sistema

Para comprobar el funcionamiento del robot en un entorno ROS 2, se proponen los siguientes comandos:

**Visualización del árbol TF2:**

`ros2 run tf2_tools view_frames`

**Consulta de transformaciones:**

`ros2 run tf2_ros tf2_echo link_base link_final`

**Consulta del estado de las articulaciones:**

`ros2 topic echo /joint_states`

**Consulta de la descripción del robot:**

`ros2 topic echo /robot_description --once`

Estos comandos quedan pendientes de ejecución.

## 6. Evidencias de ejecución

Se prepararon los archivos necesarios para la descripción del robot y su integración con RViz2 y Gazebo.

Sin embargo, no se contó con un entorno Ubuntu y ROS 2 configurado para ejecutar los simuladores.

Por este motivo, no fue posible obtener las capturas de pantalla de RViz2 y Gazebo ni generar el archivo `frames.pdf` mediante `view_frames`.

El proyecto se entrega como una propuesta de implementación pendiente de validación práctica.

## 7. Preguntas

### a) ¿Por qué un modelo correcto en RViz2 puede colapsar en Gazebo?

Porque RViz2 representa visualmente el robot, mientras que Gazebo realiza cálculos físicos.

Si las masas, inercias, colisiones o restricciones están mal definidas, el robot puede presentar movimientos inestables o colapsar durante la simulación.

### b) ¿Qué función cumplen parent y child dentro de un joint?

La etiqueta `parent` identifica el eslabón padre y `child` identifica el eslabón hijo.

Estas etiquetas permiten establecer la jerarquía cinemática del robot.

En un URDF clásico, la estructura debe formar un árbol sin ciclos, donde cada eslabón, excepto el raíz, tiene un único padre.

### c) ¿Cuál es la ventaja de utilizar macros de Xacro?

Las macros permiten reutilizar código y definir propiedades mediante variables.

Esto reduce la repetición de instrucciones, facilita las modificaciones y mejora la organización de los modelos robóticos.

## 8. Conclusiones

Durante el desarrollo de esta actividad se comprendió la importancia de utilizar URDF y Xacro para representar la estructura de un robot.

Se identificaron los elementos principales de un modelo robótico, como los eslabones, las articulaciones y las propiedades inerciales.

También se comprendió la diferencia entre las herramientas de visualización y simulación utilizadas en ROS 2.

Aunque no fue posible realizar las pruebas de ejecución, se preparó una estructura de archivos que servirá como base para futuras prácticas de simulación robótica.

## 9. Referencias

- ROS 2 Documentation: https://docs.ros.org/
- Gazebo Documentation: https://gazebosim.org/docs
- URDF Tutorials: https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html
- Repositorio de referencia: https://github.com/angelparedes-lab/ProgRob2026B
