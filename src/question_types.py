from pyautogui import write
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .config.basic_info import WAIT_TIME
import time


def fill_text(b, inputfield, text):
    element = b.find_element(By.XPATH, inputfield)
    ActionChains(b).move_to_element(element).click().send_keys(text).perform()


def fill_with_click(b, box):
    element = b.find_element(By.XPATH, box)
    element.click()


def fill_dropdown(b, box, option):
    dropdown_menu = b.find_element(By.XPATH, box)
    dropdown_menu.click()

    time.sleep(WAIT_TIME)

    for i in range(option):
        write(["down"])
    write(["enter"])
