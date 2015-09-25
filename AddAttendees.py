import sys, time
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    msg = "Please instatall Selenium"
    print(msg)
    sys.exit(msg)

login = "<your eventbrite username>"
pwd = "<your eventbrite password>"
attendeeList = "path_to_the_attendee_list.txt" #Tab-delimited file containing the firstname, surname and email address of your attendees

eventID = "123456" #eg open your event then see the URL to obtain the ID, eg https://www.eventbrite.com.au/myevent?eid=123456
ticketID = "quant_98765" #Use the Dev Tools inspector to determine the ID of the ticket type you wish to add (http://i.imgur.com/RIYANW1.png)

#Open a browser at the event homepage
fp = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("https://www.eventbrite.com.au/attendees-add?eid=" + str(eventID))
username = browser.find_element_by_id("login-email")
password = browser.find_element_by_id("login-password")
username.send_keys(login)
password.send_keys(pwd)
loginButton = browser.find_element_by_xpath(".//*[@id='authentication-container']/div/div/form/div[2]/div/div[4]/input")
loginButton.click()
time.sleep(10)

#Iterate through each name in the input file
with open(attendeeList) as inFile:
    lines = inFile.readlines()
    for line in lines:
        tokens = line.split("\t")
        firstname = tokens[0]
        surname = tokens[1]
        email = tokens[2]
        print("Adding " + firstname + " " + surname + " (" + email + ")")
        
        #Add each person to the guest list
        try:
            browser.get("https://www.eventbrite.com.au/attendees-add?eid=" + str(eventID))
            time.sleep(10)
            quantity = browser.find_element_by_id(ticketID)
            quantity.send_keys("1")
            continueBtn = browser.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/section/section/form/div[4]/div/a")
            continueBtn.click()
            time.sleep(10)
            browser.find_element_by_id("first_name").send_keys(firstname)
            browser.find_element_by_id("last_name").send_keys(surname)
            browser.find_element_by_id("email_address").send_keys(email)
            browser.find_element_by_xpath(".//*[@id='primary_cta']/a").click()
            time.sleep(10)
        except:
            print("There was a problem adding " + firstname + " " + surname)

browser.close()