FROM ros:noetic-robot-xenial

#============================================================================================
# RUN AS ROOT

# Install bootstrap tools
RUN apt-get update && apt-get install -y \
    locales \
    bash-completion \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# finish environment setup
RUN locale-gen en_US.UTF-8 
ENV LANG en_US.UTF-8

# quiet the xdg runtime directory warning
ARG XDG_RUNTIME_DIR="/tmp/xdg_runtime_dir"
RUN mkdir -p ${XDG_RUNTIME_DIR} && chmod 777 ${XDG_RUNTIME_DIR}
ENV XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR}

# ROS/Gazebo envs
ENV ROS_MASTER_URI="http://localhost:11311"
ENV QT_X11_NO_MITSHM=1
ENV IGN_IP="127.0.0.1"
#
# setup ROS keys and sources.list for noetic install
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' \
    --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > \
    /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
#RUN apt-get update && apt-get install --no-install-recommends -y 

# bootstrap rosdep
#RUN rosdep init && rosdep update

# install competitor ros packages
# also some common general packages
ENV ROS_DISTRO noetic
RUN apt-get update && apt-get install -y \
    python-catkin-tools ros-noetic-robot-localization ros-noetic-joystick-drivers ros-noetic-grid-map ros-noetic-rosserial-python ros-noetic-rosserial-arduino ros-noetic-usb-cam ros-noetic-multimaster-fkie libusb-dev ipython \
    ros-noetic-ros-base \
    ros-noetic-robot-state-publisher \
    ros-noetic-velocity-controllers \
    ros-noetic-position-controllers \
    ros-noetic-joint-state-publisher \
    ros-noetic-joint-state-controller \
    ros-noetic-compressed-image-transport \
    ros-noetic-rviz \
    ros-noetic-rqt \ 
    #ros-noetic-rqt-common-plugins \ # This creats an anoying bug where it asks for your keyboard type but doesn't seem to accept input from user
    ros-noetic-stereo-image-proc \
    ros-noetic-xacro \
    imagemagick \
    python3-pip \ 
    vim \
    nano \
    tree \
    \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG HOME="/home/carter"
# runtime stuff: bash and entrypoint scripts
RUN mkdir -p ${HOME}/Swarmie
# COPY ./devl ${HOME}/Swarmie

# ======================================================================================================================
# RUN AS END-USER
#
USER ${enduser_name}
ENV HOME="/home/${enduser_name}"

RUN mkdir -p ${HOME}/scripts       && \
    mkdir -p ${HOME}/ros_workspace && \
    mkdir -p ${HOME}/logs          && \
    mkdir -p ${HOME}/.ros          

ENV ROS_HOME="${HOME}/.ros"
#
VOLUME "${HOME}/.ros"
VOLUME "${HOME}/logs"
