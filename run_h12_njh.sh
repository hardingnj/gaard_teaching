#! /bin/bash
set -e

source /var/lib/galaxy-server/miniconda3/miniconda3/bin/activate GAARD_35

python scripts/compute_h12.py \
  phase2.AR1/haplotypes/main/hdf5/ag1000g.phase2.ar1.haplotypes.3R.h5 \
  output/UGANDA_h12.txt \
  --samples samples/phase2.ar1.UGgam.txt \
  --chrom 3R \
  --windowsize 300
