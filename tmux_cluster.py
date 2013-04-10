#!/usr/bin/env python

import argparse
import getpass
import os
import sys

# Dict of system given as cluster group. Define as needed.
system = {"system1": ["host1", "host2"],
          "system2": ["host3", "host4", "host5"]}

def connect(hosts):
    """Connect to list of hosts

    Args:
        hosts: a list of hosts
    Returns:
        True or False depending on success
    """
    raise NotImplementedError

def new_window(hosts, session):
    """Make a new window in session

    Args:
        hosts   : a list of hosts
        session : tmux-session to make a new window in
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

def main():
    parser = argparse.ArgumentParser(
            usage="Usage: %s system" % os.path.basename(sys.argv[0]), 
            description="Tmux cluster similar to clusterssh.", 
            version="0.1")

    # Newline is horrible
    parser.add_argument("-s", "--system", help="Connect to system defined in config")
    parser.add_argument("-t", "--tmux-session", help="Add new window to session instead of making a new session")
    parser.add_argument("-u", "--user", help="User used with ssh. Defaults to self", default=getpass.getuser())

    args = parser.parse_args()

    # Check and act according to args

if __name__ == "__main__":
    main()
else:
    print "%s should not be imported as a module." % os.path.basename(sys.argv[0])
    sys.exit(1)
