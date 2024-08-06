from selenium.webdriver.common.by import By

from helper.action import *
from helper.config import *
from pom.POM_home import *


def test_logo_scope(openDriver):
    #openDriver.find_element(By.XPATH, "//*[@class='nav-logo']").click()
    # Bikin file POM_home.py
    #openDriver.find_element(logoScope[0], logoScope[1]).click()
    # Setelah bikin File action
    element_click(openDriver, logoScope)
    validasi_url(openDriver, wpWeb)


def test_search_scope(openDriver):
    #openDriver.find_element(By.ID, "search-input").send_keys("covid")
    #Bikin file POM_home.py
    #openDriver.find_element(searchScope[0], searchScope[1]).send_keys("covid")
    # Setelah bikin File action
    element_input(openDriver, searchScope, "covid")

def test_burger_menu(openDriver):
    #openDriver.find_element(By.XPATH, "//*[contains(@class,'icon-burger')]").is_displayed()

    # Bikin file POM_home.py
    #openDriver.find_element(burgerMenu[0], burgerMenu[1]).click()
    #Setelah bikin File action
    validate_is_display(openDriver, burgerMenu)

def test_scope_special(openDriver):
    # Bikin file POM_home.py
    #openDriver.find_element(imgSpecialScope[0], imgSpecialScope[1]).is_displayed()
    validate_is_display(openDriver, imgSpecialScope)
    validate_is_display(openDriver, titleScopeSpecial)
    validasi_title(openDriver, titleScopeSpecial)
    validasi_color_title(openDriver, titleScopeSpecial)
    validasi_img(openDriver, imgSpecialScope)
    element_click(openDriver, moreScopeSpecial)

def test_scope_News(openDriver):
    validate_is_display(openDriver, imgNews)
    validasi_img(openDriver, imgNews)
    validasi_title(openDriver, titleNews)
    element_click(openDriver, moreNews)
    element_click(openDriver, moreALLNews)
    validasi_url(openDriver, newsMoreScope)
    #element_click(openDriver, hideMore)

def test_logo_sindo_footer(openDriver):
    validasi_img(openDriver, sindoFooter)
    element_click(openDriver, sindoFooter)
    validasi_url(openDriver, wpWeb)

def test_downloadApp_footer(openDriver):
    validate_is_display(openDriver, appStore)
    validate_is_display(openDriver, playStore)

def test_fb_footer(openDriver):
    element_click(openDriver, fbFooter)
    validasi_url(openDriver, fbSindo)

def test_x_footer(openDriver):
    element_click(openDriver, xFooter)
    validasi_url(openDriver, xSindo)

def test_ig_footer(openDriver):
    element_click(openDriver, igFooter)
    validasi_url(openDriver, igSindo)

def test_yt_footer(openDriver):
    element_click(openDriver, ytFooter)
    validasi_url(openDriver, ytSindo)

def test_tiktok_footer(openDriver):
    element_click(openDriver, tiktokFooter)
    validasi_url(openDriver, tiktokSindo)


