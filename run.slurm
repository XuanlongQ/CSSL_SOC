#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=xuanlong@link.cuhk.edu.hk,yjli@link.cuhk.edu.hk
#SBATCH --job-name=weibo-search-xuanlong
#SBATCH --output=scraping.out
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1500M 

sh test.sh
