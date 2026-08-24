# Import ROS 2 Python library
import rclpy
# Import Node class from ROS 2
from rclpy.node import Node
# Import Twist message type
from geometry_msgs.msg import Twist


# Subscriber Node: listens to movement commands and prints them
class TurtleBotMonitor(Node):
    def __init__(self):
        # Initialize the node with the name 'turtlebot_monitor'
        super().__init__('turtlebot_monitor')

        # Subscribe to /cmd_vel and call listener_callback for every message
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )

        # Print a message when the node starts
        self.get_logger().info('TurtleBot Monitor Node has started.')
        self.get_logger().info('Listening on /cmd_vel...')

    # Called automatically whenever a new Twist message arrives
    def listener_callback(self, msg):
        # Forward/backward speed
        linear_x = msg.linear.x
        # Turning speed
        angular_z = msg.angular.z

        # Print the values in a readable format
        self.get_logger().info(
            f'Linear X: {linear_x} | Angular Z: {angular_z}'
        )


# Main function
def main(args=None):
    # Initialize ROS 2
    rclpy.init(args=args)

    # Create the monitor node
    node = TurtleBotMonitor()

    # Keep the node running to receive and print messages
    rclpy.spin(node)

    # Clean up the node and shut down ROS 2
    node.destroy_node()
    rclpy.shutdown()


# Run main() when this file is executed directly
if __name__ == '__main__':
    main()ذ