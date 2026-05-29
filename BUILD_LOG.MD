## Task 1 — <establish repo>
- Brief: Make a respository for the capstone project.
- Verification: Checked to see if it was saved

## Task 2 — <CLAUDE.md>
- Brief: Describe how you would go about writing a CLAUDE.md file, a file that provides guidelines on how Claude Code is expected to behave.
- What Claude proposed: Claude gave an extensive list that included tips such as being specific and including rationale/context behind everything.
- What I changed before approving: It suggested a "nested" format where general rules had one file and different files for other pages, all under the same folder, but I decided not to overcomplicate it.
- Verification: Observed Claude during the following interactions to see if it followed these guidelines.
- One thing I learned: I decided to test out Claude without the md, and it was incredibly unrestrained, trying to edit entire files. No wonder this was the first task instructed.

## Task 3 — <establish app.py>
- Brief: Create an app.py file, as a place to begin adding in the coding for the site. This file must be empty initially.
- What Claude proposed: (I did not remember to consult planning mode, so Claude simply added it with my approval.)
- Verification: n/a
- One thing I learned: Pay more attention to the process and do planning mode.

## Task 4 — <establish main.html and create a basic website>
- Brief: Create a main.html title. This should be a webpage, which presents with a title and body text. Title should say "AstroTest" and body should say "Welcome to the astronomy quiz! Would you like to test your knowledge?" Do not add code until told.
- What Claude proposed: Claude set up the website fairly straightforward.
- What I changed before approving: Claude for whatever reason did not register the text component, so I had to specify once more.
- Verification: Launched via local host and checked the page; it did not work.

## Task 5 — <add basic flask routing to app.py>
- Brief: Install and import flask into the python file. Use it to implement the webpage. Do not add code until told.
- What Claude proposed: Claude broke and asked for specific settings within my computer to install flask. After doing so, it was able to run.
- Verification: Asked Claude to manually reload the page, then checked it again. This time it worked.

## Task 6 — <add start>
- Brief: Add a button that starts the quiz and redirects to a "question" page.
- What Claude proposed: Claude agreed creating a new page for questions, and added "answers" as an option as well.
- What I changed before approving: I told it to save answers for the next step.
- Verification: Clicked the button on the webpage, self explanatory.

## Task 7 — <add answer options>
- Brief: Create a dropdown menu, where the options are taken from a dict. These will be the answers to the questions, and each question will be assigned a unique set of answers based on what is applicable.
- What Claude proposed: Claude proposed a specific routing that would take the number and assign questions and answers to it when appropriate.  
- What I changed before approving: Changed some of the proposed questions and answers to make them a bit harder, and added new ones. Additonally, Claude wanted to add more answer functionality but I shut that down to focus on for the next steps.
- Verification: Attempted to answer the questions; however, the answers were not visible yet.

## Task 8 — <correct/incorrect>
- Brief: Allow for the answers to be recognized as correct or incorrect.
- What Claude proposed: Claude created a large number of pages and created links between all of them to create the experience of a quiz format.
- What I changed before approving: Claude proposed two options: the dropdown menu or a different option involving buttons. I actually switched my mind and chose buttons for simplicity's sake.
- Verification: Answered both correctly and incorrectly to test both options out.
 
## Task 9 — <answer chain>
- Brief: After answering, a button that links to the next question sequentially should be there.
- What Claude proposed: Claude set up the system perfectly.
- What I changed : Initially, it seemed to believe that only correct answers would link to the next page, but I caught this and corrected it.
- Verification: Answered every question and got to the end.

## Task 10 - <results>
- Brief: Add a "results" page after question 5. Using a counter for the number of correct answers the user input, display the final score via percentage. Additionally, add a "replay" button that takes the user back to the first page.
- What Claude proposed: Proposed a simple message to display the score and to reset the quiz.
- Verification: Tested answering every question correctly and then resetting, then tested getting some wrong and resetting.
