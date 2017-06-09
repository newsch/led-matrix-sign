# led-matrix-sign
code used to control a 192x16 led sign with a raspberry pi

## Getting Started
1. Clone the project
```shell
$ git clone https://github.com/newsch/led-matrix-sign.git
```

2. Setup the submodule (more reading on git submodules [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules))
```bash
$ git submodule init
$ git submodule update
```

3. Make and install the relevant python libraries
build the python3 library according to @hzeller's [instructons](https://github.com/newsch/rpi-rgb-led-matrix/blob/master/python/README.md)
```bash
$ cd rpi-rgb-led-matrix/
$ sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
$ make build-python PYTHON=$(which python3)
$ sudo make install-python PYTHON=$(which python3)
```
