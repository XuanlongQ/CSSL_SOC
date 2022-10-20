#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=xuanlong@link.cuhk.edu.hk,yjli@link.cuhk.edu.hk
#SBATCH --job-name=xl-weiboscraping
#SBATCH --output=scraping.out
#SBATCH --time=72:00:00
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1500M

nohup scrapy crawl search 