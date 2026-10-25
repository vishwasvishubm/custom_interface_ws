import rclpy
from rclpy.node import Node
from custom_interfaces.srv import CalculateArea


class AreaServer(Node):

    def __init__(self):
        super().__init__('area_server')

        self.service = self.create_service(
            CalculateArea,
            'calculate_area',
            self.calculate_area_callback
        )

        self.get_logger().info('Area service is ready!')

    def calculate_area_callback(self, request, response):
        response.area = request.length * request.width

        self.get_logger().info(
            f'Length: {request.length}, '
            f'Width: {request.width}, '
            f'Area: {response.area}'
        )

        return response


def main(args=None):
    rclpy.init(args=args)

    node = AreaServer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
