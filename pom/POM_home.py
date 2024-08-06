from selenium.webdriver.common.by import By

logoScope = [By.XPATH, "//*[@class='nav-logo']"]
searchScope = [By.ID, "search-input"]
burgerMenu = [By.XPATH, "//*[contains(@class,'icon-burger')]"]
nasionalBurger = [By.XPATH, "//*[@class='list-nav-kanal'][2]"]
internasionalBurger = [By.XPATH, "//*[@class='list-nav-kanal'][3]"]

hiLite = [By.XPATH, "//*[contains(@class,'fas fa-plus fa-fw hi-lite')]"]
moreHilite = [By.XPATH, "//*[@class='hi-lite']"]

imgSpecialScope = [By.XPATH, "//img[@alt='Kejar Tayang Agar Merah Putih Berkibar di IKN']"]
titleScopeSpecial = [By.XPATH, "//*[contains(text(),'Kejar Tayang Agar Merah Putih Berkibar di IKN')]"]
moreScopeSpecial = [By.XPATH, "//*[@id='view-more-scope-1']"]

imgNews = [By.XPATH, "//*[@data-src='https://pict.sindonews.net/dyn/414/pena/sindoscope/2024/07/401/artis-di-pilkada-pendulang-suara-atau-penggembira-cil.jpg']"]
titleNews = [By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/a/div/div[2]/div"]
moreNews = [By.ID, "view-more-scope-0"]
hideMore = [By.ID, "view-hide-scope-0"]
moreALLNews = [By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[6]/div[5]/a/div/div"]

#=========================================== FOOTER ==================================================
sindoFooter = [By.XPATH, "//*[@src='https://az.sindonews.net/dyn/600/mobile/2016/images/logo/sindonews-logo-center.png']"]
appStore = [By.XPATH, '//*[@id="end-of-article"]/div[1]/div[1]/div[2]/a[1]/img']
playStore = [By.XPATH, '//*[@id="end-of-article"]/div[1]/div[1]/div[2]/a[2]/img']
fbFooter = [By.XPATH, "//*[@alt='fb']"]
xFooter = [By.XPATH, "//*[@alt='tw']"]
igFooter = [By.XPATH, "/html/body/div[2]/footer/div[1]/div[1]/div[3]/a[3]/img"]
ytFooter = [By.XPATH, "//*[@alt='yt']"]
tiktokFooter = [By.XPATH, "//*[@alt='tiktok']"]
