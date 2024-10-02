
### README.md

# Automate the Boring Stuff with Python - Self-Learning Project

This project is designed for self-learners practicing Python automation tasks inspired by "Automate the Boring Stuff with Python." The project is divided into various chapters, each focusing on different automation techniques like web scraping, file handling, working with spreadsheets, and more.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction
This project contains Python scripts corresponding to various chapters from "Automate the Boring Stuff with Python." You can import these files into `main.py` and test their functions to get hands-on experience with RPA (Robotic Process Automation) tasks.

## Prerequisites
- Python 3.x
- A Google account with access to Google Sheets API for Chapter 14.

## Setup
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. For Google Sheets integration (Chapter 14), download the `credentials.json` file from the Google Cloud Console and place it in the root directory of your project.

## Configuration
1. A sample configuration file `config.example.json` is provided to store email credentials and other sensitive information.
2. Before running the scripts, create a copy of `config.example.json` and rename it to `config.json`.
3. Open `config.json` and fill in your email credentials:
   ```json
   {
       "email": {
           "sender_email": "your_email@example.com",
           "sender_password": "your_password",
           "recipient_email": "recipient_email@example.com"
       }
   }
   ```
   Make sure to keep `config.json` safe and do **not** share it publicly, as it contains sensitive information.

## Contributing
This project is for self-study purposes. Feel free to modify and experiment with the scripts to suit your learning objectives.
