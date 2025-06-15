from pages.google_page import GooglePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
os.makedirs("reports", exist_ok=True)

def test_google_search(driver):
    #driver.get("https://www.google.com")
    google = GooglePage(driver)
    google.load()



    # Accepter les cookies si présent (Google peut afficher un pop-up)
    try:
        agree_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Accept all'] or .//div[text()='Accepter tout']]"))
        )
        agree_btn.click()
    except:
        pass  # pas de pop-up => continuer

    # Attendre que le champ de recherche soit visible et interactif
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    #search_box.send_keys("OpenAI\n")
    google.search("OpenAI")


    # Vérifier que le titre contient "OpenAI"
    WebDriverWait(driver, 10).until(
        EC.title_contains("OpenAI")
    )
    assert "OpenAI" in driver.title

