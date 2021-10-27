# A file to quickly show how to use the functions
from docker_commands import *

# Initialize the client
client = docker.from_env()

#pull_image(client, "alpine")
#run_hello_world(client)
#run_detached_hello(client)

client.containers.prune()
