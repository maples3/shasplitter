#!/usr/bin/python3

import argparse
import os

# Handle the CLI arguments
parser = argparse.ArgumentParser(description="Split a large file into smaller files")
parser.add_argument("in_file",
	help="The input file to read.  Must be in Zefania XML format.",
	nargs=1)
parser.add_argument("-o", "--outdir",
	help="The directory to store the output files in.\n"
		+ "Note that the filenames will be all UPPERCASE",
	dest="out_dir",
	default="out/")
parser.add_argument("-n", "--names",
	help="The number of characters to take from the beginning of each line.",
	type=int,
	dest='num_chars',
	default=2)
results = parser.parse_args()

# This dict will contain references to each open file.
# Key will be the first X chars, value will be ref to OPENED file.
outfiles = dict()

# Open the file and read it one line at a time
with open(results.in_file) as input_file:
	for line in input_file:
		outfname = line[:results.num_chars].upper() # out file name (minus .txt)
		if outfname not in outfiles.keys():
			# Open the file for appending and put it in the dict
			outfiles[outfname] = open(out_dir + outfname + ".txt", 'a')
		outfiles[outfname].write(line)

# Close all output files
for f in outfiles:
	print("Closing " + f.name + "... ", end='')
	f.flush()
	os.fsync(f.fileno())
	f.close()
	print("Done!")
