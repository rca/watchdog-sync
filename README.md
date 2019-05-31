# watchdog-sync

wrapper around Python's watchdog to keep a local directory in sync on a remote server/device

This script assumes you have SSH access to the remote system and `rsync` is installed on your local and remote system.


# Usage

The command below will watch the local `project` directory and (semi-) immediately push changes to the directory named
`project` in the remote `username`'s home directory:

```
cd /path/to/project
watchdog-sync username@hostname
```


# Installation

To install clone this directory, and then:

```
cd /path/to/watchdog-sync
pip install .
```

## Inside a virtual environment

Make sure you have `pipenv` installed.

```
pipenv shell
pipenv install

pip install -e .
```
