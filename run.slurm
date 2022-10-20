#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=siqihan@cuhk.edu.hk
#SBATCH --job-name=siqi-openalex
#SBATCH --output=scraping.out
#SBATCH --time=72:00:00
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=1500M

sh test.sh
