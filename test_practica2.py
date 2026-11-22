"""Práctica 2: 3 pruebas Selenium WebDriver con 2+ asserts cada una."""
from pathlib import Path
import re
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = 'https://automationexercise.com'
ROOT = Path(__file__).resolve().parent
EVIDENCIAS = ROOT / 'evidencias'
EVIDENCIAS.mkdir(exist_ok=True)

class Practica2(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(60)
        self.wait = WebDriverWait(self.driver, 30)

    def tearDown(self):
        self.driver.quit()

    def captura(self, nombre):
        ruta = EVIDENCIAS / f'{nombre}.png'
        self.driver.save_screenshot(str(ruta))
        print(f'Captura guardada: {ruta}')

    def test_01_login_incorrecto(self):
        d = self.driver
        d.get(BASE + '/login')
        email = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="login-email"]')))
        email.send_keys('invalido_prueba_2026@example.com')
        d.find_element(By.NAME, 'password').send_keys('ClaveIncorrecta123')
        d.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()
        mensaje = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//form[@action="/login"]//p')))
        self.assertIn('Your email or password is incorrect!', mensaje.text)  # Assert 1
        self.assertIn('/login', d.current_url)  # Assert 2
        self.captura('01_login_incorrecto')

    def test_02_busqueda_productos(self):
        d = self.driver
        d.get(BASE + '/products')
        buscador = self.wait.until(EC.visibility_of_element_located((By.ID, 'search_product')))
        buscador.send_keys('top')
        d.find_element(By.ID, 'submit_search').click()
        titulo = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[contains(@class,"title") and contains(normalize-space(.),"SEARCHED PRODUCTS")]')))
        self.assertIn('SEARCHED PRODUCTS', titulo.text.upper())  # Assert 1
        nombres = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.features_items .productinfo p')))
        textos = [n.text.strip() for n in nombres if n.text.strip()]
        self.assertTrue(any('top' in t.lower() for t in textos), f'No hay productos relacionados con top: {textos}')  # Assert 2
        self.captura('02_busqueda_productos')

    def test_03_suscripcion(self):
        d = self.driver
        d.get(BASE)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'susbscribe_email')))
        d.execute_script('arguments[0].scrollIntoView({block:"center"});', email)
        self.wait.until(EC.visibility_of(email))
        email.send_keys(f'prueba_selenium_{datetime.now():%Y%m%d%H%M%S}@example.com')
        d.find_element(By.ID, 'subscribe').click()
        aviso = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#success-subscribe .alert-success')))
        self.assertIn('You have been successfully subscribed!', aviso.text)  # Assert 1
        self.assertTrue(aviso.is_displayed())  # Assert 2
        self.captura('03_suscripcion')

if __name__ == '__main__':
    unittest.main(verbosity=2)
