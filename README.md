# ShaSplitter

This program takes a single large list of SHA checksums (or any kind of checksum) and splits it
into separate files based on the first few characters to assist in searching vast amounts of data.

Originally intended to make it feasible for an average computer to handle the huge
[Pwned Passwords lists](https://haveibeenpwned.com/Passwords)
 provided by Troy Hunt, but can theoretically be used on any plain-text 
line-based set of data.

## Usage
```
usage: shasplitter.py [-h] [-o OUT_DIR] [-n NUM_CHARS] [-p PROGRESS]
                      [-l LIMIT_FILES]
                      in_file

Split a large file into smaller files. NOTE: Converts everything to UPPERCASE

positional arguments:
  in_file               The input file to read.

optional arguments:
  -h, --help            show this help message and exit
  -o OUT_DIR, --outdir OUT_DIR
                        The directory to store the output files in (default: out/)
  -n NUM_CHARS, --names NUM_CHARS
                        The number of characters to take from the beginning of each line (default: 2)
  -p PROGRESS, --progress PROGRESS
                        Print out a progress message every x lines (default: 1000)
  -l LIMIT_FILES, --limit-files LIMIT_FILES
                        Limit to x number of open files at a time (default: 100)
```
