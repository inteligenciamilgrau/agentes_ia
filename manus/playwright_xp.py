from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://www.inteligenciamilgrau.com.br')
    print(page.title())
    page.screenshot(path=f'example.png')
    browser.close()
