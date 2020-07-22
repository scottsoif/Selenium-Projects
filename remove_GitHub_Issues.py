#
#   I was working with the GitHub Rest API
#   and created lots of issues. So here is a 
#   bot to bulk delete the repo issues
#
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Specify webdrive location
browser = webdriver.Chrome('/Users/scottsoifer/coding/selenium/chromedriver')

##   Modify you github repo url here
browser.get('https://github.com/scottsoif/CrowdIt/issues')

## 1. Run this file interactively (i.e. 'python -i remove_GitHub_Issues.py') 
#  2. When you run this file a webpage should display
#  3. Log into you GitHub account
#  4. In the python shell enter remove_all_issues() and Voilà

def remove_all_issues():

    # Adjust range depending on how many issues you need to remove
    for i in range(0,100):
        try:
            elem = browser.find_element_by_id(f'issue_{i}_link')
            elem.click()
            elem =browser.find_element_by_class_name("octicon-trashcan")
            elem.click()
            elem = browser.find_element_by_name("verify_delete")
            elem.click()
            print(f"Deleted issue #: {i}")
        except NoSuchElementException:
            print("Not found")
