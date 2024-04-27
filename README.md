# picbox
Picbox is a preview site for pictures processing.

 ![preview_pic](https://user-images.githubusercontent.com/11898075/162750212-a90e431d-9a78-4429-801f-8f6c95ebafd2.png)

# log
- v2.0 finish: add ocr 
- v1.0 finish: pretty UI
- v0.3 bugfix, gray_img not show
- v0.2 choose example ok 
- v0.1 basic core function achieved

# design
- frontend: jquery
- webserver: flask
- api: flask


# deploy steps
```
mkdir picbox_work 
cd picbox_work

wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh 
bash Miniconda3-py39_4.11.0-Linux-x86_64.sh 
echo "PATH=$PATH:/root/miniconda3/bin" >> ~/.bashrc
su

conda config --set auto_activate_base false
conda init
su

conda create -n py39 python=3.9
conda env list
conda activate py39

apt update
apt-get install ffmpeg libsm6 libxext6 -y
pip install opencv-python Flask

git clone https://github.com/kyshel/picbox.git
cd picbox
bash run_api.sh

open brwoser NOW~
```



# proxy R2L
```
screen ssh  -N -R localhost:1080:localhost:1080  root@x.x.x.x
```