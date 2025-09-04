#!/usr/bin/env python3
"""
EM-Muscle Control Node (Stub)
Project: NomadLink-MIPA / Exoform
Author: Aaron Dean Whitman (2025)

Description:
This is a placeholder ROS 2 node for controlling a single EM-Muscle actuator pod.
It normalizes incoming joint commands, enforces limits, and outputs current or
position setpoints to a VESC-class motor controller over CAN.

This stub is safe: by default it publishes zero torque.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class EMMuscleControl(Node):
    def __init__(self):
        super().__init__('em_muscle_control')
        # Parameters
        self.declare_parameter('joint_name', 'em_joint_1')
        self.declare_parameter('deg_limit_low', -45.0)
        self.declare_parameter('deg_limit_high', 45.0)
        self.declare_parameter('vel_limit_dps', 90.0)

        self.joint_name = self.get_parameter('joint_name').value
        self.lo = self.get_parameter('deg_limit_low').value
        self.hi = self.get_parameter('deg_limit_high').value
        self.vel = self.get_parameter('vel_limit_dps').value

        # Sub and pub
        self.sub = self.create_subscription(
            Float32,
            f'/exo/{self.joint_name}/cmd_deg_safe',
            self.cb_cmd,
            10
        )
        self.pub = self.create_publisher(
            Float32,
            f'/exo/{self.joint_name}/setpoint',
            10
        )

        self.last_deg = 0.0
        self.dt = 0.01
        self.create_timer(self.dt, self.loop)

        self.get_logger().info(
            f"EM-Muscle Control Node started for {self.joint_name} "
            f"(limits {self.lo}..{self.hi} deg, vel {self.vel} dps)"
        )

    def cb_cmd(self, msg: Float32):
        self.cmd = float(msg.data)

    def loop(self):
        # Ramp command to respect velocity limits
        target = max(self.lo, min(self.cmd, self.hi))
        step = max(-self.vel*self.dt, min(self.vel*self.dt, target - self.last_deg))
        self.last_deg += step

        out = Float32()
        out.data = self.last_deg
        self.pub.publish(out)

def main():
    rclpy.init()
    node = EMMuscleControl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
