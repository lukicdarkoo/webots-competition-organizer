#!/usr/bin/env python3
#
# Copyright 1996-2020 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from controller import Robot


# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Initialize motors
motor_left = robot.getMotor('left wheel motor')
motor_right = robot.getMotor('right wheel motor')
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))
motor_left.setVelocity(0)
motor_right.setVelocity(0)

# Initialize distance sensors
ds = []
for i in range(8):
    sensor = robot.getDistanceSensor(f'ps{i}')
    sensor.enable(timestep)
    ds.append(sensor)

state = 'MOVE'

while robot.step(timestep) != -1:
    ps = [sensor.getValue() for sensor in ds]

    right_obstacle = ps[0] + ps[1] * 0.5
    left_obstacle = ps[7] + ps[6] * 0.5

    if state == 'MOVE':
        left_speed = 3
        right_speed = 3
        if left_obstacle > 300 or right_obstacle > 300:
            if left_obstacle > right_obstacle:
                state = 'AVOID_LEFT'
            else:
                state = 'AVOID_RIGHT'
    if state == 'AVOID_LEFT':
        left_speed = 3
        right_speed = -3
        if left_obstacle < 110:
            state = 'MOVE'
    if state == 'AVOID_RIGHT':
        left_speed = -3
        right_speed = 3
        if right_obstacle < 110:
            state = 'MOVE'

    motor_left.setVelocity(left_speed)
    motor_right.setVelocity(right_speed)
