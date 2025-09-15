Requirement：opencv 2.x.x & python 2.7
*Todo:*
1. 读取彩色图像，缩放一次，同时显示缩放前后的图像
2. 读取视频文件并播放

*Create conda environment and install dependencies:*
```
conda create -n computer_vision python=2.7
conda activate computer_vision
conda install -c menpo opencv=2.4.11
pip install numpy
```

*Run the following commands to test your code:*
```
python week1_hm_1/src/image_resize_show.py week1_hm_1/src/assets/LenaRGB.bmp
python ffmpeg_pipe_play.py ./week1_hm_1/src/assets/w5.avi [--fps 30]
```

