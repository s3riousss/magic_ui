from selenium.webdriver.common.by import By

first_name = (By.ID, 'firstname')
last_name = (By.ID, 'lastname')
email = (By.ID, 'email_address')
password = (By.ID, 'password')
confirm_password = (By.ID, 'password-confirmation')
btn_create_account = (By.CLASS_NAME, 'submit')
alert = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
first_name_error = (By.ID, 'firstname-error')
last_name_error = (By.ID, 'lastname-error')
email_error = (By.ID, 'email_address-error')
password_error = (By.ID, 'password-error')
confirm_password_error = (By.ID, 'password-confirmation-error')
