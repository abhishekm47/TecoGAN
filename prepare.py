import os
from pathlib import Path
from glob import glob
import subprocess
import shutil
import hashlib
import re
import pprint

raw_dataset = "/home/ubuntu/TecoGAN/rawDataset"

hr_dataset_raw = raw_dataset+'/HR'
lr_dataset_raw = raw_dataset+'/LR'

hr_dataset = "/home/ubuntu/TecoGAN/HR_dataset"
lr_dataset = "/home/ubuntu/TecoGAN/LR_dataset"

def _find_filenames(file_dir_path, file_pattern): return list(file_dir_path.glob(file_pattern))


fi = 2000
dir_prefix = "scene"

all_videos = _find_filenames(Path(lr_dataset_raw), '*.mp4')
all_videos = [str(filename) for filename in all_videos]
all_videos.sort(key=lambda f: int(re.sub('\D', '', f)))

for video in all_videos:
    
    frames_dir = os.path.join(lr_dataset, dir_prefix+'_'+str(fi))
    
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir, 0o777)
        
    frames_save_string = frames_dir+ "/col_high_%04d.png"
    
    subprocess.call(['ffmpeg', '-noautorotate', '-i', video, '-f', 'image2', '-q:v', '1', frames_save_string])
    
    fi=fi+1




