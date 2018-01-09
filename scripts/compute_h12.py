__author__ = 'Nicholas Harding'

import pandas as pd
import numpy as np
import h5py
import allel
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("hdf5", default=None)
parser.add_argument("out", default=None)
parser.add_argument("--windowsize", "-w", default=500, type=int)
parser.add_argument("--chrom", "-c", default=None, required=True)
parser.add_argument("--samples", required=True)
parser.add_argument("--downsample", "-d", default=None, type=int)
args = parser.parse_args()

with open(args.samples, "r") as reader:
    samples = [x.rstrip() for x in reader.readlines()]

if args.downsample is not None:
    samples = np.random.choice(samples, args.downsample).tolist()
elif len(samples) > 100:
    print("You are running with {0} samples. ".format(len(samples)) + \
          "This may take a long time to run. " + \
          "Consider using the --downsample argument")

fh = h5py.File(args.hdf5, "r")[args.chrom]

def main(callset, use_samples, window_size):

    callset_samples = callset["samples"][:].astype("<S8")
    keep_samples = np.in1d(callset_samples, use_samples)
    gt = allel.GenotypeChunkedArray(callset["calldata/genotype"])
    h = gt.compress(keep_samples, axis=1).to_haplotypes()

    positions = allel.SortedIndex(callset["variants/POS"])

    windows = allel.stats.moving_statistic(positions,
                                           statistic=lambda v: [v[0], v[-1]],
                                           size=window_size + 1, step=None)
    windows = windows.astype("int")

    midpoint = allel.stats.moving_statistic(positions,
                                            statistic=lambda v: v[v.size//2],
                                            size=window_size + 1, step=None)

    h1, h12, h123, h2_h1 = allel.moving_garud_h(
        h, window_size + 1, start=0, stop=None, step=None)

    df = pd.DataFrame.from_items((
         ("midpoint", midpoint),
         ("start", windows[:, 0] ),
         ("stop", windows[:, 1]),
         ("h1", h1),
         ("h12", h12),
         ("h123", h123),
         ("h2_h1", h2_h1)))

    return df

result = main(callset=fh, use_samples=samples, window_size=args.windowsize)
result.to_csv(args.out, sep="\t", index=False)
