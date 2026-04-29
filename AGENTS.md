# AGENTS.md
 
## How I Used AI During This Project
 
### What AI helped with
 
I used Claude (by Anthropic) throughout this project as a guide and coding assistant.
 
- **Project idea**: I love to read books, so I wanted to create something that is easy to use to track my personal book collection.
- **Writing library.py**: Claude wrote the initial version of the core code including the add, list, update, remove, and search functions. I reviewed each function and asked questions about parts I did not understand, such as how elif works and how JSON files are used to store data.
- **Writing tests**: Claude helped me write the pytest test suite. I customized the test examples to use books I am familiar with, like Divergent by Veronica Roth and A Court of Thorns and Roses by Sarah J. Maas.
- **Git issues**: Claude helped me fix several push errors caused by my local and remote repositories being out of sync. I learned to use git pull --rebase to fix these issues.
- **README**: Claude helped me structure the README and I wrote and edited the final version myself.
### Where AI steered me wrong
 
- At one point I accidentally typed content meant for Notepad directly into the Command Prompt. This was a misunderstanding on my part about the workflow, not an AI error, but it caused some confusion.
- A merge conflict occurred in README.md because I was editing the file on GitHub's website and on my local computer at the same time. Git did not know which version to keep. Claude helped me understand what a merge conflict is and how to fix it by using a force push to keep my local version.
### What I learned
 
- How to structure a real Python project with tests and CI/CD
- How git push, pull, and rebase work
- How GitHub Actions automatically runs tests on every commit
- How to use JSON as a simple local database
- The importance of committing early and often
### Takeaway
 
This project taught me a lot about what it actually takes to build and ship a real software project. I came in knowing I wanted to build something around books since reading is something I genuinely enjoy. Working through each step, from writing the code to setting up tests and CI/CD, showed me that there is a lot more to a project than just writing code that works. I also learned that using AI as a tool is a skill in itself. You have to ask the right questions, push back when something is too complicated, and make it your own.

