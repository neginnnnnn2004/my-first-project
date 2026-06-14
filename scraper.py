from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import time

domains = [
    "pateh.com",
    "irangardmag.ir",
    "lastsecond.ir",
    "eligasht.com",
    "flytoday.ir",
    "seeiran.ir",
    "alibaba.ir",
    "irangard.com",
    "ittic.com",
    "safarmarket.com",
    "findatour.co",
    "destinationiran.com",
    "gardeshgari724.com",
    "mapgard.com",
    "eghamat24.com",
    "hamgardi.com",
    "irantouring.com",
    "irantourismonline.com",
    "emroozkojaberim.com",
    "anyja.ir",
    "iranview.ir",
    "kalouttravel.com",
    "kojaro.com",
    "iranhamsafar.com",
    "toptourist.ir",
    "rahbalad.com",
    "sedayemiras.ir",
    "mdsafar.com",
    "jabama.com",
    "iranhotelonline.com",
    "aminmana.com",
    "reiseniran.de",
    "saadatrent.com",
    "safarirani.ir",
    "ghasedak24.com",
    "avaair.ir",
    "setarehvanak.com",
    "niksanasafar.com",
    "esfahantours.ir",
    "snapptrip.com",
    "mysafar.com",
    "chap.sch.ir",
    "iranarze.ir"
]

data = []

print("🔥 در حال باز کردن Firefox با پروفایل شخصی شما...")

options = Options()
options.set_preference(
    "profile",
    r"C:\Users\Top\AppData\Roaming\Mozilla\Firefox\Profiles\ibbl3tp7.default-release"
)

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

driver.set_page_load_timeout(30)

for domain in domains:
    print(f"در حال بررسی {domain} ...")
    try:
        driver.get(f"https://trafficlens.io/analyze/{domain}")

        wait = WebDriverWait(driver, 25)

        xpath_rank = "//*[contains(text(),'Global Rank')]/following::*[1]"

        element = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_rank))
        )

        rank = element.text.strip()
        print(f"✅ {domain}: {rank}")
        data.append({"Domain": domain, "Global Rank": rank})

    except TimeoutException:
        print(f"⏱️ تایم‌اوت: {domain}")
        data.append({"Domain": domain, "Global Rank": "پیدا نشد"})

    except Exception as e:
        print(f"❌ خطا {domain}: {e}")
        data.append({"Domain": domain, "Global Rank": "خطا"})

    time.sleep(6)  # ضد بلاک + انسانی

driver.quit()

df = pd.DataFrame(data)
df.to_excel("TrafficLens_Ranks.xlsx", index=False)
print("✅ تموم شد — همه با Firefox خودت")