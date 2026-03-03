Title: Workflow
Date: 2024-11-11
Modified: 2025-10-28

## Introduction

This post discusses my workflows. I am sharing it in case it is helpful for others to read.

## Every Day

### Administrative

* Read unread emails and unread Slack messages. Respond to everything.
* Check personal goals and their progress for the year.

### Gutcheck Projects

* Review each project's motivation, goals, "secret sauce", current status, and timeline to finish. Do they make sense?
* [Heilmeier Catechism](https://www.darpa.mil/work-with-us/heilmeier-catechism)
    * What are you trying to do? Articulate your objectives using absolutely no jargon.
    * How is it done today, and what are the limits of current practice?
    * What is new in your approach and why do you think it will be successful?
    * Who cares? If you are successful, what difference will it make?
    * What are the risks?
    * How much will it cost?
    * How long will it take?
    * What are the midterm and final "exams" to check for success?
* Writing papers
    * What problem are you solving?
    * Why is it an important problem?
    * What are the existing approaches? Why are they not sufficient?
    * What is your approach? Why is it more effective, efficient, novel, etc?
    * How do you implement it? Why is that a good and practical way?
    * How do you evaluate your approach and system? Why is the evaluation fair and realistic? How do the results support the goals and claims of your approach and system?

### [Read](http://www.evandowning.com/suggested-reads.html) academic papers and blog posts

* For papers, create a summary:
    * Problem
    * Existing approaches and their limitations
    * Approach
    * Evaluation

### Coding

* Review Pull Requests.
* Work on code for each project.
* Automate linting and tests via [Github actions](https://github.com/features/actions).

## Fridays

### Start of Day

* Administrative
* Gutcheck Projects

### Write

* Brainstorm research ideas
    * Focus on defining the problem. If you define the problem well enough, the solution will become clear.
* Work on the draft of academic paper or client report
    * This is an up-to-date version of the final draft. The weekly meetings serve as snapshots of the final draft, so you can track the evolution of the project.
    * The story for the project (motivation)
    * Outline the evaluation (how you will measure success)
    * Fill in results as you get them each day (if you were successful)
    * Working on the final draft of the paper or report helps you not leave things until the last minute
    * Save filling in the rest (introduction, related works, discussion) until the week before you submit
    * Two days before the deadline, every co-author should have read the final draft and made comments/edits

## Starting a New Project

* Create a Google Drive of Documents and Slides:
    * Related Works (Folder containing PDFs of papers referenced in `Background`)
    * Background (Doc which lists and summarizes related works and existing solutions)
    * Brainstorming (Doc containing ideas I have)
    * Meetings (Doc of meeting minutes of me presenting the idea to others)
    * Overview (Doc of Heilmeier Catechism for planning, Ongoing Summary for up-to-date status of project. See [Gutcheck Projects](#gutcheck-projects))
    * Slides (Presentation during meetings with status updates)
* Go Fast!
    * To start, search (Google Scholar)[https://scholar.google.com/] and (Scholar Labs)[https://scholar.google.com/scholar_labs/search] for existing works in top-tier conferences. Put these in your `Related Works` folder -- just download, drag, and drop.
    * Use [NotebookLM](https://notebooklm.google/). Add your `Background`, `Brainstorming`, and `Overview` Docs as well as all papers in `Related Works/` Ask it research questions, brainstorm ideas, list experiments to perform (and in what order, such that each tells you the most information about what to do next), etc.
* Go Slow!
    * Read through claims from LLMs about novel research directions and summaries of prior works. Fact check everything. Carefully craft your research direction and list of experiments to perform.
    * Create rapid software prototypes and measurements against the state-of-the-art. Ask NotebookLM to craft prompts to give to LLMs to quickly develop these prototypes -- double-check each implementation carefully.

## Writing Proposals

  1. Create an overview diagram of what the system will look like. What happens first, second, third, etc. in the pipeline. What is the input? What is the output?
  1. Write & submit an abstract describing the solution. What is the goal? What are the constraints? What is the approach? What are the expected results?
  1. Fill in the front and back matter on the proposal. Now you know how many pages you have to work with to write the technical content.
  1. Create a real-world motivating example (1-2 paragraphs) you will use throughout the proposal.
    * This is a framing device to go back and talk about how the solution will handle each challenge in the motivating example.
  1. Split the system into components (which should already be apparent by the diagram) and assign engineers to tackle each part.
  1. Make sure you include the exact metrics the BAA is asking for and say your solution will accomplish them.

## Leadership

* Break each project down into 2 or 3 parts, and assign each person one part to own.
* For each project, have an end-goal in mind and an end-date. I.e., what specifically do you want to accomplish by when?
* Everyone self-updates their progress for you to present at status updates, as well as allows you to ask and answer questions there (an internal Google Doc).
* For each status update, create slides and meeting meetings (shared with the client). Have action items they agree to (ranked by importance) for the next meeting.
* For each status update presentation, create ~6 slides to share with the client. That way, it is easy for them to track your progress over time.
    * Agenda
    * Running list of Insights and Contributions
    * 2-3 updates (visual/graph/numbers of results)
    * Insights for each update -- What did I learn? What is novel/interesting?
    * Next steps -- From what I learned last week, what will I do this week?
* If you are away on leave, assign someone to lead in your place, and notify the client who the lead contact will be until you get back. No major changes to the project should be made until you return, unless absolutely necessary.
* Overspend on the front end of a project, so you can get far enough along that you can divert your attention if needed (e.g., a proposal needs your attention or you have meetings/trainings/other responsibilities to take care of later).
* Every time there is a problem or something does not go according to plan, ask the Five Whys (from The Lean Startup book). Ask "why" 5 times, and you will usually identify the root cause of an issue. Fix the fifth (final) "why" first, then fix the other "whys" if they pop up again. Blame the problem, not the person. If someone makes a mistake, it is our fault it was easy for them to make that mistake.

## Retrospective

* After each project is finished, do a retrospective for lessons learned.
    * What went right? Why did it go right?
    * What went wrong? Why did it go wrong? What will we do to prevent this in the future?
