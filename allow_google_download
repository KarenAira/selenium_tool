from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import csv
import os
import requests
from requests import get

#prevent web close****************
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://192.168.10.86/#/login")

#download
prefs={"download.default_directory":" ~/Downloads"}
options.add_experimental_option("prefs", {
    "download.default_directory": " ~/Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


#********************************************

driver = webdriver.Chrome(service=service, options=options)
    #web IP for 192.168.10.122
driver.get("http://192.168.10.86/#/login")

title = driver.title
driver.implicitly_wait(10)
