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

import sys, os, os.path, ntpath
from datetime import date

HISTORY_PATH = "content/history/"
PERSONAL_SLIDE_HISTORY = HISTORY_PATH + "personal/"
SPECIAL_SLIDE_HISTORY = HISTORY_PATH + "special/"

PERSONAL_SLIDE_TEMPLATE = open("src/templates/personal-slides.md", 'r').read()
ADDITIONAL_CONCERNS_SLIDE_TEMPLATE = open("src/templates/additional-concerns.md", 'r').read()
SPECIAL_ANNOUNCEMENTS_SLIDE_TEMPLATE = open("src/templates/special-announcements.md", 'r').read()

# ----------------------------------------------------------------------------------------------------------------------
# the actual script
# ----------------------------------------------------------------------------------------------------------------------

def archive_content(md_file_dir_dst, md_file_dir_src, md_file_name, commit_name, content_template):
	md_file_fullpath_dst = md_file_dir_dst + md_file_name
	if not os.path.exists(md_file_fullpath_dst):
		open(md_file_fullpath_dst, 'w').close()
	md_file_name = md_file_dir_src + md_file_name
	latest_contents = open(md_file_name, "r").read()
	history_file = open(md_file_fullpath_dst, "r")
	history_contents = history_file.read()
	history_file.close()
	os.remove(md_file_fullpath_dst)
	history_file = open(md_file_fullpath_dst, "w") 
	commit = '# ' + commit_name + "\n\n" + latest_contents + "\n\n\n" + history_contents
	history_file.writelines(commit)
	md_file_src_fresh = open(md_file_name, "w")
	md_file_src_fresh.writelines(content_template)


current_date = date.today().strftime("%B %d, %Y")

if len(sys.argv) < 2:
	print ("usage: python commit.py [<commit name>]\n\t<commit name>\tA name for the history entry (e.g., a date)")
	print ("Since you did not specify a value for <commit name>, the current date (" + current_date + ") is used\n")

commit_name = " "
commit_name = current_date if  len(sys.argv) < 2 else commit_name.join(sys.argv[1:])

def filename_from_path(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

for md_file in os.listdir("content/latest/personal"):
	if md_file.endswith(".md"):
		user_name = str(md_file)
		archive_content(PERSONAL_SLIDE_HISTORY, "content/latest/personal/", md_file, commit_name, PERSONAL_SLIDE_TEMPLATE)
		print ("added history entry for user '" + user_name.replace(".md", "") + "'")


archive_content(SPECIAL_SLIDE_HISTORY, "content/latest/special/", "Additional Concerns.md", commit_name, ADDITIONAL_CONCERNS_SLIDE_TEMPLATE)
print ("added history entry for additional concerns")

archive_content(SPECIAL_SLIDE_HISTORY, "content/latest/special/", "Special Announcements.md", commit_name, SPECIAL_ANNOUNCEMENTS_SLIDE_TEMPLATE)
print ("added history entry for special announdements\n\n")

print ("slides has been resetted.")


