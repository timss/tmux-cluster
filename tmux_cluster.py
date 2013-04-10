#!/usr/bin/env python

import argparse
import getpass
import os
import sys

# Dict of system given as cluster group. Define as needed.
system = {"system1": ["host1", "host2"],
          "system2": ["host3", "host4", "host5"]}


def connect(hosts, user=None, port=None):
    """Connect to list of hosts using ssh.

    Args:
        hosts (list): hosts to connect to.
        user (str): username to connect with.
        port (str): port to connect to.

    Returns:
        True or False.

    """
    raise NotImplementedError


def new_window(session):
    """Make a new window in session.

    Args:
        session (str): tmux-session to make a new window in.

    Returns:
        Window id or False.

    """
    raise NotImplementedError


def systems_hosts(system):
    """Get list of hosts in system.

    Args:
        system (str): name of system used as key in system dict.

    Returns:
        A list of hosts.

    """
    raise NotImplementedError


def python_req():
    """Check if python version 2 and dependencies fulfilled.

    Returns:
        True or False.

    """
    if sys.version_info[:1] != (2,):
        print "Requires Python 2."
        return False

    try:
        __import__(argparse)
    except ImportError:
        print "Tmux cluster requires argparse.\n\
               Argparse became standard as of Python 2.7"
        return False

    return True


def main():
    if not python_req(): sys.exit(1)

    parser = argparse.ArgumentParser(
            usage="Usage: %s system" % os.path.basename(sys.argv[0]), 
            description="Tmux cluster similar to clusterssh.", 
            version="0.1")

    # Newline is horrible
    parser.add_argument("-s", "--system", help="Connect to system defined in config")
    parser.add_argument("-t", "--tmux-session", help="Add new window to session instead of making a new session")
    parser.add_argument("-u", "--user", help="Username used with ssh. Defaults to self", default=getpass.getuser())
    parser.add_argument("-p", "--port", help="Port used with ssh. Defaults to 22", default="22")

    args = parser.parse_args()

    # Check and act according to args


if __name__ == "__main__":
    main()
else:
    print "%s should not be imported as a module." % os.path.basename(sys.argv[0])
    sys.exit(1)
