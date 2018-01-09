#! /bin/bash
set -e

# READ THIS!
# This is the script we will use to compute h12 on chromosome 3R.
# You will need to decide which population to evaluate
# You will also need to choose the name of your output file, and the window size you will use.
# The window size (in SNPs is very important) 
# Too small will not be informative as there will be insufficient SNPs to seperate haplotypes
# too large will mean no haplotypes are identical.
# READ THE COMMAND BELOW AND REPLACE THE {#} WITH APPROPRIATE INPUT.

source /var/lib/galaxy-server/miniconda3/miniconda3/bin/activate GAARD_35

python scripts/compute_h12.py \
  phase2.AR1/haplotypes/main/hdf5/ag1000g.phase2.ar1.haplotypes.3R.h5 \
  output/{1} \
  --samples samples/{2} \
  --chrom 3R \
  --windowsize {3}

# {1}. Replace this with the name of your output file. Use the name of the population you are using. 
# The file should have the '.txt' ending

# {2} Replace this with the file listing the population you have chosen 
# These files are found in the samples directory.

# {3} The window size in SNPs which to calculate Fst. 
# 300 is appropriate for populations with high diversity. Ask if unsure.
