#!/usr/bin/env bash
# Necessary to open windows
xhost local:root

docker run \
    -it \
    --rm \
    --env="DISPLAY=${DISPLAY}" \
    $MOUNT_LOCAL_REPO \
    --privileged \
    --net=host \
    -e PULSE_SERVER=unix:/run/user/$UID/pulse/native \
    $RUNTIME \
    -v /dev:/dev \
    --name noetic_franka \
    rohan132/franka_emika_panda bash   

# Here you are dropped into a shell in the container with the ability of
# opening graphical applications
