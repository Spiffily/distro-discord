#!/bin/bash
case $1 in

  "distro")
    pi 10
    ;;

  "de")
    echo $XDG_CURRENT_DESKTOP
    ;;

  "uptime")
    uptime -p
    ;;

  *)
    echo "ERROR: Invalid arguement"
    ;;
esac
