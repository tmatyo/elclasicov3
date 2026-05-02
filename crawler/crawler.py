#
# elclasico
# author: tmatyo
# v1.0 - 18-Mar-2019
# v2.0 - 17-May-2024
# v3.0 - 24-Mar-2026
#
# Tool for crawling livescore.sk to get next el clasico schedule and transfermarkt for historical data
#

import datetime
from typing import List
from playwright.sync_api import sync_playwright
from src.api import get_current_schedule, post_data

# things
schedule_url = "https://www.flashscore.sk/tim/real-madrid/W8mj7MDD/program/"
fixture_url = "https://www.transfermarkt.com/vergleich/vereineBegegnungen/statistik/131_418"
target = "Barcelona"


def crawl(mode):
    results = []
    print(f'Starting...{mode}')
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled']
        )
        page = browser.new_page(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        # Add stealth headers
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
        """)

        if (mode == "schedule"):
            page.goto(schedule_url)
            page.wait_for_selector('.event__match')
            results = get_schedule(page)
        elif (mode == "fixture"):
            page.goto(fixture_url)
            page.wait_for_load_state('networkidle')

            # Try to dismiss cookie consent popup if it exists
            try:
                page.click('button:has-text("Accept")', timeout=5000)
            except:
                pass

            try:
                page.click(
                    '[data-testid="cookie-accept"], .cookie-consent-accept, button[aria-label*="cookie"]', timeout=5000)
            except:
                pass

            # Try to click "Begin" button if verification page appears
            try:
                page.click('button:has-text("Begin")', timeout=5000)
                page.wait_for_load_state('networkidle')
            except:
                pass

            try:
                page.wait_for_selector('tr', timeout=60000)
            except Exception as e:
                # Save a screenshot for debugging
                now = datetime.datetime.now()
                debug_file_name = f"debug_{mode}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"
                page.screenshot(path=debug_file_name)
                print(f"Failed to find table, see {debug_file_name}: {e}")
                raise

            results = get_fixtures(page)
        else:
            print(f'Mode {mode} was useless...')

        browser.close()
        return results


def get_schedule(page) -> List:
    schedule = []

    # find the schedule
    matches = page.locator('.event__match')
    print(f"Scheduled matches: {matches.count()}:")

    # loop through the schedule to get relevant data
    for i in range(matches.count()):
        match = matches.nth(i)
        home = match.locator('.event__homeParticipant').inner_text()
        away = match.locator('.event__awayParticipant').inner_text()

        # if its elclasico, save data
        if (home.startswith(target) or away.startswith(target)):
            match_time = match.locator('.event__time').inner_text()

            date_cells = match_time.strip().split('.')
            crawl_time = f"{date_cells[1]}.{date_cells[0]}.{date_cells[2]}"
            now = datetime.datetime.now()
            year = now.year if is_date_in_future(
                now, crawl_time) else now.year + 1

            schedule.append({
                'time': match_time,
                'time_parsed': f"{str(year)}.{crawl_time}",
                'home_team': home,
                'away_team': away
            })

    print(f"El clasico found: {len(schedule)}")
    return schedule


def get_winner(home_team, home_score, away_team, away_score) -> str:
    home_score, away_score = int(home_score), int(away_score)
    return home_team if home_score > away_score else away_team if home_score < away_score else "remiza"


def get_stats(line) -> List:
    return [{
        'matches': int(line[0].inner_text()),
        'barca': int(line[1].inner_text()),
        'barca_goals': int(line[4].inner_text().split(':')[0]),
        'draw': int(line[2].inner_text()),
        'real': int(line[3].inner_text()),
        'real_goals': int(line[4].inner_text().split(':')[1]),
        'avg_attendance': float(line[5].inner_text())
    }]


def get_fixtures(tree) -> dict[str, List]:
    fixtures = []
    stats = []
    rows = tree.locator('tr')

    for i in range(rows.count()):
        row = rows.nth(i)
        cells = row.locator('td')
        count = cells.count()

        if (count == 6):
            stats = get_stats([cells.nth(i) for i in range(count)])

        if (count == 13):
            # match date
            date_text = cells.nth(3).inner_text()
            date = date_text.split(', ')
            date_parsed = date[1].strip().split('/')

            # team names
            home_team = cells.nth(7).locator('a').inner_text()
            away_team = cells.nth(10).locator('a').inner_text()

            # event data
            event = cells.nth(1).locator('img').get_attribute('title')
            match_report = cells.nth(12).locator('a').get_attribute('href')

            # parsing score to get winner
            score_meta = cells.nth(12).locator(
                'a').inner_text().strip().split(':')
            score_home = score_meta[0]
            score_away = score_meta[1].split(' ')[0]
            # print(f"{event} - {date_parsed[2]}-{date_parsed[1].zfill(2)}-{date_parsed[0].zfill(2)}")
            # putting together fixtures data
            fixtures.append({
                'date': f"{date_parsed[2]}-{date_parsed[1].zfill(2)}-{date_parsed[0].zfill(2)}",
                'home_team': home_team,
                'away_team': away_team,
                'event': event,
                'score': f"{score_home}:{score_away}",
                'winner': get_winner(home_team, score_home, away_team, score_away),
                'attendance': cells.nth(11).inner_text(),
                'link': f"https://www.transfermarkt.com{match_report}"
            })

    print(f"Fixtures found: {len(fixtures)}")
    return {'fixtures': fixtures, 'stats': stats}


def parse_date_string(match_time):
    d = match_time.strip().split('.')
    t = d[len(d) - 1].split(':')

    if (len(d) == 3):
        return [d[0], d[1], t[0], t[1]]

    if (len(d) == 4):
        return [d[0], d[1], d[2], t[0], t[1]]


def is_date_in_future(now, match_time):
    d = parse_date_string(match_time)

    if (len(d) == 4):
        the_match = datetime.datetime(now.year, int(
            d[0]), int(d[1]), int(d[2]), int(d[3]))
    else:
        the_match = datetime.datetime(int(d[0]), int(
            d[1]), int(d[2]), int(d[3]), int(d[4]))

    return the_match > now


def match_key(match):
    return (match["time_parsed"], match["home_team"], match["away_team"])


if __name__ == "__main__":
    # load old schedule
    old_schedule = get_current_schedule()
    print(f"Old schedule: {old_schedule}")

    # get new schedule
    new_schedule = crawl("schedule")
    print(f"New schedule: {new_schedule}")

    # no old schedule JSON or no elclasico was scheduled at last run
    # new crawl has an actual date, so its either a first run or a new match was scheduled since last crawl, lets get list of fixtures
    # if they would equal, nothing changed, so lets not waste compute on crawling a long list of fixtures, since nothing changed
    #
    # IMPORTANT: old_schedule_json[0] is not THE ONLY elclasico scheduled, but THE NEXT elclasico
    # new match was scheduled since last crawl with a closer date, or a match was played and another is still scheduled so lets get list of fixtures
    # if they would equal, nothing was played, so no need to waste compute on loading fixtures, since they would be the same
    same = (old_schedule and new_schedule and match_key(
        old_schedule[0]) == match_key(new_schedule[0]))

    if not same:
        print("Schedule changed, crawling fixtures...")
        fix_and_stat = crawl("fixture")
        post_data({**fix_and_stat, 'schedules': new_schedule})
    else:
        print("Schedule is the same, skipping crawling fixtures...")
