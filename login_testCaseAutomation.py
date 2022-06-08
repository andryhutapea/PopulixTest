
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Menjalankan Web Browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Membuka Website Populix
# scrip ini kita gunakan untuk membuka halaman login 
urlLogin="https://www.populix.co/login/"
browser.maximize_window()
browser.get(urlLogin)
time.sleep(4)

emails = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_email"]')))
passwords = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]')))

# Testcase 1
# Klik button Masuk
# script ini bertujuan untuk menguji apakah fungsi  login berhasil apabila kolom username dan password di isi kosong 
browser.find_element(By.ID, value="submit_login").click()
print("Test case 1 selesai")
time.sleep(5)

# Testcase 2
# script ini bertujuan untuk menguji apakah fungsi  login berhasil apabila kolom username di isi degan email valid dan password di isi kosong
browser.find_element(By.NAME, value="username").send_keys("qa@gmail.com")
browser.find_element(By.NAME, value="password").send_keys("")
browser.find_element(By.ID, value="submit_login").click()
print("Test case 2 selesai")
time.sleep(5)

# Testcase 3
# script ini bertujuan untuk menguji apakah fungsi  login berhasil apabila kolom username di isi kosong dan password di isi degan password yang valid
emails.send_keys(Keys.CONTROL + "a" + Keys.DELETE) 
passwords.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
time.sleep(2)
browser.find_element(By.NAME, value="username").send_keys("")
browser.find_element(By.NAME, value="password").send_keys("engineer")
browser.find_element(By.ID, value="submit_login").click()
print("Test case 3 selesai")
time.sleep(5)

# Test case 4
# username dan Password yang akan kita masukkan di halaman login Populix
username = "qa@gmail.com"
password = "engineer"
# script ini kita gunakan untuk Mengisi kolom username dan Password secara otomatis setelah halaman login terbuka
emails.send_keys(Keys.CONTROL + "a" + Keys.DELETE) 
passwords.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
time.sleep(2)
browser.find_element(By.NAME, value="username").send_keys(username)
browser.find_element(By.NAME, value="password").send_keys(password)
# Klik Masuk
# script ini bertujuan untuk menguji apakah fungsi button login setelah username dan password di input dan melihat apakah login berhasil atau tidak dengan asumsi email dan password yang dimasukkan sudah terdaftar/valid
browser.find_element(By.ID, value="submit_login").click()
print("Test case 4 selesai")
time.sleep(4)

# Test case 5
# Klik Lupa Kata Sandi
# script ini bertujuan untuk menguji apakah fungsi "Lupa Kata Sandi" berjalan atau tidak, apakah user diarahkan ke halaman lupa kata sandi setelah di klik
browser.find_element(By.ID, value="btn_to-forgot-password").click()
print("go to forget password page")
time.sleep(4)
print("Test case 5 selesai")
browser.find_element(By.ID, value="btn_resend").click()
print("back to login page")

# Test case 6
# klik Daftar
# script ini bertujuan untuk menguji apakah fungsi "Daftar" berjalan atau tidak, apakah user diarahkan ke halaman registrasi setelah di klik
browser.find_element(By.ID, value="btn_to-register").click()
print("go to Register page")
time.sleep(4)
print("Test case 6 selesai")
browser.find_element(By.PARTIAL_LINK_TEXT, value="Masuk Sekarang").click()
print("back to login page")

# Test Case 7
# klik Facebook
# script ini bertujuan untuk menguji apakah fungsi "Login dengan Facebook" berjalan atau tidak, apakah user diarahkan ke halaman login facebook setelah d klik
browser.find_element(By.XPATH, '//*[@id="login_facebook"]').click()
print("go to login facebook page")
time.sleep(4)
print("Test case 7 selesai")
browser.get(urlLogin)
print("back to login page")

# test Case 8
# klik Google
# Script ini bertujuan untuk menguji apakah fungsi "Login dengan Google" berjalan atau tidak, apakah user diarahkan ke halaman login Google setelah d klik
browser.find_element(By.XPATH, '//*[@id="login_google"]').click()
print("go to login google page")
time.sleep(4)
print("Test case 8 selesai")
browser.get(urlLogin)
print("back to login page")
time.sleep(10)

