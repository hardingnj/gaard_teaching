#! /bin/bash

source activate bio
python scripts/compute_fst.py \
  /kwiat/vector/ag1000g/release/phase1.AR3.1/haplotypes/specific_regions/PARA/2L_2358158_2431617.vcf.gz \
  output/fst.txt \
  --samplesA samples/phase2.ar1.GW.txt \
  --samplesB samples/phase2.ar1.KE.txt \
  --chrom 2L
