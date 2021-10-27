import argparse
from docker_commands import *

def main():
    # create the parser
    parser = argparse.ArgumentParser()

    # Create the subparser for `image` and `run`
    # dest= is how we can differentiate which argument is used
    subparser = parser.add_subparsers(dest='command')

    # Creating our different subparsers
    pull       = subparser.add_parser('pull')
    run        = subparser.add_parser('run')

    # ---image pulling command arguments---

    # Sample call: arglib pull <image name>
    pull.add_argument('image_name', type=str)

    # ---container arguments---

    # Runs an alpine hello world container
    # For now this is useless, any string can be passed to it
    # Sample call: arglib run hello
    run.add_argument('run_image', type=str)

    # Adds the option to start the container detached
    # Sample call: arglib run -d
    run.add_argument('-detach', '-d', action='store_true', required=False)

    # Get the arguments
    args = parser.parse_args()


    # Initialize the client
    client = docker.from_env()

    if args.command == 'pull':
        print(f'Pulling {args.image_name} from Dockerhub\n')
        pull_image(client, args.image_name)
    elif args.command == 'run':
        # Get the container flags
        detach_flag = args.detach
        pull_image(client, 'alpine')
        if(detach_flag):
            run_detached_hello(client)
        else:
            run_hello_world(client)

if __name__ == "__main__":
    main()
