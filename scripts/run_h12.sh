#! /bin/bash
set -e

source activate bio

python scripts/compute_h12.py \
  /kwiat/vector/ag1000g/release/phase2.AR1/haplotypes/main/hdf5/ag1000g.phase2.ar1.haplotypes.3R.h5 \
  output/UGANDA_h12.txt \
  --samples samples/phase2.ar1.UGgam.txt \
  --chrom 3R \
  --windowsize 300
