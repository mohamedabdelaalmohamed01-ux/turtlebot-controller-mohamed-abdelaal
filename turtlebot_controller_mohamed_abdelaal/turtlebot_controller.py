# Import ROS 2 Python library
import rclpy
# Import Node class from ROS 2
from rclpy.node import Node
# Import Twist message type
from geometry_msgs.msg import Twist


# Publisher Node: sends movement commands to the robot
class TurtleBotController(Node):
    def __init__(self):
        # Initialize the node with the name 'turtlebot_controller'
        super().__init__('turtlebot_controller')

        # Create a publisher that sends Twist messages on /cmd_vel
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Twist message used to hold the current movement command
        self.cmd_vel = Twist()

        # Print a message when the node starts
        self.get_logger().info('TurtleBot Controller Node has started.')
        self.get_logger().info('Use W/A/S/D to move, Q to quit.')

    # Convert a keyboard key into a movement command and publish it
    def move_robot(self, key):
        # Reset speeds before applying the new command
        self.cmd_vel.linear.x = 0.0
        self.cmd_vel.angular.z = 0.0

        if key == 'w':          # move forward
            self.cmd_vel.linear.x = 0.1
        elif key == 's':        # move backward
            self.cmd_vel.linear.x = -0.1
        elif key == 'a':        # turn left
            self.cmd_vel.angular.z = 0.1
        elif key == 'd':        # turn right
            self.cmd_vel.angular.z = -0.1
        else:
            # Any other key (or 'q') keeps the robot stopped
            self.get_logger().info('Unknown key, robot stopped.')

        # Publish the Twist message so the robot receives the command
        self.publisher.publish(self.cmd_vel)

        # Print what was sent, useful for testing/demo
        self.get_logger().info(
            f'Sent -> linear.x={self.cmd_vel.linear.x}, angular.z={self.cmd_vel.angular.z}'
        )

    # Publish a stop command (used when quitting)
    def stop_robot(self):
        self.cmd_vel.linear.x = 0.0
        self.cmd_vel.angular.z = 0.0
        self.publisher.publish(self.cmd_vel)
        self.get_logger().info('Robot stopped.')


# Main function
def main(args=None):
    # Initialize ROS 2
    rclpy.init(args=args)

    # Create the controller node
    node = TurtleBotController()

    # Keep asking the user for a command until 'q' is entered
    while rclpy.ok():
        key = input('Enter w/a/s/d or q to quit: ').lower()

        if key == 'q':
            node.stop_robot()
            break

        node.move_robot(key)

    # Clean up the node and shut down ROS 2
    node.destroy_node()
    rclpy.shutdown()


# Run main() when this file is executed directly
if __name__ == '__main__':
    main()