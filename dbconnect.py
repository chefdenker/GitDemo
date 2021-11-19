import mysql.connector

dbuser = ""
dbpassword =""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dbadmin',
    database='sakila'
)
##-----------------------------

cursor = db.cursor()
cursor.execute('select username from staff where staff_id = 3 limit 10')

for f in cursor:
    print(f)
    dbuser = f

cursor.execute('select password from staff where staff_id = 3 limit 10')
for f in cursor:
    print(f)
    dbpassword = f

print (dbuser)
print (dbpassword)
## ----------------------------------- credentials known -> connect

##driver = webdriver.Chrome(executable_path="C:\Drivers\cd95\chromedriver.exe")  # starts chrome
driver = webdriver.Chrome(executable_path="C:\Drivers\cd95\chromedriver.exe")  # starts chrome

driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)

user_ele=driver.find_element_by_name("userName")

print(user_ele.is_displayed())   #returns true/false based of element status
print(user_ele.is_enabled())     # returns true/false

pwd_ele=driver.find_element_by_name("password")

print(pwd_ele.is_displayed())   #returns true/false based of element status
print(pwd_ele.is_enabled())     # returns true/false

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("submit").click()

# new lines for GitDemo
time.sleep(5)
driver.quit()
