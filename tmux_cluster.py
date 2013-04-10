#!/usr/bin/env python

import argparse
import getpass
import os
import sys

# Dict of system given as cluster group. Define as needed.
system = {"system1": ["host1", "host2"],
          "system2": ["host3", "host4", "host5"]}

def connect(hosts, user=None, port=None):
    """Connect to list of hosts using ssh

    Args:
        hosts: a list of hosts to connect to
        user:  username to connect with
        port:  port to connect with
    Returns:
        True or False depending on success
    """
    raise NotImplementedError

def new_window(hosts, session):
    """Make a new window in session

    Args:
        hosts:   a list of hosts 
        session: tmux-session to make a new window in
    Returns:
        True or False depending on success
    """
    raise NotImplementedError

def systems_hosts(system):
    """Get list of hosts in system
    Args:
        system: name of system used as key in system dict
    Returns:
        a list of hosts
    """
    raise NotImplementedError

# What a horrible function name. Go on. Come up with something better.
def python_info_ok():
    """Check if python version 2 and dependencies fulfilled."""
    if not (2,) <= sys.version_info[:2] < (3,):
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
    if not python_info_ok(): sys.exit(1)

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
