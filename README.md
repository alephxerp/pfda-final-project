# POINT AND CLICK PROTOTYPE

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/alephxerp/pfda-final-project>

## Description
This is a very basic prototype for a point-and-click game. It allows the user to click around on different elements to interact with the world. Once clicked, elements will have some dialogue shown to the player in a text box. A menu can also be opened up by pressing ESC, which pauses the game.

This program is split into a few files.
- The "project.py" file contains the bulk of the project, creating the elements in the game world and running the game loop.
- The "mouse.py" file is a small file that makes handling the pygame mouse data a little easier.
- The "element.py" file creates the Element and ElementGroup classes, children of the pygame classes Sprite and Group, respectively. Elements have functions for being hovered and clicked, which are overwritten in the child classes Button, Character, and Dialogue. ElementGroups hold Elements within them, rendering and processing their held Elements as given. These classes are what most of the program is built off of.

The primarily design consideration at first was scalability, but much of the later code ended up being temporary workarounds. Some parts of the code such as the rendergroup, processgroup, and viewport still allow for lots of flexibility in design.

There are many areas of improvement, most notably the messy code I ended up writing near the end of the project. Many functions and blocks of code could be simplified or condensed. The class system I set up could also be changed to make elements more versatile. Additionally, many more features could be added onto this program, for example: dialogue choices, settings, moving between screens, etc.

