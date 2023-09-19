<h1 align="center">DOI Finder</h1>

<p align="center">
  
<img src="https://img.shields.io/badge/made%20by-berkeokur-blue.svg?color=%23009FFD" >

<img src="https://img.shields.io/badge/version-1.0 Beta 2-brightgreen?color=%7fff00">

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >
</p>

# Project Setup Guide

Follow these steps to set up your project environment and run the code.

## Step 1: Create a Project Folder

1. Create a new folder on your desktop or in another location to organize your project files.

## Step 2: Open the Folder in VSCode

1. Open Visual Studio Code (VSCode).
2. Use the "File" menu in VSCode to open the folder you created in Step 1.

## Step 3: Open the Terminal

1. In VSCode, open the integrated terminal by pressing `Ctrl + J`(Windows), `CMD + J`(macOS).

## Step 4 (Windows): Install and Create a Virtual Environment

1. If you haven't already installed `virtualenv` globally, run this command to install it:

```
pip install virtualenv
```

2. Create a virtual environment by running the following command in the terminal:

```
python -m venv env
```
3. Activate the virtual environment:

```
env\Scripts\activate
```

## Step 4 (macOS): Install and Create a Virtual Environment

1. If you haven't already installed `virtualenv` globally, run this command to install it:

```
pip install virtualenv
```

2. Create a virtual environment by running the following command in the terminal:

```
virtualenv env
```

3. Activate the virtual environment:

```
source env/bin/activate
```

After creating and activating the virtual environment
install the required dependencies:

```
pip install -r requirements.txt
```

Move a copy of excel file to working directory

Run main.py and follow the instructions