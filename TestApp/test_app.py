import json
import logging
import sys
import os
from fastapi import FastAPI, HTTPException
from typing import Optional

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from requestmodel import ContainersModel
# from WebAPIClient.Containers import WebSocketSubscription, JSONPlaceholderClient
# from WebAPIClient.Containers import Containers 
# from Logger.logger_setup import setup_logger

from autobahn.twisted.websocket import connectWS
from twisted.internet import reactor
app = FastAPI()

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

config_path = os.path.join(os.path.dirname(__file__), 'testapp_config.json')
config = load_config(config_path)

# logger = setup_logger(
#     __name__,
#     log_dir=config.get('log_dir'),
#     max_bytes=config.get('max_bytes'),
#     backup_count=config.get('backup_count'),
#     level=logging.getLevelName(config.get('log_level', 'INFO'))
# )

# Mock library interaction for container management
class ContainerLibrary:
    @staticmethod
    def create_container(container_data: dict):
        # Logic to create container via server API
        response = Containers.createContainer(endpoint, params)
        return {"message": f"Container '{container_data['name']}' created", "data": container_data}

    @staticmethod
    def update_container(container_data: dict):
        # Logic to update container via server API
        return {"message": f"Container '{container_data['name']}' updated", "data": container_data}

    @staticmethod
    def delete_container(container_data: dict):
        # Logic to delete container via server API
        return {"message": f"Container '{container_data['name']}' deleted", "data": container_data}

@app.get("/v2/containers")
def test_jsonplaceholder(endpoint: str, post_id: Optional[int] = None):
    # Adding 'post_id' as a query parameter if provided
    params = {"id": post_id} if post_id else None

    # Call the library function that interacts with JSONPlaceholder
    response = Containers.getContainer(endpoint, params)

    # Return the response back to the client
    return response
    
@app.post("v2/containers/")
async def handle_container_request(request: ContainersModel, endpoint: str,):
    method = request.method.lower()
    params = request.params or {}
    container_data = params.get("container", {})
    
    # Method handling
    if method == "createcontainer":
        response = ContainerLibrary.create_container(container_data, endpoint)
    elif method == "updatecontainer":
        response = ContainerLibrary.update_container(container_data)
    elif method == "deletecontainer":
        response = ContainerLibrary.delete_container(container_data)
    else:
        raise HTTPException(status_code=400, detail="Invalid method provided")
    
    # Return the JSON-RPC formatted response
    return {
        "id": request.id,
        "jsonrpc": request.jsonrpc,
        "result": response
    }


##############
# def print_menu():
    
#     print("\nInteractive JSONPlaceholder API Test App")
#     print("1. Get all posts")
#     print("2. Get a post by ID")
#     print("3. Create a post")
#     print("4. Update a post")
#     print("5. Delete a post")
#     print("6. Subscribe to topic")
#     print("7. Exit")

# def on_message_received(message):
#     print(f"Received message: {message}")
#     logger.info(f"Received message: {message}")

# def main():
#     client = JSONPlaceholderClient()

#     while True:
#         print_menu()
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             try:
#                 posts = client.get_posts()
#                 print("\nPosts: ")
#                 for post in posts:
#                     print(post)
#             except Exception as e:
#                 print(f"Error: {e}")

#         elif choice == '2':
#             post_id = input("Enter post ID: ")
#             try:
#                 post = client.get_post(post_id)
#                 print("\nPost: ", post)
#             except Exception as e:
#                 print(f"Error: {e}")

#         elif choice == '3':
#             title = input("Enter post title: ")
#             body = input("Enter post body: ")
#             post = {'title': title, 'body': body, 'userId': 1}
#             try:
#                 new_post = client.create_post(post)
#                 print("\nCreated post: ", new_post)
#             except Exception as e:
#                 print(f"Error: {e}")

#         elif choice == '4':
#             post_id = input("Enter post ID to update: ")
#             title = input("Enter new post title: ")
#             body = input("Enter new post body: ")
#             post = {'title': title, 'body': body, 'userId': 1}
#             try:
#                 updated_post = client.update_post(post_id, post)
#                 print("\nUpdated post: ", updated_post)
#             except Exception as e:
#                 print(f"Error: {e}")

#         elif choice == '5':
#             post_id = input("Enter post ID: ")
#             try:
#                 deleted_post = client.delete_post(post_id)
#                 print("\nPost deleted successfully with ID: ",post_id)
#             except Exception as e:
#                 print(f"Error: {e}")

#         elif choice == '6':
#             def stop_reactor():
#                 print("Stopping reactor...")
#                 reactor.stop()

#             # Increase the timeout duration to give more time for the connection to be established and messages to be received
#             TIMEOUT_DURATION = 10  # seconds

#             web_socket = WebSocketSubscription(callback=on_message_received)
#             factory = web_socket.factory
#             factory.protocol = lambda: web_socket  # Pass the instance of WebSocketSubscription
#             connectWS(factory)
#             reactor.callLater(TIMEOUT_DURATION, stop_reactor)
#             reactor.run()

#         elif choice == '7':
#             print("Exiting...")
#             sys.exit(0)

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == '__main__':
#     main()

