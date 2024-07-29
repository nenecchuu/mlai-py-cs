# Virtual Assistant using Python

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple virtual assistant built using Python. It mimics the functionality of popular virtual assistants like Apple's Siri, Google Home, and Amazon Alexa. This virtual assistant can be activated, renamed, schedule tasks, view scheduled tasks, tell jokes, and send emails.

## Features

1. **Activate the Assistant**: Activate the assistant to start listening to commands.
2. **Change Name**: Change the name of the virtual assistant.
3. **Create Schedule**: Add tasks to the assistant's schedule.
4. **View Schedule**: View the tasks scheduled.
5. **Tell Jokes**: The assistant can tell a random joke.
6. **Send Email**: Send an email using the assistant.

## Installation

To run this virtual assistant, you need to have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/virtual-assistant.git
    cd virtual-assistant
    ```

2. Install the required dependencies:
    ```sh
    pip install pipreqs
    pipreqs .
    pip install -r requirements.txt
    ```

3. Create a `.env` file from `.env.example` and add your configuration:
    ```
    SMTP_USER=your_email
    SMTP_PASSWORD=your_app_password
    ```

## Usage

1. **Activate the Assistant**: Run the main script to activate the assistant.
    ```sh
    python main.py
    ```

2. **Change Name**: Use the assistant's menu to change its name.
3. **Create Schedule**: Add tasks to the schedule through the menu.
4. **View Schedule**: View the tasks that have been scheduled.
5. **Tell Jokes**: Ask the assistant to tell a joke.
6. **Send Email**: Provide the necessary details to send an email through the assistant.