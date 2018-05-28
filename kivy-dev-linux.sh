#!/bin/bash
clear
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
read -p "Press enter to continue"

clear
## system dependencies

sudo dpkg --add-architecture i386
sudo apt install -y libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 \
libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 zlib1g:i386

sudo apt install -y openjdk-8-jdk
sudo apt install -y ccache adb apksigner

sudo apt install -y build-essential git python-dev python3-dev libssl-dev \
libcups2-dev libcairo2-dev libsdl2-dev libsdl2-image-dev \
libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev \
libavformat-dev libavcodec-dev zlib1g-dev ffmpeg libsmpeg-dev \
libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
docutils-common docutils-doc sgml-base xclip xml-core xsel \
python-lxml python3-lxml xvfb 

read -p "Press enter to continue"

clear
# get and install miniconda if not exists (not use sudo)
if [ ! -f ./Miniconda3-latest-Linux-x86_64.sh ]; then
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
fi

chmod +x Miniconda3-latest-Linux-x86_64.sh
# run installer, agree, set default location and update PATH in .bashrc
./Miniconda3-latest-Linux-x86_64.sh

# update conda and create kivy virtualenv
cd
~./.bashrc
conda update --all
conda create -n kivy3 pip setuptools requests

read -p "Press enter to continue"

clear
source activate kivy3
pip install cython==0.23 pillow==4.3.0
pip install -r need-install.txt

read -p "Press enter to continue"

clear
# download kivy source code
wget https://github.com/kivy/kivy/archive/master.zip
unzip master.zip

# install from source
cd kivy-master
python setup.py install
pip install kivy-garden

read -p "Press enter to continue"

clear
cd examples/demo/showcase/
python main.py

# Optional - install PyCharm CE
# wget https://download.jetbrains.com/python/pycharm-community-2018.1.2.tar.gz
# extract at /home/develop
