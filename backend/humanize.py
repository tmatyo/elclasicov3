
import asyncio
import random


async def delay_before_next_page(delay_min=2.5, delay_max=5.0):
    delay = random.uniform(delay_min, delay_max)
    print(f"Waiting for {delay:.2f} seconds before loading next page...")
    await asyncio.sleep(delay)


async def mouse_move(page):
    viewport = page.viewport_size
    if not viewport:
        return

    width, height = viewport['width'], viewport['height']

    for _ in range(random.randint(1, 3)):
        x = random.randint(0, width)
        y = random.randint(0, height)
        await page.mouse.move(x, y)
        await asyncio.sleep(random.uniform(0.1, 2.5))


async def scroll_page(page):
    position = 0
    total_height = await page.evaluate('document.body.scrollHeight')

    while position < total_height:
        scroll_step = random.randint(150, 400)
        await page.mouse.wheel(0, scroll_step)
        position += scroll_step
        await asyncio.sleep(random.uniform(0.1, 2.5))


async def random_browser_identity(browser):

    windows_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edge/12.10240",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    ]

    windows_viewports = [
        {"width": 1920, "height": 1080},
        {"width": 1366, "height": 768},
        {"width": 1440, "height": 900},
    ]

    mac_user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    ]

    mac_viewports = [
        {"width": 2560, "height": 1600},
        {"width": 1440, "height": 900},
        {"width": 3024, "height": 1964},
        {"width": 1728, "height": 1117}
    ]

    windows_user = {
        "user_agent": random.choice(windows_user_agents),
        "viewport": random.choice(windows_viewports)
    }

    mac_user = {
        "user_agent": random.choice(mac_user_agents),
        "viewport": random.choice(mac_viewports)
    }

    user_agents = random.choice([windows_user, mac_user])

    locale = random.choice(["en-US", "sk-SK", "de-DE", "hu-HU", "cs-CZ"])

    context = await browser.new_context(
        user_agent=user_agents["user_agent"], viewport=user_agents["viewport"], locale=locale, timezone_id="Europe/Bratislava")

    return context
