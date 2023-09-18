
# Project Setup Guide

Follow these steps to set up your project environment and run the code.

## Step 1: Create a Project Folder

1. Create a new folder on your desktop or in another location to organize your project files.

## Step 2: Open the Folder in VSCode

1. Open Visual Studio Code (VSCode).
2. Use the "File" menu in VSCode to open the folder you created in Step 1.

## Step 3: Open the Terminal

1. In VSCode, open the integrated terminal by pressing `Ctrl + J`.

## Step 4 (Windows): Install and Create a Virtual Environment

1. If you haven't already installed `virtualenv` globally, run this command to install it:

pip install virtualenv

2. Create a virtual environment by running the following command in the terminal:

virtualenv env

## Step 4 (macOS): Install and Create a Virtual Environment

1. If you haven't already installed `virtualenv` globally, run this command to install it:

pip install virtualenv

2. Create a virtual environment by running the following command in the terminal:

virtualenv env


## Step 5: Activate the Virtual Environment

1. Activate the virtual environment on Windows by running:

.\env\Scripts\activate

2. Activate the virtual environment on macOS by running:

source env/bin/activate

## Step 6: Install Dependencies

1. While the virtual environment is active, install the project dependencies from `requirements.txt`:

pip install -r requirements.txt

## Step 7: Prepare Excel File

1. Move a copy of your Excel file to the project's working directory.
2. Rename the Excel file to "file" (without quotes) if it has a different name.

## Step 8: Run the Main Script

1. Run the main script by executing:

python main.py

Now your project environment is set up, and you can start using the code. Make sure to activate the virtual environment whenever you work on the project, and deactivate it when you're finished by running `deactivate` in the terminal.
