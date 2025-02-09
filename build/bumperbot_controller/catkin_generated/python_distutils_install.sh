#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ahmed/bumperbot_ws/src/bumperbot_controller"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ahmed/bumperbot_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ahmed/bumperbot_ws/install/lib/python3/dist-packages:/home/ahmed/bumperbot_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ahmed/bumperbot_ws/build" \
    "/usr/bin/python3" \
    "/home/ahmed/bumperbot_ws/src/bumperbot_controller/setup.py" \
     \
    build --build-base "/home/ahmed/bumperbot_ws/build/bumperbot_controller" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ahmed/bumperbot_ws/install" --install-scripts="/home/ahmed/bumperbot_ws/install/bin"
