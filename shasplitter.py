#!/usr/bin/python3

import argparse
import os
import subprocess

# Handle the CLI arguments
parser = argparse.ArgumentParser(description="Split a large file into smaller files")
parser.add_argument("in_file",
	help="The input file to read.",
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
parser.add_argument("-p", "--progress",
	help="Print out a progress message every x lines",
	type=int,
	dest="progress",
	default=-1
)
results = parser.parse_args()

# If the dir name doesn't have a trailing slash, add it
outDir = results.out_dir
if outDir[-1] != '/':
	outDir = outDir + '/'
# Also make sure it exists
if not os.path.exists(outDir):
	subprocess.run(["mkdir", outDir])

#real_in_file = os.path.abspath(results.in_file)
real_in_file = results.in_file[0]

# This dict will contain references to each open file.
# Key will be the first X chars, value will be ref to OPENED file.
outfiles = dict()

line_count = 0
progress_interval = results.progress

# Open the file and read it one line at a time
with open(real_in_file, 'r') as input_file:
	for line in input_file:
		line_count += 1
		outfname = line[:results.num_chars].upper() # out file name (minus .txt)
		if outfname not in outfiles.keys():
			# Open the file for appending and put it in the dict
			outfiles[outfname] = open(outDir + outfname + ".txt", 'a')
		outfiles[outfname].write(line)

		# Progress message
		if (line_count % progress_interval == 0):
			print("Completed line " + str(line_count))
	print("Finished parsing " + str(line_count) + " lines")


# Close all output files
print("Closing output files...")
for k in outfiles.keys():
	outfiles[k].flush()
	os.fsync(outfiles[k].fileno())
	outfiles[k].close()
	#print(".", end='')
print("Done!")
