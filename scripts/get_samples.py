import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("metadata", default=None)
parser.add_argument("--stem", default=None)
args = parser.parse_args()

df = pd.read_table(args.metadata)

for pop in df.population.unique():
    df.query("population == @pop").ox_code.to_csv(args.stem.format(pop=pop), header=False, index=False)

