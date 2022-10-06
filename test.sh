#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=xuanlong@link.cuhk.edu.hk
#SBATCH --job-name=xl-weiboscraping
#SBATCH --output=scraping.out
#SBATCH --time=72:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1500M

# module load python/3.9.11

# srun python 



nohup scrapy crawl search 