# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Firefox()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Firefox()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
# time.sleep(5)
# browser.close()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("python")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(10)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Firefox()
#     browser.get(link)
#
    # input1 = browser.find_element(By.TAG_NAME, 'input')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, 'last_name')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
#
# finally:
#     time.sleep(20)
#     browser.quit()



import math
# link = "http://suninjuly.github.io/find_link_text"

# try:
#     browser = webdriver.Firefox()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, '224592')
#     link.click()
#
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     link.click()
#     browser.quit()

# print(str(math.ceil(math.pow(math.pi, math.e)*10000)))

# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта. В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение. Теперь эта задача под силу только роботам ﻿🤖﻿.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Firefox()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for element in elements:
#         element.send_keys("По умолчанию")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# На этот раз воспользуемся возможностью искать элементы по XPath.


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Firefox()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//div/*[text()='Submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

