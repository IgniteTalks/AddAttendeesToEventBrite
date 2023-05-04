# AddAttendees (Python Script)
AddAttendees.py aims to simplify and automate the process of adding attendees to an event in Eventbrite. This user-friendly tool utilizes Selenium WebDriver to automate the process so you do not have to manually add users one-by-one.
## Background
Eventbrite is a great tool for creating and managing events. It allows you to define an event's basic info, details, registration page, and much more. Additionally, you are able to sell tickets (either paid or free) to check people in during the event using their mobile device.

One flaw with Eventbrite is that there is no easy import function to manually add multiple attendees at once. Thus, if you have a long list of attendees to add, it's time-consuming and error-prone.

This script automates that process, so you can easily import multiple attendees to your guest list.

# Getting Started
## Setting Up Your Event 
<i>These steps must be completed prior to running the script.</i>
1. Log into your EventBrite account and navigate to the event that you wish to add attendees to. Note the event's 'eid' value, which will be shown in the page's URL. E.g. https://www.eventbrite.com/exampleEvent?eid=123456.
2. Hit the 'Order Options' drop-down menu (found in the lower-left of the event's home page), then select the 'Order Form' option. You will be redirected to a page that looks like [this](https://imgur.com/gallery/4QG6vaG).
3. Select 'Create new form from scratch' and on the next page do the following:
    * In the 'Collect information from' section, make sure the 'Each attendee' box is selected. 
    * Under 'Collect attendee information on the following tickets', make sure the 'General Admission' is NOT selected.
4. Hit the 'Manage Attendees' drop-down menu (found in the lower-left of the Home page), then select the 'Add Attendees' option.
5. On the new page, use your browser's Developer Tools to note the ticket type ID of the event. Right-click the 'Quantity' box and click 'Inspect'. See the following [finding the ID of the quantity field](https://i.imgur.com/isWfSJe.png) example.
6. Open [AddAttendees.py](https://github.com/tsanevp/AddAttendeesToEventBrite/blob/ec2860f62701801223a1ecf22ebe0a312f8dd868/AddAttendees.py) and replace all the placeholder variables you noted in steps 1 and 5.

## Building and Running The Script
<i>Skip any of the following steps if they do not apply</i>
1. Download and setup the latest version of [VS Code & Python](https://code.visualstudio.com/docs/python/python-tutorial) using this guide.
2. Download the latest version of [Selenium](https://selenium-python.readthedocs.io/installation.html).
3. Install [ChromeDriver](https://chromedriver.chromium.org/downloads).
4. Clone this repository to your local machine.
5. Create a text file with all the users you wish to add to your event. See the [example file](https://github.com/tsanevp/AddAttendeesToEventBrite/blob/master/attendees_list_example.txt).
6. Open [AddAttendees.py](https://github.com/tsanevp/AddAttendeesToEventBrite/blob/ec2860f62701801223a1ecf22ebe0a312f8dd868/AddAttendees.py) and replace all the placeholder variables:
    * Enter your EventBrite login and password on lines 22 & 23.
    * Add your attendees to a comma-limited text file in the format `firstname,surname,email_address` (see example text file).
    * Update the `attendeeList` variable on line 26 to point to the text file.
    * Update the `eventID` and `ticketID` variables on lines 30 & 32 with the values you determined in [Setting Up Your Event](#setting-up-your-event).
7. Run the script by selecting the Run button in the top right corner.

### What Happens When Script Is Ran
1. A new Chrome browser is opened and redirected to your Eventbrite account login.
2. You are logged into your account and directly taken to your event home page.
3. Each attendee in the text file you provide is added one-by-one to your event.
4. After 50 or so additions, Eventbrite times out and the script needs to be restarted, starting at the last member that was added.

# Licenses
## AddAttendees.py File:
```
Title: AddAttendees.py
Author: slead
Date: 2015
Availability: https://github.com/IgniteTalks/AddAttendeesToEventBrite/blob/master/AddAttendees.py
License: https://github.com/IgniteTalks/AddAttendeesToEventBrite/blob/master/license
The codebase above is based on the following repository: https://github.com/IgniteTalks/AddAttendeesToEventBrite
```