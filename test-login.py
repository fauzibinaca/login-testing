from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Mengatur opsi Selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument('--disable-gpu')
options.add_argument("--enable-cookies")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Inisialisasi Service untuk ChromeDriver
service = Service('/usr/bin/chromedriver')  # Sesuaikan path dengan lokasi ChromeDriver

# Inisialisasi WebDriver dengan Service
driver = webdriver.Chrome(service=service, options=options)

try:
    # Buka halaman login
    driver.get("https://fauzi.ukm.id/dashboard/")
    time.sleep(2)  # Tunggu halaman selesai dimuat

    # Temukan elemen input untuk username dan password
    username_field = driver.find_element(By.NAME, "log")  # Gantilah 'username' dengan nama elemen sebenarnya
    password_field = driver.find_element(By.NAME, "pwd")  # Gantilah 'password' dengan nama elemen sebenarnya

    # Masukkan username dan password
    username_field.send_keys("YOUR_USERNAME")  # Masukkan username di sini
    password_field.send_keys("YOUR_PASSWORD")  # Masukkan password di sini

    # Klik tombol Login
    login_button = driver.find_element(By.NAME, "wp-submit")  # Gantilah dengan XPATH tombol login jika berbeda
    login_button.click()
    time.sleep(3)  # Tunggu sampai halaman beralih

    # Verifikasi keberhasilan login
    if "dashboard/sitepages/" in driver.current_url:
        print("Login berhasil.")
    else:
        print("Login gagal.")


except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    # Tutup browser
    driver.quit()
