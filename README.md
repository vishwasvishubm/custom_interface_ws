# ROS 2 Custom Service Interface

Defines a custom service `CalculateArea.srv` (`length`, `width` -> `area`) and a Python server/client that use it.

## Packages

- `custom_interfaces` (ament_cmake): `srv/CalculateArea.srv`
- `area_service` (ament_python): `area_server`, `area_client`

## Requirements

- Ubuntu 24.04, ROS 2 Jazzy

## Build

```bash
cd custom_interface_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Run

Source `install/setup.bash` in every new terminal first.

```bash
# Terminal 1
ros2 run area_service area_server

# Terminal 2
ros2 run area_service area_client 4.0 2.5

# Inspect the interface
ros2 interface show custom_interfaces/srv/CalculateArea
```

## Concepts practised

custom `.srv` interfaces, `rosidl_generate_interfaces`, mixing CMake and Python packages
