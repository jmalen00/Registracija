from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from random import randint


web = webdriver.Chrome()
web.get('https://www.links.hr/hr/register')
UreduLocation = web.find_elements_by_xpath('//*[@id="eu-cookie-ok"]')[0]
time.sleep(2)

Ime = 'sdjkfvhbbiwehrbihtreivthiwehtrurewvtuiwbehrturhvewuibtuirioverwtuioretbiuroetvbwervhturvhgdh"#442mmsnndjwgrugrjhqwbfjshuiwhrjwenrkjwegrhqwbrjkwehruizweruzeurhkjfbjbfubvuhvjrbvuhuwevrbuhrbvquhrbuvhrehwevruheuirqviobverhvbuhrvbhreubhwevurheuwvhrewuhrvuiewhruh'
Prezime = 'sdjkfvhbbiwehrbihtreivthiwehtrurewvtuiwbehrturhvewuibtuirioverwtuioretbiuroetvbwervhturvhgdh"#442mmsnndjwgrugrjhqwbfjshuiwhrjwenrkjwegrhqwbrjkwehruizweruzeurhkjfbjbfubvuhvjrbvuhuwevrbuhrbvquhrbuvhrehwevruheuirqviobverhvbuhrvbhreubhwevurheuwvhrewuhrvuiewhruh'
Ime2 = 'Ime'
Prezime2 = 'Prezime'
Lozinka = "aaaaaa"


ImeLocation = web.find_elements_by_xpath('//*[@id="FirstName"]')[0]
PrezimeLocation = web.find_elements_by_xpath('//*[@id="LastName"]')[0]
EmailLocation = web.find_elements_by_xpath('//*[@id="Email"]')[0]
LozinkaLocation = web.find_elements_by_xpath('//*[@id="Password"]')[0]
PotvrdaLozinkeLocation = web.find_elements_by_xpath('//*[@id="ConfirmPassword"]')[0]
RegistracijaLocation = web.find_elements_by_xpath('//*[@id="register-button"]')[0]

def ImePotrebno():
    try:
        web.find_element_by_xpath("//*[contains(text(), 'Ime je potrebno')]")
    except NoSuchElementException:
        return False
    return True
def PrezimePotrebno():
    try:
        web.find_element_by_xpath("//*[contains(text(), 'Prezime je potrebno.')]")
    except NoSuchElementException:
        return False
    return True
def EmailPotreban():
    try:
        web.find_element_by_xpath("//*[contains(text(), 'Elektronska pošta je potrebna')]")
    except NoSuchElementException:
        return False
    return True
def LozinaPotrebna():
    try:
        web.find_element_by_xpath("//*[contains(text(), 'Lozinka je potrebna.')]")
    except NoSuchElementException:
        return False
    return True
def UspjesnaRegistracija():
    try:
        web.find_element_by_css_selector('.result')
    except NoSuchElementException:
        return False
    return True
def ProvjeraTexta():
    if ImePotrebno():
        print("Crveni text ispod imena")
    else:
        print("Nema crvenog texta ispod imena")

    if PrezimePotrebno():
        print("Crveni text ispod prezimena")
    else:
        print("Nema crvenog texta ispod prezimena")

    if EmailPotreban():
        print("Crveni text ispod email polja")
    else:
        print("Nema crvenog texta ispod email polja")

    if LozinaPotrebna():
        print("Crveni text ispod polja za lozinku")
    else:
        print("Nema crvenog texta ispod polja za lozinku")
def ProvjeraRegistracije():
    if UspjesnaRegistracija():
        print("Registracija uspjesna")
    else:
        print("Doslo je problema prilikom registracije")




UreduLocation.click()

time.sleep(2)

print("PRVI TEST")
RegistracijaLocation.click()
ProvjeraTexta()
print(" ")


print("DRUGI TEST")
EmailLocation.send_keys("test" + str(randint(25, 111111111)) + "@test.test")
ProvjeraTexta()
print(" ")


print("TRECI TEST")
EmailLocation.clear()
ImeLocation.send_keys(Ime)
PrezimeLocation.send_keys(Prezime)
EmailLocation.send_keys("test" + str(randint(25, 111111111)) + "@test.test")
LozinkaLocation.send_keys(Lozinka)
PotvrdaLozinkeLocation.send_keys(Lozinka)
RegistracijaLocation.click()
ProvjeraTexta()
ProvjeraRegistracije()
print(" ")

print("CETVRTI TEST")
web.execute_script("window.history.go(-1)")
ImeLocation = web.find_elements_by_xpath('//*[@id="FirstName"]')[0]
PrezimeLocation = web.find_elements_by_xpath('//*[@id="LastName"]')[0]
EmailLocation = web.find_elements_by_xpath('//*[@id="Email"]')[0]
LozinkaLocation = web.find_elements_by_xpath('//*[@id="Password"]')[0]
PotvrdaLozinkeLocation = web.find_elements_by_xpath('//*[@id="ConfirmPassword"]')[0]
RegistracijaLocation = web.find_elements_by_xpath('//*[@id="register-button"]')[0]
ImeLocation.clear()
PrezimeLocation.clear()
EmailLocation.clear()
LozinkaLocation.clear()
PotvrdaLozinkeLocation.clear()
ImeLocation.send_keys(Ime2)
PrezimeLocation.send_keys(Prezime2)
EmailLocation.send_keys("test" + str(randint(25, 111111111)) + "@test.test")
LozinkaLocation.send_keys(Lozinka)
PotvrdaLozinkeLocation.send_keys(Lozinka)
RegistracijaLocation.click()
ProvjeraTexta()
ProvjeraRegistracije()

