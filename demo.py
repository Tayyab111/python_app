import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer

# MySQL connection details
# host = "localhost" #203.99.181.17"
# user = "root_user"
# password = "ffghj23dd"
# database = "mysql"
import os
host = os.environ['DB_HOST']
user = os.environ['DB_USER']
#password = os.environ["DB_PASSWORD"]
password = "3f6K9oX9"
database = os.environ["DB_NAME"]

# Function to connect to MySQL
def connect_to_mysql():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            return "Connection Established successfully and password issue in container is fixed."
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection and connection.is_connected():
            connection.close()

# HTTP Request Handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Call the MySQL connection function
        message = connect_to_mysql()
        
        # Send HTTP status code
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Send the message as response
        self.wfile.write(message.encode('utf-8'))

# Run the server
def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
