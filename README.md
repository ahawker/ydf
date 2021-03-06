# ydf

[![Build Status](https://travis-ci.org/ahawker/ydf.svg?branch=master)](https://travis-ci.org/ahawker/ydf)
[![Test Coverage](https://codeclimate.com/github/ahawker/ydf/badges/coverage.svg)](https://codeclimate.com/github/ahawker/ydf/coverage)
[![Code Climate](https://codeclimate.com/github/ahawker/ydf/badges/gpa.svg)](https://codeclimate.com/github/ahawker/ydf)
[![Issue Count](https://codeclimate.com/github/ahawker/ydf/badges/issue_count.svg)](https://codeclimate.com/github/ahawker/ydf)

[![PyPI Version](https://badge.fury.io/py/ydf.svg)](https://badge.fury.io/py/ydf)
[![PyPI Versions](https://img.shields.io/pypi/pyversions/ydf.svg)](https://pypi.python.org/pypi/ydf)

[![Updates](https://pyup.io/repos/github/ahawker/ydf/shield.svg)](https://pyup.io/repos/github/ahawker/ydf/)

YAML to Dockerfile.

### Status

This package is maintained and under active development.

It will, to the best of my ability, respect the patterns of [Semantic Versioning](http://semver.org/).
Most importantly, this means than until the package version reaches `1.0.0`, any and all defined API's are subject to potential changes.

### Why?

Why not?

Although I have some imagined future use cases for a library such as this, the hope is that some nice YAML
features like `node anchors` could be leveraged for Dockerfile instructions that are often copy/pasted.

### Installation

To install ydf from [pip](https://pypi.python.org/pypi/pip):
```bash
    $ pip install ydf
```

To install ydf from source:
```bash
    $ git clone git@github.com:ahawker/ydf.git
    $ python setup.py install
```

### Usage

Let's take a look at a basic "Hello World" YAML file.

```bash
⇒  cat examples/readme/hello-world.yaml
meta:
  relpath: "examples/readme/hello-world.yaml"
  description: "A basic YAML file that prints 'Hello World' stdout when run"

instructions:
  - from:
      image: "alpine"
      tag: "latest"
  - label:
      maintainer: "andrew.r.hawker@gmail.com"
      version: "0.0.1"
      url: "https://github.com/ahawker/ydf/examples/readme/hello-world.yaml"
  - env:
      YDF: "1"
  - cmd: "echo Hello World"
```

It defines two top level blocks, `meta` and `instructions`.

The `meta` block just contains optional key/value pairs that you with to be emitted at the top of the Dockerfile as it's generated.

The `instructions` block is where the real meat is. `instructions` is a block that defines a list of blocks that map
to individual `Dockerfile` instructions. A full list can be found in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

From this "hello-world.yaml" file, we can generate a Dockerfile.

```bash
⇒  python ydf examples/readme/hello-world.yaml
# Automatically generated by ydf
# Version: 0.0.1
# ---
# Relpath: examples/readme/hello-world.yaml
# Description: A basic YAML file that prints 'Hello World' stdout when run
# ---

FROM alpine:latest

LABEL "maintainer"="andrew.r.hawker@gmail.com" \
      "version"="0.0.1" \
      "url"="https://github.com/ahawker/ydf/examples/readme/hello-world.yaml"

ENV YDF=1

CMD echo Hello World
```

Now that we see what it has generated, let's build it.

```bash
⇒  python ydf examples/readme/hello-world.yaml | docker build --tag hello-world-example -
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM alpine:latest
 ---> 4a415e366388
Step 2/4 : LABEL "maintainer" "andrew.r.hawker@gmail.com" "version" "0.0.1" "url" "https://github.com/ahawker/ydf/examples/readme/hello-world.yaml"
 ---> Using cache
 ---> 9e9b958c787c
Step 3/4 : ENV YDF 1
 ---> Using cache
 ---> 2dee18896d5c
Step 4/4 : CMD echo Hello World
 ---> Using cache
 ---> 8f1ab6aa3699
Successfully built 8f1ab6aa3699
Successfully tagged hello-world-example:latest
```

Now we have a local image with the "hello-world-example" tag.

```bash
⇒  docker images
REPOSITORY                            TAG                 IMAGE ID            CREATED             SIZE
hello-world-example                   latest              8f1ab6aa3699        14 minutes ago      3.99MB
```

Running this image will print "Hello World" to stdout.

```bash
⇒  docker run --rm hello-world-example
Hello World
```

### Contributing

If you would like to contribute, simply fork the repository, push your changes and send a pull request.
Pull requests will be brought into the `master` branch via a rebase and fast-forward merge with the goal of having
a linear branch history with no merge commits.

Example:
```bash
# Bring source of pull request to local machine.
$ git remote add <name> <url>
$ git fetch <name>

# Confirm local master is up-to-date.
$ git checkout master && git pull --rebase

# Checkout local branch for pull request source and rebase it with master.
$ git checkout -b <pr-branch> <name>/<pr-branch>
$ git rebase master

# Fast-forward merge the pull request into master.
$ git checkout master && git merge <pr-branch>

# Push merged pull request to remote master. If this is Github, it should automatically close
# the pull request.
$ git push origin master
```

### License

The ydf package is available under the [Apache 2.0](LICENSE) license.
