#!/usr/bin/python3

import argparse

# Handle the CLI arguments
parser = argparse.ArgumentParser(description="Split a large file into smaller files")
parser.add_argument("in_file",
	help="The input file to read.  Must be in Zefania XML format.",
	nargs=1)
parser.add_argument("-o", "--outdir",
	help="The directory to store the output files in.",
	dest="out_dir",
	default="out/")
parser.add_argument("-n", "--names",
	help="The number of characters to take from the beginning of each line.",
	type=int,
	dest='num_chars',
	default=2)
results = parser.parse_args()
