#!/bin/bash
echo "---start shell command----"
date
pwd
echo "Change to the weibo-search path"
cd /home/xlqin/workdir/program/tonytam/spiderClub/CSSL_SOC
echo `pwd`
echo $path
git pull
echo "Have updated cookies"
eval "$(conda shell.bash hook)"
conda activate weibosearch && scrapy crawl search
sbatch run.slurm
date
echo "stop shell command"
