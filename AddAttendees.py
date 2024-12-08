import sys
import time
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except Exception as exception:
    print(exception)
    msg = "Please install Selenium"
    print(msg)
    sys.exit(msg)

# Add Login Credentials
login = "<Your Eventbrite Username>"
pwd = "<Your Eventbrite Password>"

# Comma-delimited file containing the firstname, surname and email address of your attendees (see ReadMe for example)
attendeeList = "path_to_the_attendee_list.txt"

# Your Current Event's Information
eventID = "123456" # Open your event then see the URL to obtain the ID, eg https://www.eventbrite.com/myevent?eid=123456
ticketID = "quant_632892259" # Use the Dev Tools inspector to determine the ID of the ticket type you wish to add (https://i.imgur.com/isWfSJe.png)

# Opens a new Chrome browser
try:
    browser = webdriver.Chrome()
except Exception as exception:
    print(exception)
    msg = "Please install ChromeDriver"
    print(msg)
    sys.exit(msg)

# Opens Eventbrite "Add Attendees" page, prompts user login first
browser.get("https://www.eventbrite.com/attendees-add?eid={0}".format(eventID))
username = browser.find_element(By.ID, "email").send_keys(login)
password = browser.find_element(By.ID, "password").send_keys(pwd)
time.sleep(2)

# Clicks "Login" button
loginButton = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div/form/div[4]/div/button')
loginButton.click()
time.sleep(10)

# Iterates through and registers each attendee in the attendee list
with open(attendeeList) as inFile:
    lines = inFile.readlines()
    for line in lines:
        # Splits the current customers information and stores it in an array
        tokens = line.split(",")
        firstname = tokens[0]
        surname = tokens[1]
        email = tokens[2]
        print("Adding {0} {1} ({2})".format(firstname, surname, email))

        # Add each person to the event from the attendee list
        try:
            # Open "Add Attendees" page for current event
            browser.get("https://www.eventbrite.com/attendees-add?eid={0}".format(eventID))
            time.sleep(10)

            # Populates ticket purchase amount for current customer
            ticket_quantity = browser.find_element(By.ID, ticketID)
            ticket_quantity.send_keys("1")
            time.sleep(2)

            # Clicks "Continue" button
            continue_btn = browser.find_element(By.XPATH, '//*[@id="continue-attendee"]').click()
            time.sleep(10)
            browser.switch_to.frame(0)

            # Populates current attendee's first/last name & email
            buyer_first_name = browser.find_element(By.ID, "buyer.N-first_name").send_keys(firstname)
            buyer_last_name = browser.find_element(By.ID, "buyer.N-last_name").send_keys(surname)
            buyer_email = browser.find_element(By.ID, "buyer.N-email").send_keys(email)
            time.sleep(5)

            # Clicks "Submit" button
            submit_btn = browser.find_element(By.XPATH, '//*[@id="edsModalContentChildren"]/div/div[2]/div/div/div/button')
            submit_btn.click()
            time.sleep(10)
        except Exception as exception:
            print(exception)
            print("There was a problem adding {0} {1}".format(
                firstname, surname))

browser.close()
