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

import os
import shutil
from datetime import date

# ----------------------------------------------------------------------------------------------------------------------
# constants for mapping markdown section names
# ----------------------------------------------------------------------------------------------------------------------

PERSONAL_SLIDE_SEC_RUNNING_PROJECTS = "Running Projects"
PERSONAL_SLIDE_SEC_CURRENT_TASKS = "Current Tasks"
PERSONAL_SLIDE_SEC_QUESTIONS_AND_REQUESTS = "Questions and Requests"
PERSONAL_SLIDE_SEC_WANT_TO_SHARE = "Want to Share"
PERSONAL_SLIDE_SEC_NEXT_STEPS = "Next Steps"

# ----------------------------------------------------------------------------------------------------------------------
# customization
# ----------------------------------------------------------------------------------------------------------------------

color_hightlight = open('customize/color-highlight', 'r').read()

# ----------------------------------------------------------------------------------------------------------------------
# html snippets from some templates
# ----------------------------------------------------------------------------------------------------------------------

index_contents  = open('src/index.html', 'r').read()
personal_slide_block = open('src/personal-slide.html', 'r').read()
additional_concerns_block = open('src/additional-concerns.html', 'r').read()
special_announcements_block = open('src/special-announcements.html', 'r').read()
agenda_block = open('src/agenda-for-today.html', 'r').read()
css_contents = open('src/css/styles.css', 'r').read()

# ----------------------------------------------------------------------------------------------------------------------
# templates for standard empty content; used to check if a change is made for the latest presentation  
# ----------------------------------------------------------------------------------------------------------------------

PERSONAL_SLIDE_CONTENT_EMPTY = open("src/templates/personal-slides.md", 'r').read()
ADDITIONAL_CONCERNS_CONTENT_EMPTY = open("src/templates/additional-concerns.md", 'r').read()
SPECIAL_ANNOUNCEMENTS_CONTENT_EMPTY = open("src/templates/special-announcements.md", 'r').read()

# ----------------------------------------------------------------------------------------------------------------------
# flags to indiciate what to show in the outline / table of content slide 
# ----------------------------------------------------------------------------------------------------------------------

has_annoncement_slide = False
has_personal_slides = False
has_additional_concerns_slide = False

# ----------------------------------------------------------------------------------------------------------------------
# the html/css files that are actually generated
# ----------------------------------------------------------------------------------------------------------------------

index_out = open("html/index.html", "w")
css_out = open("html/css/styles.css", "w")

slide_num = 2 # at least the front page, and end slide

# ----------------------------------------------------------------------------------------------------------------------
# personal slides
# ----------------------------------------------------------------------------------------------------------------------

def extract_personal_info(personal_slide_md):
	ret = dict()
	current_section = "unknown"
	current_item = "null"

	for line in personal_slide_md.replace("\r", "").split('\n'):
		line = line.strip()
		if (line.startswith("##")):
			current_section = line.replace("##", "", 1).strip()
			continue
		else:
			if (line.startswith("-")):
				current_item = line.replace("-", "").strip()
			else:
				current_item += " " + line.strip()
				continue

		if current_section not in ret:
			ret[current_section] = list()

		ret[current_section].append(current_item)

	return ret

def replace_with_contents(string, comment, content_map, key):
	if key in content_map:
		for item in content_map[key]:
			string = string.replace(comment,
				"<li>" + item + "</li>" + comment)
	return 	string

def insert_personal_content(slide_block, content_map):
	slide_block = replace_with_contents(slide_block, "<!-- bob-running-projects-list -->", content_map, PERSONAL_SLIDE_SEC_RUNNING_PROJECTS)
	slide_block = replace_with_contents(slide_block, "<!-- bob-current-tasks-list -->", content_map, PERSONAL_SLIDE_SEC_CURRENT_TASKS)
	slide_block = replace_with_contents(slide_block, "<!-- bob-questions-and-requests-list -->", content_map, PERSONAL_SLIDE_SEC_QUESTIONS_AND_REQUESTS)
	slide_block = replace_with_contents(slide_block, "<!-- bob-want-to-share-list -->", content_map, PERSONAL_SLIDE_SEC_WANT_TO_SHARE)
	slide_block = replace_with_contents(slide_block, "<!-- bob-next-steps-list -->", content_map, PERSONAL_SLIDE_SEC_NEXT_STEPS)
	return 	slide_block

for file in os.listdir("content/latest/personal"):
	if file.endswith(".md"):
		personal_slide_contents = open("content/latest/personal/" + file, 'r').read()
		if personal_slide_contents != PERSONAL_SLIDE_CONTENT_EMPTY:
			content_map = extract_personal_info(personal_slide_contents)
			this_personal_slide_block = insert_personal_content(personal_slide_block[:], content_map)
			index_contents = index_contents.replace("<!-- bob-personal-slide-next -->", 
													this_personal_slide_block)
			index_contents = index_contents.replace("<!-- bob-presenters-name -->", file.replace(".md", ""))
			slide_num += 1
			has_personal_slides = True

# ----------------------------------------------------------------------------------------------------------------------
# special slides
# ----------------------------------------------------------------------------------------------------------------------

