from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pandas as pd
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

navegador = webdriver.Chrome(options=chrome_options)          # '/usr/bin/chromedriver'
navegador.get('http://tutorialsninja.com/demo/')
navegador.maximize_window()
sleep(1)

# ############################# SELECT 2 IPHONES, TAKE A SCREENSHOT AND ADD BOTH TO THE CART ###################################################

#PRESS PHONES BUTTON
phones = navegador.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phones.click()
sleep(1)

#PRESS IPHONE BUTTON
iphone = navegador.find_element(By.XPATH, '//a[text()="iPhone"]')
iphone.click()
sleep(1)

#Click in iphone image
iphone_img = navegador.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
iphone_img.click()
sleep(1)


#Now we want to press the right arrow button 5 times to go to the last image of the Iphone
arrow_button = navegador.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

for i in range(5):
    arrow_button.click()
    sleep(1)
    
#Now we want to get a screenshot and save it as a png
navegador.save_screenshot('screenshot_ecom_iphone.png')


#Now we will press the x button to close the image
close_btn = navegador.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
close_btn.click()
sleep(1)


#We like this iphone so much that we want to buy 2 of them
quantity = navegador.find_element(By.ID, 'input-quantity')
quantity.click()
sleep(1)
#primeiro vamos apagar o valor que está lá por default (que é 1)
quantity.clear()
sleep(1)
#Now we want to put 2 in the box
quantity.send_keys(Keys.NUMPAD2)
#quantity.send_keys('2')     #BOTH WORK
sleep(1)


#Now we want to press the Add to Cart button
add_cart_btn = navegador.find_element(By.ID, 'button-cart')
add_cart_btn.click()
sleep(1)

#######################################################################################################################################

############################# SELECT HP COMPUTER, DEFINE A SPECIFIC DELIVERY DATE AND ADD TO CART #####################################

#Lets go to the Laptop buttons and select all laptops
laptop_btn = navegador.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
action = ActionChains(navegador)
action.move_to_element(laptop_btn).perform()
# laptop_btn.click()
sleep(1)

#Show All Laptops & Notebooks
all_laptops_btn = navegador.find_element(By.XPATH, '//a[text()="Show All Laptops & Notebooks"]')
all_laptops_btn.click()
sleep(1)

#Now we want to select the HP LP3065 computer
pc_hp_btn = navegador.find_element(By.XPATH, '//a[text()="HP LP3065"]')
pc_hp_btn.click()
sleep(1)


#Now we will scroll down to a button that we want (in this case the add to cart button)
# We actually didn't need to do that but is cool to know how its done

add_cart_btn2 = navegador.find_element(By.XPATH, '//button[@id="button-cart"]')
add_cart_btn2.location_once_scrolled_into_view
sleep(1)


#Now we want to select the day of the delivery so we need to press the Calendar button
calendar_btn = navegador.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar_btn.click()
sleep(1)


#Select a delivery date for: 31-12-2022
#First select Month and Year: December 2022
next_btn = navegador.find_element(By.XPATH, '//th[@class="next"]')
month_year = navegador.find_element(By.XPATH, '//th[@class="picker-switch"]')
while month_year.text != 'December 2022':
    next_btn.click()

sleep(1)

#select day 31
calendar_date = navegador.find_element(By.XPATH, '//td[text()="31"]')
calendar_date.click()
sleep(1)

#After the delivery date is selected we will add the computer to the cart:
add_cart_btn2.click()      #we already have defined the xpath for the add to cart button above so we just need to click in it
sleep(1)

##########################################################################################################################################


######################################### CREATE A GUEST ACCOUNT AND COMPLETE CHECK OUT PROCESS ###########################################

#click in the cart button
cart_btn = navegador.find_element(By.ID, 'cart-total')
cart_btn.click()
sleep(0.5)

#click in the checkout button
checkout_btn = navegador.find_element(By.XPATH, '//p[@class="text-right"]/a[2]')
checkout_btn.click()
sleep(0.5)


#But now im in the checkout and i can go through because they don't have Iphones in stock so I will delete that article from the cart
delete_btn = navegador.find_element(By.XPATH, '//button[@class="btn btn-danger"][1]')
delete_btn.click()
sleep(0.5)

#Now I need to press the checkout button again
checkout_btn2 = navegador.find_element(By.XPATH, '//a[text()="Checkout"]')
checkout_btn2.click()
sleep(0.5)

#Select procedd as guest
guest_checkout_btn = navegador.find_element(By.XPATH, '//input[@value="guest"]')
guest_checkout_btn.click()
sleep(0.5)

#Then press continue to go to step2
continue_btn = navegador.find_element(By.ID, 'button-account')
continue_btn.click()
sleep(0.5)

#In the Step2 we are going to need to scroll down. So that the "title": Step2: Billing Details goes to the top of the website
scroll_step2 = navegador.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]')
scroll_step2.location_once_scrolled_into_view
sleep(0.5)


#Now fill that shit
first_name = navegador.find_element(By.ID, 'input-payment-firstname')
first_name.click()
sleep(1)
first_name.send_keys('Daniela')

last_name = navegador.find_element(By.ID, 'input-payment-lastname')
last_name.click()
sleep(1)
last_name.send_keys('Bartilotti')

email = navegador.find_element(By.ID, 'input-payment-email')
email.click()
sleep(1)
email.send_keys('figas.23.fantasy@gmail.com')

tele = navegador.find_element(By.ID, 'input-payment-telephone')
tele.click()
sleep(1)
tele.send_keys('918775067')

address = navegador.find_element(By.ID, 'input-payment-address-1')
address.click()
sleep(1)
address.send_keys('Rua de O Primeiro de Janeiro')

city = navegador.find_element(By.ID, 'input-payment-city')
city.click()
sleep(1)
city.send_keys('Boavista')

post_code = navegador.find_element(By.ID, 'input-payment-postcode')
post_code.click()
sleep(1)
post_code.send_keys('4100-365')


country = navegador.find_element(By.ID, 'input-payment-country')
country.click()
dropdown = Select(country)
dropdown.select_by_visible_text('Portugal')
sleep(1)


region = navegador.find_element(By.ID, 'input-payment-zone')
region.click()
dropdown2 = Select(region)
dropdown2.select_by_visible_text('Porto')
sleep(1)


#Now that we filled that shit we are going to press the continue button
continue_btn2 = navegador.find_element(By.ID, 'button-guest')
continue_btn2.click()
sleep(1)

# Text for the delivery guy
text_area = navegador.find_element(By.XPATH, '//textarea[@class="form-control"]')
text_area.click()
text_area.send_keys('The Client shall be addressed as Princess Daniela')
sleep(2)

#Press another continue btn
continue_btn3 = navegador.find_element(By.ID, 'button-shipping-method')
continue_btn3.click()
sleep(1)

# Accept terms and conditions
terms_checkbox = navegador.find_element(By.XPATH, '//input[@name="agree"]')
terms_checkbox.click()
sleep(0.5)


continue_btn4 = navegador.find_element(By.ID, 'button-payment-method')
continue_btn4.click()
sleep(0.5)


#Now we reach a table and we want to extract the total cost of the purchase
preço_final = navegador.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print(f"The final price of the purchase is: {preço_final.text}")


