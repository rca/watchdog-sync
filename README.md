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

## Configuration options

### WATCHDOG_DEST_DIR=.

When the files should not land in the home directory, but elsewhere:

```
WATCHDOG_DEST_DIR=/path/to/parent/directory watchdog-sync username@hostname
```


### WATCHDOG_DELETE_DEST_FILES=false

Remote files that do not exist locally are preserved by default; to delete them, set to `true`

```
WATCHDOG_DELETE_DEST_FILES=true watchdog-sync username@hostname
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
