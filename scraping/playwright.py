'''
-> [https://playwright.dev/python/docs/intro]
Para ejecutar Playwright primero debes tener instalado ciertas cosas:
*Dependencias:
	pip install pytest-playwright
*Navegadores requeridos:
	playwright install
'''

# Example test
import re # regular expretion
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# Exercise Scraping

from playwright.sync_api import sync_playwright

url = 'https://midu.dev'

with sync_playwright() as p:
	browser = p.chromium.lounch(headless=False, slow_mo=2000) # Los parametros que le pasamos permite visualizar lo que hace
	page = browser.new_page()
	page.goto(url)

	first_article = page.locator('article a').first
	print(first_article.text_content())
	first_article.click()

	page.wait_for_load_state()

	first_image = page.locator('main img').first
	image_src = first_image.get_atribute('src')
	print(f'La imagendel primer curso es: {image_src}')

	curso_content_container = page.locator('text:"Contenido del curso"')
	curso_content_sibling = curso_content_container.locator('xpath=./div/')
	# Informarce sobre 'xpath'
	browser.close()