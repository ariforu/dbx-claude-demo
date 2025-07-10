"""
A simple example of using Claude via the Databricks AI Gateway.
"""

import os
import sys
from dotenv import load_dotenv
from databricks.sdk import WorkspaceClient
from payload import MessagePayload

def main(): 
    # Load environment variables
    load_dotenv()
    host = os.getenv("DATABRICKS_HOST")
    token = os.getenv("DATABRICKS_TOKEN")
    endpoint_name = os.getenv("DATABRICKS_ENDPOINT_NAME", "databricks-claude-3-7-sonnet")
    
    if not host or not token:
        print("Error: DATABRICKS_HOST or DATABRICKS_TOKEN not found in environment variables.")
        print("Please create a .env file with your Databricks credentials or set them as environment variables.")
        sys.exit(1)
    
    # Initialize the Databricks client
    workspace_client = WorkspaceClient(host=host, token=token)
        
    # Define the payload
    payload = MessagePayload(role='user', prompt="Explain the theory of relativity in 2 sentences.", max_tokens=100)

    # Call the endpoint using the WorkspaceClient
    response = workspace_client.serving_endpoints.query(
        name=f"{endpoint_name}", messages=[payload]
    )

    # Display the result
    print("Response from Claude:")
    print(response)

if __name__ == "__main__":
    main()
