__author__ = 'Nicholas Harding'

import pandas as pd
import numpy as np
import h5py
import allel
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("vcf", default=None)
parser.add_argument("out", default=None)

parser.add_argument("--windowsize", "-w", default=100000, type=int)
parser.add_argument("--downsample", "-d", default=None, type=int)
parser.add_argument("--chrom", "-c", default=None, required=True)

parser.add_argument("--samplesA", required=True)
parser.add_argument("--samplesB", required=True)

args = parser.parse_args()


with open(args.samplesA, "r") as reader:
    samplesA = [x.rstrip() for x in reader.readlines()]
if args.downsample is not None:
    samplesA = np.random.choice(samplesA, args.downsample).tolist()


with open(args.samplesB, "r") as reader:
    samplesB = [x.rstrip() for x in reader.readlines()]
if args.downsample is not None:
    samplesB = np.random.choice(samplesB, args.downsample).tolist()

fh = allel.read_vcf(args.vcf)

def check_samples(selected, samplesin, label):

    assert len(selected) > 0, "No samples in {0}. Failed.".format(label)
    if len(selected) < len(samplesin):
        print("Not all samples provided in {0} were found. Check your samples file. Found {1}/{2}.".format(
            label, len(selected), len(samplesin)))
    else:
        print("All samples in {0} found. (n = {1})".format(label, len(selected)))


def main(callset, samplesA, samplesB, window_size):

    callset_samples = callset["samples"][:].astype("U8").tolist()

    sa = [callset_samples.index(x) for x in samplesA if x in callset_samples]
    sb = [callset_samples.index(x) for x in samplesB if x in callset_samples]

    check_samples(sa, samplesA, "A")
    check_samples(sb, samplesB, "B")

    positions = allel.SortedIndex(callset["variants/POS"])
    
    last_pos = positions[-1]
    window_starts = np.arange(1, last_pos, window_size, dtype=int)

    df = pd.DataFrame(columns=["start", "stop", "nvar"], index=window_starts)
    df["fst"] = pd.Series(index=window_starts, dtype=float)
    df["start"] = window_starts
    df["stop"] = window_starts + window_size

    gt = allel.GenotypeChunkedArray(callset["calldata/GT"])

    for start in window_starts:
        try:
            loc = positions.locate_range(start, start + window_size - 1) 
        except KeyError:
            df.at[start, "nvar"] = 0
            continue

        g = gt[loc]
        ac1 = g.count_alleles(subpop=sa)
        ac2 = g.count_alleles(subpop=sb)
        
        num, den = allel.stats.hudson_fst(ac1, ac2)
        df.at[start, "fst"] = (np.sum(num) / np.sum(den))
        df.at[start, "nvar"] = num.size

    return df

result = main(callset=fh, samplesA=samplesA, samplesB=samplesB, window_size=args.windowsize)
result.to_csv(args.out, sep="\t", index=False)
