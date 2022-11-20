echo "---start shell command----"
date
pwd
echo "Change to the weibo-search path"
cd /home/xlqin/workdir/program/tonytam/spiderClub/CSSL_SOC
echo `pwd`
echo $path
git pull
echo "Have updated cookies"
conda activate weibosearch
sbatch run.slurm
date
echo "stop shell command"
