#!/usr/bin/env python3
import os
import subprocess
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.sync_api import sync_playwright

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(base, "assets/maestro"), exist_ok=True)
os.makedirs(os.path.join(base, "assets/rebecca"), exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 900})
    page.goto("file://" + base + "/maestro/index.html")
    page.wait_for_timeout(2500)
    page.screenshot(
        path=os.path.join(base, "assets/maestro/maestro-workflow-preview.png"),
        full_page=False,
    )

    page.set_viewport_size({"width": 1200, "height": 800})
    page.goto("file://" + base + "/projects/agent-rebecca.html#output")
    page.wait_for_timeout(1500)
    page.locator(".rapport-mockup").screenshot(
        path=os.path.join(base, "assets/rebecca/rebecca-rapport-preview.png")
    )

    page.goto("file://" + base + "/projects/agent-rebecca.html#database")
    page.wait_for_timeout(1000)
    page.locator(".db-mockup").screenshot(
        path=os.path.join(base, "assets/rebecca/rebecca-dashboard-preview.png")
    )
    browser.close()

print("Screenshots captured.")
