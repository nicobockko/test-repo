import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect

def scrolldown(page):
    _prev_height = -1
    _max_scrolls = 100
    _scroll_count = 0
    while _scroll_count < _max_scrolls:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)
        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == _prev_height : break
        _prev_height = new_height
        _scroll_count += 1

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=%EC%95%88%EB%85%95")
    scrolldown(page)
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
