from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.in/New-Apple-iPhone-Mini-64GB/dp/B08L5TDRQC/ref=sr_1_1_sspa?dchild=1&keywords=iphone&qid=1623753041&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExS082R0M1SUlXSDZWJmVuY3J5cHRlZElkPUEwMjQ1NDg2TEM0WEhZQzI0U1ZOJmVuY3J5cHRlZEFkSWQ9QTAzMTUyNjAyODlZRERXR1pLSE9SJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",'Accept-Language':"en-US,en;q=0.9"}

request = requests.get(PRODUCT_URL,headers=header)
supe = BeautifulSoup(request.content,'lxml')
price = supe.find('span',class_="a-size-medium a-color-price priceBlockBuyingPriceString")
real_price = price.get_text().split()[1]
prices = real_price.split(',')
price1 = prices[0]
price2 = prices[1]
price3 = f"{price1}{price2}"
finalprice = int(float(price3))


sender = 'shuvratcp@gmail.com'
password = 'iamacool'
receiver = 'shuvra232@gmail.com'
massage = f"iPhone 12 price is now {real_price} . Hurry!"

if finalprice < 70000:
   with smtplib.SMTP('smtp.gmail.com',port=587) as mail:
       mail.starttls()
       mail.login(user=sender,password=password)
       try:
           mail.sendmail(from_addr=sender,to_addrs=receiver,msg=f"Subject: iPhone 12 Price dropped\n\n{massage}")
       except UnicodeEncodeError:
           print("Error")


