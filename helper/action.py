from assertpy import assert_that


def element_click(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).click()

def element_input(openDriver, pom, text):
    openDriver.find_element(pom[0], pom[1]).send_keys(text)

def validate_is_display(openDriver, pom):
    openDriver.find_element(pom[0], pom[1]).is_displayed()

def validasi_is_equals(text1, text2):
    assert_that(text1).is_equal_to(text2)

def validasi_url(openDriver, text):
    openDriver.get(text)

def validasi_img (openDriver, pom):
    elementImg = openDriver.find_element(pom[0], pom[1])
    width = elementImg.get_property("width")
    height = elementImg.get_property("height")
    print(width)
    print(height)

def validasi_title (openDriver, pom):
    elementFont = openDriver.find_element(pom[0], pom[1])
    fontSize = elementFont.value_of_css_property("font-size")
    print(fontSize)

def validasi_color_title (openDriver, pom):
    elementColor = openDriver.find_element(pom[0], pom[1])
    color = elementColor.value_of_css_property("color")
    print(color)





