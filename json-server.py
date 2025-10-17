import sqlite3
import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status
from views import get_all_orders

class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for Kneel-Diamonds"""
    pass

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = 'hi'
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":

            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else:
            return self.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8088
    print(f"Server starting on http://localhost:{port}")
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()