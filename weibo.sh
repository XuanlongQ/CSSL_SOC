echo "---start shell command----"
date
pwd
echo "Change to the weibo-search path"
cd /Users/xuanlong/Documents/program/python/src/tam/spider/weibo-search
echo `pwd`
echo $path
git pull
echo "Have updated cookies"
sbatch run.slurm
date
echo "stop shell command"
