# ROS Package Installation #

## Windows ##

### Install WSL 2 ###
```bash
# Goto the website - https://learn.microsoft.com/en-us/windows/wsl/install
# Open Windows Powershell with administrator rights.(right-click on the application and click on Run-as Administrator)
# Run the command in pwershell
wsl --install
# Make WSL version 2 as default
wsl --set-default-version 2
```

### Install the docker desktop ###
```bash
# Goto to the Docker website
# Cick on "Docker Desktop for Windows" and run the installation.
https://docs.docker.com/desktop/install/windows-install/

# If you face an error "WSL installation is incomplete"
# Goto the link given in the dialog box in the error.
# Complete step 4 and step 5.
# Restart your PC
```
- **Goto Settings in Docker Desktop application.**
- **Click on Resources and then on WSL Integration.**
- **Make sure that Ubuntu 20.04.5 LTS is switched on**

This will make sure that docker runs on your WSL2 bases Ubuntu 20.04.5 LTS. **Very Important Step**

### Install Ubuntu 20.04 ###
- Install [Ubuntu 20.04.5 LTS](https://apps.microsoft.com/store/detail/ubuntu-20045-lts/9MTTCL66CPXJ?hl=en-us&gl=us) via the Microsoft Store.
- Run and set-up the application.

### Install GWSL ###
- Install [GWSL](https://apps.microsoft.com/store/detail/gwsl/9NL6KD1H33V3?hl=en-us&gl=us) via the Microsoft Store
- Run this application before running ROS GUI-based applications.

# Run ROS package #
1. Run the docker desktop app. make sure it is started.
2. Run the GWSL application.
3. Run the Ubuntu 20.04.5 LTS application.
4. Inside the Ubuntu 20.04.5 LTS terminal, Run the following command 
```bash
# Pull the docker image
docker pull rohan132/franka_emika_panda
# Clone the workspace
git clone https://github.com/rohan-khaire25/Franka_emika_panda.git
# Goto to docker scripts folder and start the docker container.
./run_noetic_image_windows.sh
```
5. Now you are inside the docker image. It has ROS noetic installed.
```bash
# Source the workspace
cd home/catkin_ws/
source devel/setup.bash
```
6. Run the ROS node
```bash
# Launch the ROS node
roslaunch franka_emika_panda franka_model.launch
```

## Ubuntu ##

## Install Docker ##
- Follow the "Install using the repository" approach to install docker using the link below.
- Install the [Docker](https://docs.docker.com/engine/install/ubuntu/) for Ubuntu.

# Run ROS package #
```bash
# Pull the docker image
docker pull rohan132/franka_emika_panda
# Clone the workspace
git clone https://github.com/rohan-khaire25/Franka_emika_panda.git
# Goto to docker scripts folder and start the docker container.
./run_noetic_image.sh
```
5. Now you are inside the docker image. It has ROS noetic installed.
```bash
# Source the workspace
cd home/catkin_ws/ && source devel/setup.bash
```
6. Run the ROS node
```bash
# Launch the ROS node
roslaunch franka_emika_panda franka_model.launch
```









