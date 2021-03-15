from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "",
#     password = ""
# )

chrome_option = Options()
chrome_option.add_argument("--incognito")
chrome_option.add_argument("--window-size=1920x1028")

driver = webdriver.Chrome(chrome_options=chrome_option, executable_path= "D:\ChromeDriver\chromedriver.exe" )
url = "https://coinmarketcap.com/?page=2"
driver.get(url)
time.sleep(10)

while True:
    try:
        driver.execute_script("window.scrollTo(0, 0)")
        for i in range(1, 101):
            driver.execute_script("window.scrollTo(0, "+str(i*100)+")")
            list = {}
            if i == 11:
                continue

            name = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(3) p")
            price = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(4) a")
            day_percent = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(5) span")
            week_percent = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(6) span")
            market_cap = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(7) p")
            volume = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(8) a>p")
            coin_volume = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(8) p")
            circulating_supply = driver.find_element_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(9) p")

            list["name"] = name.text
            list["price"] = price.text

            if driver.find_elements_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(5) span.icon-Caret-up"):
                list["day_percent"] = "+" + day_percent.text
            else:
                list["day_percent"] = "-" + day_percent.text

            if driver.find_elements_by_css_selector("tr:nth-child("+str(i)+") td:nth-child(6) span.icon-Caret-up"):
                list["week_percent"] = "+" + week_percent.text
            else:
                list["week_percent"] = "-" + week_percent.text

            list["market_cap"] = market_cap.text
            list["volume"] = volume.text
            list["coin_volume"] = coin_volume.text
            list["circulating_supply"] = circulating_supply.text
            print(list)

        time.sleep(1)
    except KeyboardInterrupt:
        #get out of while loop on control-c
        driver.quit()
        print('Exit program')
        break

    finally:
        pass



