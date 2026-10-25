import sys

import rclpy
from rclpy.node import Node
from custom_interfaces.srv import CalculateArea


class AreaClient(Node):

    def __init__(self):
        super().__init__('area_client')

        self.client = self.create_client(
            CalculateArea,
            'calculate_area'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for the area service...'
            )

    def send_request(self, length, width):
        request = CalculateArea.Request()
        request.length = length
        request.width = width

        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    node = AreaClient()

    length = float(sys.argv[1])
    width = float(sys.argv[2])

    future = node.send_request(length, width)
    rclpy.spin_until_future_complete(node, future)

    response = future.result()

    node.get_logger().info(
        f'Area of {length} × {width} = {response.area}'
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

