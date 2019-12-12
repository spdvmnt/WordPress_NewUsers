from selenium import webdriver
import time
import os, sys, inspect
import random
import string
from sys import platform


def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))



def newuser():

        domaininput = input('Domain (member.example.com):')
        domain = 'https://' + domaininput
        wpuser = input("WP Admin User:")
        wppass = input('WP Admin Password:')
        usercount = input('How many Users do you need? (500):')
        startnumber = input('Where to start counting users? (1000):')


        current_folder = os.path.realpath(
            os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
        #chromedriver1 = os.path.join(current_folder, "chromedriver")

        if platform == "linux" or platform == "linux2":
            linux = True
        else:
            linux = False

        if linux == True:

            firefoxdriver1 = os.path.join(current_folder, "geckodriver")
        else:
            firefoxdriver1 = os.path.join(sys._MEIPASS, "geckodriver.exe")

        driver = webdriver.Firefox(executable_path=firefoxdriver1)
        driver.get(domain + '/wp-admin/user-new.php')
        searchwpuser = driver.find_element_by_name('log')
        searchwpuser.send_keys(wpuser)
        searchwppass = driver.find_element_by_name('pwd')
        searchwppass.send_keys(wppass)
        searchwppass.submit()
        time.sleep(2)

        for i in range(int(startnumber), int(startnumber)+int(usercount)):
            newuser = 'member' + str(i)
            newemail = newuser + '@example.com'
            newpass = randomStringDigits(10)

            driver.get(domain + '/wp-admin/user-new.php')

            searchusernew = driver.find_element_by_id('user_login')
            searchusernew.send_keys(newuser)

            searchemailnew = driver.find_element_by_id('email')
            searchemailnew.send_keys(newemail)

            searchchoosecategory = driver.find_element_by_xpath('//*[@id="createuser"]/table[1]/tbody/tr[6]/td/button')
            searchchoosecategory.click()

            searchwppass2 = driver.find_element_by_name('pass1')
            searchwppass2.clear()
            for c in newpass:
                searchwppass2.send_keys(c)
                time.sleep(0.1)
            searchwppass2.submit()
            time.sleep(3)

            #print('User: ' + newuser + ' Password: ' + newpass)
            text_file = open("members.txt", "a")
            n = text_file.write('User: ' + newuser + ' Password: ' + newpass + '\n')
            text_file.close()

        driver.quit()
        print('Work is Done!')

if __name__ == '__main__':
    newuser()