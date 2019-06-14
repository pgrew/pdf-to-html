#!/usr/bin/python
"""
pdf2html.py converts a pdf to html and prints the output to stdout
"""

import os
import subprocess
import sys

if __name__ == "__main__":
	pdf = sys.argv[1]
	# convert pdf to html
	file_name = os.path.basename(pdf)
	DEVNULL = open(os.devnull, 'w')
	#convert_proc = subprocess.Popen(["pdf2htmlEX", "--zoom", "1.3", file_name], stdout=DEVNULL)
	convert_proc = subprocess.Popen(["pdf2htmlEX", file_name], stdout=DEVNULL)
	convert_proc.communicate()
	DEVNULL.close()

	# print the prettified html
	output_file_name = file_name[:-4] + ".html"
	cat_proc = subprocess.Popen(["cat", output_file_name], stdout=subprocess.PIPE)
	html_output = cat_proc.communicate()[0]
	print html_output
