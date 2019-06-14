#!/usr/bin/python
"""
convery.py converts a pdf to html
"""

import itertools
import os
import re
import sys
import subprocess

if __name__ == "__main__":
	input_file = sys.argv[1]
	output_file = sys.argv[2]

	print "Building docker image..."
	proc = subprocess.Popen(["docker", "build", "--build-arg", "INPUT_PDF=%s" % (input_file), "."], stdout=subprocess.PIPE)
	docker_image_id = proc.communicate()[0][-13:-1]

	print "Converting pdf to html..."
	proc = subprocess.Popen(["docker", "run", "-it", docker_image_id, "./pdf2html.py", input_file], stdout=subprocess.PIPE)
	all_output = proc.communicate()[0]

	print "Cleaning up html..."
	# strip out the garbage before the html
	start_ind = all_output.find("<!DOCTYPE html>")
	ugly_html = all_output[start_ind:]

	# strip out the script tags and the text inside
	stop_str = '</script>'
	start_it = re.finditer('<script>', ugly_html)
	stop_it = re.finditer(stop_str, ugly_html)
	reduced_html = ""
	last = -1
	for start, end in itertools.izip(start_it, stop_it):
		s = start.start()
		e = end.start()
		if last == -1:
			reduced_html = reduced_html + ugly_html[:s]
		else:
			reduced_html = reduced_html + ugly_html[last:s]
		last = e+1
	reduced_html = reduced_html + ugly_html[last:]

	# write the html to file
	with open(output_file, "w") as fh:
		fh.write(reduced_html)

	print "Go to https://duckduckgo.com/?q=html+beautify to beautify the output"
	print "Done!"
