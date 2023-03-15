# Web-Scraping-Demo

# Overview

Demo.py is a demonstration of web scraping using Selenium 4 and Chrome Webdriver. The next half of the file we are connecting to DynamoDB and altering the database. The data in this example comes from [Apex Legends Status](https://apexlegendsstatus.com/live-ranked-leaderboards/Battle_Royale/PC).

[Software Demo Video](https://youtu.be/p0IyfQXwI8Q)

# Data Analysis Results

The most trouble I ran into while working on this project was the webdriver. I found that placing the executable in the root of the project worked just fine. In Selenium 3 or less, you need to still specify the path to the webdriver executable upon creating a new selenium webdriver object.

# Development Environment

I am using the most recent chrome webdriver as well as selenium 4. This can be run in almost any IDE, but it is recommended that you use a python virtual environment such as anaconda.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Chrome Web Drivers](https://chromedriver.chromium.org/downloads)
- [Selenium Documentation](https://www.selenium.dev/documentation/overview/)
- [Apex Legends Leaderboard](https://apexlegendsstatus.com/live-ranked-leaderboards/Battle_Royale/PC)

# Future Work

Future work to be done here:

- The delete process in this code will only delete as many rows as there are rows to be added.
- Change explicit 15 second wait time to wait until the element has been rendered in the DOM.
