# The Slideshow Bob Presentation Generator 

Slideshow Bob is a lightweight, and modern team status report presentation generator suitable for medium to large teams, which need to run status updates on a regular basis and which look for a solution that has an easy workflow, that is scriptable and that need a minimum on technical infrastructure to run. 

Not yet convinced? Have a look at the following features, the workflow description and scripting commands. 

By the way, Slideshow Bob is customizable, too.

## Features

In a nutshell, these are the feature of Slideshow Bob:

- <b>Focussed Slides</b>: presenters are activated to express their current state cristall clear by 
  explictly requiring them to speak about running projects, current tasks, 
  questions and requests, next steps, and what they want to share
- <b>Small Managment Overhead</b>: slides of single presenters are only included if new information is present,
  same for a special announcements slide and an additional concerns slide. Presenters fill their particular markdown file, which is always stored at the same location, always automatically resetted after the last presentation, and which has minimal structure overhead
- <b>Clear and Modern</b>: simple design language to focus on content with HTML5/CSS slides supporting directly jumps to specific slides, and navigation though the presentation by both arrow keys and the navigation bar. The responsive design supports tiny beamer resolutions, too.
- <b>History Management</b>: commit based history managment that adds individual presenters content to the 
  presents report file, and archives additional concerns and announcements. Report files are markdown formatted and are ordered by commit date.
- <b>Scriptable</b>: a few python scripts to commit the latest presentation to history, build the presentation or add new presenters. 



## Workflow by Example

Imaging a medium-sized team that works in a company, that has a strong branding for a particular fruit. On a regular basis, all team mates assemble and give an overview on their current state. A dedicated team member, Jane Doe, is respondible to manage the status reports process. By luck, she stumbled upon Slideshow Bob.

Another team member, John Doe, gives his regular report and must make a team-wide special announcement, and who wants to express some additional concerns. Also there is 
a third team member, Bob.

Let's follow both during their adventure with Slideshow Bob. Imagine Slideshow Bob is stored on some network drive (or stored in a repository, or ...)

### Personal Slides

A John Doe gives status information in his own <i>personal slide description file</i>, which is a markdown file with his name (e.g., `John Doe.md`) and which is always located in `content/latest/personal`. 

This file has the following structure:

```markdown
## Running Projects

- ...

## Current Tasks

- ...

## Questions and Requests

- ...


## Want to Share

- ...


## Next Steps

- ...

```

Let's say John works on two projects, buying more bananas and writing a book about it. To the point of the next meeting, we just had a phone call with the bananas dealer and always ordered some bananas. Since he was very busy with that, we couldn't manage to write much about it in his book. During the team meeting, John has questions on the color of bananas and tries to find a college who will help him carriering all soon arriving bananas. Since the dealer told John an awesome joke about apes, John wants to share this with his colleges. Finally, John's next steps are making some space in his office for the bunch of bananas that will arrive very soon. 

During the days, he fills his personal slide description file with the following contents.

```markdown
## Running Projects

- Dominate the Banana Market
- Book about Bananas

## Current Tasks

- Bought all bananas for (1)
- Bananas are on the way
- No progress in writing about it

## Questions and Requests

- Who is strong? A lot Bananas will arrive!


## Want to Share

- Awesome joke about apes by dealer


## Next Steps

- Making space for (1) before (ii) is done

```

### Special Announcements and Additional Concerns

Before the presentation day, John remembers that he not yet talked about his new strategy. Therefore, we will add some information to the special announcement slide. 
For this, he edits the <i>announcements description file</i> which is a markdown file by the name `Special Announcements.md`, which is always located in `content/latest/special`. 

This file has the following structure:

```markdown
- ...
```

John knows that his special announcement will be added to the presentation, once he give some information in this file. And so he will do: John give his announcement for the team by editing the file `Special Announcements.md` to

```markdown
- Our team will conquer the <b>banana</b> market 
```

Image that a bit of time passes and that the team presentation takes place very soon. Out of nowhere, John realizes that he has had absolute no budget, and just took all the team's money to pay for his bananas. He decided to  express an additional concern. Similar to his special announcement, he edits the file `Additional Concerns.md` located in `content/latest/special`. 

Briefly before the team meeting, all other team members prepare their personal slides, too.

### As Presentation Owner

The day of the meeting has arrvied. Jane, who is responsbile for the meeting and acts as an moderator, prepares the slides a few moments before the meeting. For this, she just runs the following Python script located in the root directory of `Slideshow Bob`:

```
$ python start.py
```

## Commands

## Customization

## License

Slideshow Bob is licensed under MIT License, which means you must keep the copyright notice of Slideshow Bob intact when you use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Slideshow Bob source code. This restriction does not affect presentations created with Slideshow Bob.