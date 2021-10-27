import docker

# Question: Should we initialize the client within each function, or just have
#           a client variable that gets passed into each function?


# Requires: Initialized docker client
# TO DO:    Check if docker client is initialized, if not then pass an error
def pull_image(client, image) :
    print(f"Pulling {image} image...")

    # Pull the specified image from dockerhub
    # Equivalent to: docker pull <image>
    image = client.images.pull(image)
    print(image.id + '\n')

# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
def run_hello_world(client) :
    #pull_alpine_img(client)
    print("\nStarting new container...")

    print("\nContainer Logs:")
    # Run the hello world container
    # Equivalent to: docker run alpine echo hello world
    print(client.containers.run("alpine", "echo hello world").decode("utf-8"))

# Requires: Initialized docker client,
#           Alpine image pulled and/or available
# TO DO:    Check if docker client is initialized, if not then pass an error
# TO DO:    Check if the image is available, if not then pass an error
def run_detached_hello(client) :
    #pull_alpine_img(client)
    print("\nStarting new detached container...")
    # Run the hellow world container, but this time we detach it and get the logs after
    # Equivalent to: docker run -d alpine echo hello world
    alpine_cont = client.containers.run("alpine", "echo hello world",
                                        detach=True)
    print("\nContainer Logs:")

    # print of the logs of the container
    # Equivalent to: docker logs <container_id>
    print(alpine_cont.logs().decode("utf-8"))
