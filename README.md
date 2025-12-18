# Web Automation Script

## Overview
This script uses Selenium WebDriver to navigate the interface of an appointment booking website. It monitors the website for the availability of appointments at certain dates and/or times and proceeds to book them when available. The script allows the user to select their desired dates and/or times and edit the refresh rate. 

This project served as my first exposure to programming; it is not intended for commercial purposes.

## Project Structure
```
booking-bot
├── README.md  
└── bcd.py
```

## Setup

#### Clone the Repository
```
git clone https://github.com/kevinkhoow/booking-bot.git
cd booking-bot
```

#### Edit Lines 20-21 in `bcd.py` with your Login Details
```
kname = 'your_username'
kpass = 'your_password'
```

#### Install Dependencies
```
pip install selenium
```

#### Execute Program
```
python3 bcd.py
```
