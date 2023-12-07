import csv
from selenium.webdriver.common.by import By
import time
import csv
from seleniumbase import Driver
driver = Driver(uc=True)

with open('URL.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        Region = row[0]
        driver.get(row[1])

        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        Region_links = []

        City_Used = "N/A"

        try:
            try:
                if driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/main/div/ul/li/a'):
                    UL_elements = driver.find_elements(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/div/main/div/ul/li/a')
                    for UL_element in UL_elements:
                        UL_link = UL_element.get_attribute("href")
                        Region_links.append(UL_link)
            except:
                print("")
            
            try:
                if driver.find_element(By.XPATH,'//*[@id="gatsby-focus-wrapper"]/div/div/div/main/div/li'):
                    LI_elements = driver.find_elements(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div/div/div/main/div/li/a')
                    for LI_element in LI_elements:
                        LI_link = LI_element.get_attribute("href")
                        Region_links.append(LI_link)
            except:
                print("")

        except:
            print("There is no ELEMENT")
        
        for Region_link in Region_links:
            print("Successful >>> ", Region_link)
            driver.get(Region_link)

            try:
                Name = driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-header > div.provider-name > h1').text
            except:
                Name = "Empty"

            try:
                Title = driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-header > h2').text
            except:
                Title = "Empty"

            try:
                State = Region
            except:
                State = "Empty"

            try:
                Features= driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-header > div.provider-badges').text
                Features = Features.replace("\n", ", ")
            except:
                Features = "Empty"

            try:
                Bio = driver.find_element(By.CSS_SELECTOR, 'article.profile-bio').text
                Bio.replace("\n", ", ")
            except:
                Bio = "Empty"

            try:
                Specialities = ""
                Specialities_elements = driver.find_elements(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > ul:nth-child(5)>li')
                for Specialities_element in Specialities_elements:
                    Specialities = Specialities +  Specialities_element.text
            except:
                Specialities = "Empty"

            Accepted_insurances_ALL = ""
            try:

                image_modal_button = driver.find_elements(By.CSS_SELECTOR, 'button.icon')[0]
                image_modal_button.click()
                more_insurances = driver.find_elements(By.XPATH, '//*[@id="provider-insurances"]/section/div/ul/li/span')
                for more_insurance in more_insurances:
                    Accepted_insurances_ALL = Accepted_insurances_ALL + more_insurance.text
            except:
                print("There is no button")

            driver.find_element(By.XPATH, '//*[@id="provider-insurances_label"]/button').click()

            try:
                See_all_specialities = ""
                if driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > button'):
                    driver.find_element(By.XPATH, '/html/body/main/div[1]/section[2]/button').click()
                    more_infors = driver.find_elements(By.XPATH, '//*[@id="profile-full-specialty-list"]/section/div/ul/li')
                    for more_infor in more_infors:
                        See_all_specialities = See_all_specialities + more_infor.text
                    driver.find_element(By.XPATH, '//*[@id="profile-full-specialty-list_label"]/button/img').click()
                else:
                    print("There is no Button")
                    
            except:
                See_all_specialities = "Empty"

            try:
                Methods = ""
                Methods_elements = driver.find_elements(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > ul:nth-child(7) > li')
                for Methods_element in Methods_elements:
                    Methods = Methods +  Methods_element.text
            except:
                Methods = "Empty"

            try:
                if driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > h3:nth-child(11)').text == "License":
                    Licenses = driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > ul:nth-child(12) > li > span').text
                else:
                    Licenses = driver.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ul[3]/li/span').text
            except:
                Licenses = "Empty"

            try:
                if driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > h3:nth-child(13)').text == "Accepted insurance providers":
                    Accept_Insurance = driver.find_element(By.CSS_SELECTOR, 'body > main > div.provider-profile > section.provider-profile-detail-card > ul:nth-child(14) > li > span').text
                else:
                    Accept_Insurance = driver.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ul[4]/li/span').text
            except:
                Accept_Insurance = "Empty"

            try:
                if driver.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/h3[5]').text == "Languages spoken":
                    Language = driver.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ul[5]/li/span').text
                else:
                    Language = driver.find_element(By.XPATH, '/html/body/main/div[1]/section[2]/ul[5]/li/span').text
            except:
                Language = "Empty"

            Session_informations = ""
            try:
                session_elements = driver.find_elements(By.XPATH, '/html/body/main/div/section[2]/ul[last()]/li/span')
                for session_element in session_elements:
                    Session_informations = Session_informations + session_element.text
            except:
                Session_informations = "Empty"

            price_range = ""
            try:
                price_box = driver.find_element(By.XPATH, '/html/body/main/div/section[3]/ul')
                if price_box:
                    price_range = "$5-40"
                    Min = price_range.split("-")[0]
                    Max = "$" + price_range.split("-")[1]

            except:
                price_range="Empty"
                Min="Empty"
                Max="Empty"

            try:
                slot_count=""
                slot_elements = driver.find_elements(By.CLASS_NAME, 'with-slots')
                slot_count = len(slot_elements)
            except:
                slot_count = "0"

            results = [Region, City_Used, Region_link, Name, Title, State, Features, Bio, Specialities, See_all_specialities, Methods, Licenses, Accept_Insurance, Accepted_insurances_ALL, Language, Session_informations, price_range, Min, Max, slot_count]

            with open('clients.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(results)
driver.close()    