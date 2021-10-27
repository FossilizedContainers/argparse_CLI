# Comparison
Pros
* Gooey!

Cons
* no proper nesting of commands by designs
* [deficiencies when it comes to POSIX compliant argument handling](https://click.palletsprojects.com/en/8.0.x/why/) (Do we need this? Just added it to cover our bases)

# Commands
`arglib.py` is the tool with only CLI functionality, `arglib_gui.py` runs the Gooey interface. The only difference between the two files is the `@Gooey` line before main.

## CLI
The following commands are available

Pull an image from docker hub
```
python3 arglib.py pull <image>
```

Run an alpine hello world container
```
python3 arglib.py run hello
```

Run an alpine hello world container detached
```
python3 arglib.py run -d hello
```

## Gooey
```
python3 arglib_gui.py
```

# Setting up Environment

## Virtual Environment
Create the environment in python 3
```
python3 -m venv env
```

Start the environment
```
source env/bin/activate
```
## Docker SDK
```
pip install docker
```

## Avoid having to use sudo with docker
**Note: We will have to figure out how to easily add a user of the tool to the
docker group. What if they don't have sudo access?**

In your command line

Create the docker group
```
sudo groupadd docker
```
Add your user to docker group
```
sudo usermod -aG docker $USER
```

# Quick reference on making a subparser for a subparser
Let's say you want to have the CLI have subcommands similar to
`docker image pull alpine`. You can achieve that by creating a subparser of
your subparser. I do not know the preferred way to do this but this was how I
figured out how to make it. I'll use the image below as the standard.
![image](sample_layout.png)

So first you need to create your parent and regular subparser (the `image` and `container`)
```
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')

image = subparser.add_parser('image')
container = subparser.add_parser('container')
```

Now if you want to add the `pull` option to the image command you can create an
image subparser.
```
image_subparser = image.add_subparsers(dest='img_command')

pull = image_subparser.add_parser('pull')
```

You could then add an argument for pull by adding
```
pull.add_argument('image_name', type=str, required=True)
```
To call this, you would put `presto image pull <image-name>`

# References
* https://realpython.com/command-line-interfaces-python-argparse/
* https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
* https://docs.python.org/3/library/argparse.html
* https://docs.docker.com/engine/api/sdk/examples/
* https://docs.docker.com/engine/api/v1.41/
* https://docker-py.readthedocs.io/en/stable/
