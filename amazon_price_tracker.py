from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

USERNAME = "your gmail"
PASSWORD = "your password"

url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=pd_sbs_1/141-1748437-1065127" \
      "?pd_rd_w=AE2uz&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=VQSBBWKT1DA91RM53RC8&pd_rd_r=3cc74378-0a58" \
      "-4c95-b833-4fad3283abee&pd_rd_wg=uMDKJ&pd_rd_i=B075CWJ3T8&th=1"
header = {
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,fa;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                  "KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# scraping for the desired content which is the price of the item and its title
price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}".encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(USERNAME, PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=USERNAME,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
