#!/usr/bin/perl

#---TMUX-CLUSTER---#
#    Version: v1   #
#------------------#

use strict;

if($#ARGV < 0) {
    print "Usage: $0 application.\n";
    print "Applications available: Foo, Bar.\n";
    exit 0;
}

my $session = lc($ARGV[0]);
my $applications = {foo => ["a", "b", "c"],
                    bar => ["d", "e", "f"]};

system("tmux new-window -n $session");

foreach my $server (@{$applications->{$session}}) {
    system("tmux split-window -v \"ssh $server\"");
    system("tmux select-layout tiled");
}

system("tmux kill-pane -t 0");
exec("tmux set-window-option synchronize-panes on"); # exec terminates this script
