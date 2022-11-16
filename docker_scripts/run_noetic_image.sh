#!/usr/bin/env bash
# Necessary to open windows
xhost local:root

docker run \
    -it \
    --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --env="DISPLAY=${DISPLAY}" \
    $MOUNT_LOCAL_REPO \
    --privileged \
    --net=host \
    -v /run/user/$UID/pulse/native:/run/user/$UID/pulse/native \
    -e PULSE_SERVER=unix:/run/user/$UID/pulse/native \
    $RUNTIME \
    -v /dev:/dev \
    --name noetic_franka \
    rohan132/franka_emika_panda bash   
    
#auconav/conav:$AUTOWARE_VERSION_AND_ARCHITECTURE bash

# Here you are dropped into a shell in the container with the ability of
# opening graphical applications
