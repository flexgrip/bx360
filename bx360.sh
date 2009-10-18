#!/bin/bash

growisofs -use-the-force-luke=dao -use-the-force-luke=break:1913760  -dvd-compat -speed="$3" -Z "$1"="$2"

wget --spider "http://$5/xbmcCmds/xbmcHttp?command=ExecBuiltIn(Notification(Finished!,360%20backup%20complete...,5000,$4))"
