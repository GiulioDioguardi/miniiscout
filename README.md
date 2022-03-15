# Mini iScout for Scouting Frama
The mini iScout website is created by Giulio Dioguardi (or Jacala by his jungle name) that mimics the iScoutGame.com website so children between ages 9 and 11 can also enjoy iScout on their own level.

While iScoutGame both provides questions and doable exercises, this site only does the questions.
Children (and grown-ups alike) can use the site independently by answering questions that always have an answer on the map of the world. The site will keep the score by itself through cookies (which don't have to be accepted, because they're first party cookies)

## A bit about the structure
* Questions are in one big JSON file that lists all questions by title, body and answer
* Google Maps API is used to render the map and checking the answers
* The md5sum of the title is used as a unique key to keep track of answered questions
* The website has been written using python and Flask and rendered with Jinja
