import pprint

import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import  load_dotenv

load_dotenv()

my_email = os.environ["my_email"]
password = os.environ["password"]

Amazon_product_url = "https://www.amazon.in/dp/B0D268HBQY/?_encoding=UTF8&pd_rd_w=Td1Wd&content-id=amzn1.sym.a584271c-cdc4-4091-bd90-6d98b0b558bc&pf_rd_p=a584271c-cdc4-4091-bd90-6d98b0b558bc&pf_rd_r=PPSD3MMFJ8EMSQ9W7ZCQ&pd_rd_wg=4Im6T&pd_rd_r=a03ef59a-1621-491d-ac63-746ae8e2393d"

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.9,da;q=0.8,hi;q=0.7",
#     "Priority": "u=0, i",
#     "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"Windows\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#   }

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US"
}

response = requests.get(url=Amazon_product_url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
price = soup.find(class_="a-price-whole").get_text()

price = price.replace(",","")
print(price)
price_as_float = float(price)
print(price_as_float)


if price_as_float < 75000:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Hurray! Price for Instant Pot has dropped to ${price_as_float}."
        )
