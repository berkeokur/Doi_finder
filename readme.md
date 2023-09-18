Create a new folder on desktop (or another place)

Open that folder using File from top of VSCode

Open terminal (ctrl + j)

Install virtualenv if it's not installed globally:
pip install virtualenv

Create a virtual environment:
virtualenv env

Activate environment:
source env/bin/activate.ps1

Install dependencies:
pip install -r requirements.txt

Move a copy of excel file to working directory
Rename the excel file to "file"
run main.py