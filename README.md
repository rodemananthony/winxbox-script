# winxbox-script
Automate submissions for Taco Bell's Xbox Series X giveaway.

[The rules](/OfficialRules.pdf) have been included for reference. They list the 3 reusable codes that are included already.
This won't really do anything now that the promotion is over, but here's proof of the work I did.

Huge credit to exporting python code from the Selenium IDE.

## How it works
You can run main.py (which does the actual submissions) and verify.py (which makes sure all entries have been completed for the day) separately, but run.bat runs main.py then verify.py. According to the rules, only one Xbox Series X was awarded in every 15 minute interval, so the script runs over a period, with a simple sleep call between submissions. The program will do one code at a time per email. If any of an email's 3 entries have been made for the day before the program runs, the program will stop working when trying to submit more codes than allowed. 

Since I've set the webdriver to run headless, there are three ways to monitor or view results:
1. You can look at the console window while it is running.
2. A file will be created called `log.txt` has the same text that the program prints to the console. 
3. A subdirectory called `proof` will be created that stores snapshots of the browser window after submissions. Unfortunately, I only saw 'Sorry...'

verify.py just checks with the website to make sure that all 3 of the daily submissions for an email have been made. Like main.py, it writes to console and log.txt, and saves snapshots to ./proof/

## Setup
I used a venv to contain this little project.

1. Make sure to get Selenium from:
`pip install -r ./requirements.txt`

2. Update the .bat file
If you're on Linux, I'm guessing you can whip up a little script to replicate this.
The `cd` command needs to be updated with the path of the files from this repo.
If you are not using a venv, also change the other lines to invoke python however you choose.

3. Update data.json
All it needs is emails in the file. Pretty standard (I think). Just put in your list of comma-separated, quote-enclosed email addresses to be used. Emails need to be registered at [the promotion website](winxbox.com) before they can be used here. The script is pretty fragile, so just trust me.

4. Set up your webdriver
As it is, the project expects an .exe webdriver for Chrome to be in the project directory. Get your own version [here](https://chromedriver.chromium.org/downloads) and make sure that it's named `chromedriver.exe` in the project folder. If it's on your path or you're doing something different, you'll have to change the `executable_path` argument in [test_test.py](/test_test.py) in TestTest.setup_method. 

## Suggestions
There are a number of things that would make this project better. If you're reading this for some reason, here they are:
- Scheduling! I tried to get Task Scheduler to run this automatically, but I couldn't quite get it.
- Submission result identification! Might be neat if you could check with code if an entry was a winner, but I'm not positive what the winner page looks like.
