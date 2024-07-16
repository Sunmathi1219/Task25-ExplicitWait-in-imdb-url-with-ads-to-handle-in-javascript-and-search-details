""""
Using Python selenium,explicit wait,expected conditions and chrome webdriver kindly do the following task mentioned below
1.) go to the https://www.imdb.com/search/name/
2.)fill the data given in the input boxes,select boxes and drop down menu on the web page and do a search
3.)do bot use sleep() method fot the task.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
#for explicit wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Name_Search:
     driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     wait=WebDriverWait(driver,20)

     def __init__(self,url):
         self.url = url

     def start(self):
         try:
           #open the url
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
         except WebDriverException as e:
             print(e)
             return False


     def search(self):
        try:
          #To scroll this page for  skip the ad using javascrip scrollby
          self.driver.execute_script('window.scrollBy(0, 500)')

          #enter data in text boxes

          #to click the expand button
          expand_button=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='adv-search-expand-all']//span[text()='Expand all']")))
          #expand_button.click()

          # if click is not working while automation then using javascrip click
          self.driver.execute_script("arguments[0].click();", expand_button)

          # name of the actor
          name = self.wait.until(EC.presence_of_element_located((By.NAME, "name-text-input")))
          name.send_keys("Vijay")

          #birthdate
          start_birthdate=self.wait.until(EC.presence_of_element_located((By.NAME, "birth-date-start-input")))
          start_birthdate.send_keys("22-06-1974")
          end_birthdate=self.wait.until(EC.presence_of_element_located((By.NAME, "birth-date-end-input")))
          end_birthdate.send_keys("22-06-1974")

          self.driver.execute_script('window.scrollBy(0, 500)')
          #gender
          gender=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='test-chip-id-MALE']//span")))
          #gender.click()

          #if click is not working while automation then using javascrip click
          self.driver.execute_script("arguments[0].click();", gender)


          #results
          result_button=self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='adv-search-get-results']//span[text()='See results']")))
          result_button.click()
          print("The relevant details of the actor search is successful")
          return True


        except NoSuchElementException as e:
             print(e)
             return False

        finally:
             self.driver.quit()
             return None


"""
if __name__ == "__main__":
    url="https://www.imdb.com/search/name/"
    name_search=Name_Search(url)
    name_search.start()
    name_search.search()


"""



