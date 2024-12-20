<img align="center" src="https://raw.githubusercontent.com/TindraIS/comp-infrastructure/refs/heads/main/img/cloud.png" alt="Header image with cloud infrastructure">

## Table of Contents

* [Description](#10-description)
* [Contents](#20-contents)
* [Get Started](#30-get-started)
  * [Dependencies & Tools](#dependencies--tools)
  * [Setup Guide](#setup-guide)
* [Get Help](#40-get-help)
* [Author](#50-author)

## Structure

```
comp-infrastructure/
├── img/                     # Folder containing the imagery used across this repository
│
├── data/
│   ├── timestamps/          # Stores timestamp-related files
│   └── weather/             # Stores downloaded weather data in JSON format
│
├── .github/
│   └── workflows/           # GitHub Actions workflow file
│
├── .gitkeep
├── .gitignore               # A file that specifies which intentionally untracked files Git should ignore
├── weather.sh               # Bash script to automate weather data download
├── weather.log              # Logs workflow execution details and errors
├── weather.ipynb            # Jupyter Notebook with execution notes and data analysis
├── send_error_email.py      # Python script that triggers an email with the error message from weather.sh
├── requirements.txt         # Python dependencies for email notifications and Jupyter Notebook
└── README.md                # Project documentation (this file)
```


## Description

This project automates the process of retrieving, storing, and analysing weather data for the Athenry weather station. It combines Bash scripting, GitHub Actions, and Python-based data analysis to streamline daily weather data collection and reporting. 

The repository is organised into multiple tasks and a final project, with each task progressively building upon key concepts. These tasks are summarised in the accompanying Jupyter Notebook (`weather.ipynb`).

Key features include:

- **Automated data retrieval**:
A Bash script (`weather.sh`) fetches present day weather data from the Met Éireann API and saves it with timestamped filenames.

- **Scheduled automation & data storage**:
Using GitHub Actions, the script runs daily at 10AM UTC, automatically committing and pushing new weather data back to the repository, which is stored in JSON format under data/weather/.

- **Workflow monitoring**:
The workflow logs execution details, including successes and errors, to `weather.log` for easy monitoring. Additionally, any critical errors trigger a notification via email using the `send_error_email.py` script, ensuring issues are promptly reported to the author. 

- **Data analysis and other notes**:
A Jupyter Notebook (`weather.ipynb`) is included to summarise, analyse, and explore the collected weather data, providing insights into key metrics like temperature, wind speed, and rainfall. It also documents implementation steps for tasks 1-9.


## Get Started

### Dependencies & Tools
- Bash: For running the automation script
- Python 3.x
- Python modules used for data analysis in the Jupyter Notebook and email notifications script:
  - Pandas
  - Matplotlib
  - Seaborn
  - NumPy
  - Windrose
- Gmail

### Setup guide
**1. Clone the repository**

To get started, clone the repository to your local machine:
```bash
git clone https://github.com/tindrais/comp-infrastructure.git
cd comp-infrastructure
``` 

**2. Run the Bash script**

Ensure the `weather.sh` script is executable and run it:

```bash
chmod +x weather.sh
./weather.sh
```
**3. Install Python dependencies**

If you are running error notifications or the Jupyter Notebook locally, install the required Python dependencies:
```bash
pip install -r requirements.txt
```

**4. GitHub Actions configuration**

GitHub Actions workflows are preconfigured in `.github/workflows/weather-data.yml`.
For email failure notifications, [generate an app password with your Gmail account](https://support.google.com/mail/answer/185833?hl=en) and create environment variables to store SMTP credentials in your repository under _Settings > Secrets and Variables > Actions_ using the following format:
      
| Name               | Secret                   |
|--------------------|--------------------------|
| SMTP_SERVER        | smtp.gmail.com           |
| SMTP_PORT          | 587                      |
| SENDER_EMAIL       | your-email@gmail.com     |
| SENDER_PASSWORD    | your app password        |
| RECIPIENT_EMAIL    | recipient-email@gmail.com |


Alternatively, for local development, set the required environment variables manually in your terminal:
```bash
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SENDER_EMAIL=email@gmail.com
export SENDER_PASSWORD="your app password"
export RECIPIENT_EMAIL=recipient-email@gmail.com
```

## Get Help

For any issues with the code, please refer to [GitHub's issue tracker](https://github.com/tindrais/comp-infrastructure/issues) and create a new ticket.

## Author
[Irina S.](https://github.com/tindrais)