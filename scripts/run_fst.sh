#! /bin/bash

# READ THIS!
# This is the script we will use to compute fst between two populations on chromosome 3L.
# You will need to decide which 2 populations you wish to compare.
# You will also need to choose the name of your output file, and the window size you will use.
# Too small will not be informative as there will be too few variants, too large will give poor resolution.
# READ THE COMMAND BELOW AND REPLACE THE {#} WITH APPROPRIATE INPUT.

source /var/lib/galaxy-server/miniconda3/miniconda3/bin/activate GAARD_35

python /GAARD/selection/scripts/compute_fst.py \
  phase2.AR1/variation/main/vcf/pass/ag1000g.phase2.ar1.pass.3L.vcf.gz \
  output/{1} \
  --samplesA samples/{2} \
  --samplesB samples/{3} \
  --windowsize {4} \
  --chrom 3L \
  --downsample 50

# {1}. Replace this with the name of your output file. Use the names of the 2 populations you are comparing. 
# The file should have the '.txt' ending

# {2} / {3} Replace these with the files listing the populations you have chosen to compare fst between.
# These files are found in the samples directory.

# {4} The window size in base pairs in which to calculate Fst. Somewhere between 5000 and 100000 is appropriate.
