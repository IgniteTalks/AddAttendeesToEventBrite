#Add attendees to your EventBrite list

EventBrite is a great package for managing your Ignite. It allows you to sell tickets (either paid or free) and check people in using their free iPhone/Android app.

One major pain is that there's no easy Import function to add attendees. If you have a long list of attendees to add, it's time-consuming and error-prone.

This script automates the process, so you can easily import multiple attendees to your guest list.

####Before you get started

1) Log into your EventBrite account and open up the event that you wish to add people to. Note its `eid` value, which will be shown in the URL, eg https://www.eventbrite.com.au/myevent?eid=123456

2) Hit the Add Attendees option (on the lower-left of the Manage page) then use your browser's Developer Tools to note the ID of the ticket type that you wish to create.

![Finding the ID of the quantify field](http://i.imgur.com/RIYANW1.png)

3) Install the Selenium python plugin from https://selenium-python.readthedocs.org/

####Update the script

Enter your EventBrite login and password in the relevant sections.

Add your attendees to a tab-limited textfile in the format `firstname <tab> surname <tab> email_address` and update the `attendeeList` variable to point to this.

Update the `eventID` and `ticketID` sections with the values you determined in (1) and (2) above.

####Run the Python script

This should open a Firefox browser, log into your event, and add the names from the textfile to the ticket type that you've chosen.