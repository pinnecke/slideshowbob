#
# Copyright 2019 Marcus Pinnecke
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# ----------------------------------------------------------------------------------------------------------------------
# imports
# ----------------------------------------------------------------------------------------------------------------------

import sys
import os
import os.path

# ----------------------------------------------------------------------------------------------------------------------
# the actual script
# ----------------------------------------------------------------------------------------------------------------------

if len(sys.argv) < 2:
	print ("usage: python remove-user.py <full name>")
else:
	full_name = " "
	full_name = full_name.join(sys.argv[1:])
	personal_slide_md = "content/latest/personal/" + full_name + ".md"
	if not os.path.exists("content/latest/personal/" + full_name + ".md"):
		print ("This user does not exists.")
	else:
		os.remove(personal_slide_md)
		print ("User was removed. Do not forget to build the slides again by calling \n\tpython build.py")
