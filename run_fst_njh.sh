#! /bin/bash

#! /bin/bash

source /var/lib/galaxy-server/miniconda3/miniconda3/bin/activate GAARD_35

python /GAARD/selection/scripts/compute_fst.py \
  phase2.AR1/variation/main/vcf/pass/ag1000g.phase2.ar1.pass.3L.vcf.gz \
  output/BF_gam-vs-col_fst.txt \
  --samplesA samples/phase2.ar1.BFcol.txt \
  --samplesB samples/phase2.ar1.BFgam.txt \
  --windowsize 25000 \
  --chrom 3L \
  --downsample 50

# {1}. Replace this with the name of your output file. Use the names of the 2 populations you are comparing. 
# The file should have the '.txt' ending

# {2} / {3} Replace these with the files listing the populations you have chosen to compare fst between.
# These files are found in the samples directory.

# {4} The window size in base pairs in which to calculate Fst. Somewhere between 5000 and 100000 is appropriate.