def extract_items(contents):
	ret = list();
	current_item = "null"
	for line in contents.replace("\r", "").split('\n'):
		line = line.strip()
		if (line.startswith("-")):
			ret.append(current_item)
			current_item = line.replace("-", "").strip()
		else:
			current_item += " " + line.strip()
			continue
	ret.append(current_item)
	del ret[0]
	return ret

# additional concerns	

def insert_generic(block, content_list, placeholder):
	for item in content_list:
		block = block.replace(placeholder,
			"<li>" + item + "</li>" + placeholder)
	return block

additional_concerns_contents = open("content/latest/special/Additional Concerns.md", 'r').read()
if additional_concerns_contents != ADDITIONAL_CONCERNS_CONTENT_EMPTY:
	slide_num += 1
	has_additional_concerns_slide = True
	content_list = extract_items(additional_concerns_contents)
	this_additional_concerns_block = insert_generic(additional_concerns_block, content_list, "<!-- bob-additional-concerns-list -->")
	index_contents = index_contents.replace("<!-- bob-additional-concerns-slide -->", this_additional_concerns_block)

# announcements

special_announcements_contents = open("content/latest/special/Special Announcements.md", 'r').read()
if special_announcements_contents != SPECIAL_ANNOUNCEMENTS_CONTENT_EMPTY:
	slide_num += 1
	has_annoncement_slide = True
	content_list = extract_items(special_announcements_contents)
	this_special_announcements_block = insert_generic(special_announcements_block, content_list, "<!-- bob-special-announcements-list -->")
	index_contents = index_contents.replace("<!-- bob-special-announcements-slides -->", this_special_announcements_block)

# ----------------------------------------------------------------------------------------------------------------------
# update outline
# ----------------------------------------------------------------------------------------------------------------------

if has_annoncement_slide or has_personal_slides or has_additional_concerns_slide:
	index_contents = index_contents.replace("<!-- bob-agenda-slide -->" ,agenda_block)
	slide_num += 1


index_contents = index_contents if has_annoncement_slide == False else index_contents.replace("<!-- bob-outline-has-special-announcements-slide -->", "<li>Special Announcements</li>");
index_contents = index_contents if has_personal_slides == False else index_contents.replace("<!-- bob-outline-has-personal-slides -->", "<li>Personal Presentations</li>");
index_contents = index_contents if has_additional_concerns_slide == False else index_contents.replace("<!-- bob-outline-has-additional-concerns-slide -->", "<li>Additional Concerns</li>");

# ----------------------------------------------------------------------------------------------------------------------
# slider
# ----------------------------------------------------------------------------------------------------------------------

additional_slider = ""
for i in range(3, slide_num + 1):
	additional_slider += '<input type="radio" name="slider" id="slide0' + str(i) +'">\n'

index_contents = index_contents.replace("<!-- bob-additional-slider -->", additional_slider)

additional_slider_control = ""
for i in range(3, slide_num + 1):
	additional_slider_control += '<li><label for="slide0' + str(i) + '"> </label></li>\n'

index_contents = index_contents.replace("<!-- bob-additional-slider-control -->", additional_slider_control)

# ----------------------------------------------------------------------------------------------------------------------
# css slider
# ----------------------------------------------------------------------------------------------------------------------

css_contents = css_contents.replace("/* bob-css-slider-width */", str(slide_num) + "00%");

additional_slide_controls = ""
for i in range(3, slide_num + 1):
	additional_slide_controls += "#slide0" + str(i) + ":checked ~ .bob-slider-elements { left: -" + str(i - 1) + "00%; }" "\n"

css_contents = css_contents.replace("/* bob-css-additional-slide-controls */", additional_slide_controls);	

additional_slide_controls_mods = ",\n" if slide_num > 3 else ""
for i in range(3, slide_num + 1):
	additional_slide_controls_mods += '#slide0' + str(i) + ':checked ~ .bob-slider-controls label[for="slide0' + str(i) + '"]' + (", " if i < slide_num else '' ) + "\n"

css_contents = css_contents.replace("/* bob-css-additional-slide-controls-mods */", additional_slide_controls_mods);	
css_contents = css_contents.replace("/* bob-css-slider-elem-width */", str(100.0/(slide_num)) + "%")
css_contents = css_contents.replace("/* bob-customize-color-highlight */", color_hightlight)


index_contents = index_contents.replace("<!-- bob-date-today -->", date.today().strftime("%B %d, %Y"));

# ----------------------------------------------------------------------------------------------------------------------
# write everything out
# ----------------------------------------------------------------------------------------------------------------------

index_out.writelines(index_contents)
css_out.writelines(css_contents)

# ----------------------------------------------------------------------------------------------------------------------
# copy remaining sources
# ----------------------------------------------------------------------------------------------------------------------

shutil.rmtree("html/fonts", True)
shutil.rmtree("html/img", True)
shutil.copytree("src/fonts", "html/fonts")
shutil.copytree("customize/img", "html/img")

# ----------------------------------------------------------------------------------------------------------------------
# and we're done
# ----------------------------------------------------------------------------------------------------------------------

print ("Slides were built. To start the presentation, open this file in your browser:\n\thtml/index.html");



