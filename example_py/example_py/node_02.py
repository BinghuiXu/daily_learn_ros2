import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node=Node("node_02")
    node.get_logger().info("I am node 02")
    rclpy.spin(node)#keep node runnng
    rclpy.shutdown()

