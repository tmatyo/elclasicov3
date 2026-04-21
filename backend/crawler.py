#
# elclasico
# author: tmatyo
# v1.0 - 18-Mar-2019
# v2.0 - 17-May-2024
# v3.0 - 24-Mar-2026
#
# Tool for crawling livescore.sk to get next el clasico schedule and transfermarkt for historical data
#

import json
import datetime
from playwright.sync_api import sync_playwright

# things
schedule_url = "https://www.flashscore.sk/tim/real-madrid/W8mj7MDD/program/"
fixture_url = "https://www.transfermarkt.com/vergleich/vereineBegegnungen/statistik/131_418"
target = "Barcelona"
old_schedule_json = []
new_schedule_json = []


def view_source(mode):
    print(f'Starting...{mode}')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        if (mode == "schedule"):
            page.goto(schedule_url)
            page.wait_for_selector('.event__match')
            get_schedule(page)
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

            try:
                page.wait_for_selector('tr', timeout=60000)
            except Exception as e:
                # Save a screenshot for debugging
                page.screenshot(path="fixture_debug.png")
                print(f"Failed to find table: {e}")
                raise

            get_fixtures(page)
        else:
            print(f'Mode {mode} was useless...')

        browser.close()


def get_schedule(page):
    schedule = []

    # find the schedule
    matches = page.locator('.event__match')
    print(f"Matches found: {matches.count()}:")

    # loop through the schedule to get relevant data
    for i in range(matches.count()):
        match = matches.nth(i)
        home = match.locator('.event__homeParticipant').inner_text()
        away = match.locator('.event__awayParticipant').inner_text()
        print(f"{home} vs {away}")

        # if its elclasico, save data
        if (home.startswith(target) or away.startswith(target)):
            match_time = match.locator('.event__time').inner_text()

            date_cells = match_time.strip().split('.')
            crawl_time = f"{date_cells[1]}.{date_cells[0]}.{date_cells[2]}"
            now = datetime.datetime.now()

            if (is_date_in_future(crawl_time)):
                match_time_parsed = f"{str(now.year)}.{crawl_time}"
            else:
                match_time_parsed = f"{str(now.year + 1)}.{crawl_time}"

            schedule.append({
                'time': match_time,
                'time_parsed': match_time_parsed,
                'home_team': home,
                'away_team': away
            })

    print(schedule)

    if not schedule:
        schedule = [False]

    json_dump('schedule', schedule)


def get_winner(home_team, home_score, away_team, away_score):
    home_score, away_score = int(home_score), int(away_score)
    return home_team if home_score > away_score else away_team if home_score < away_score else "remiza"


def get_stats(line):
    stats = [{
        'matches': line[0].inner_text(),
        'barca': line[1].inner_text(),
        'barca_goals': line[4].inner_text().split(':')[0],
        'draw': line[2].inner_text(),
        'real': line[3].inner_text(),
        'real_goals': line[4].inner_text().split(':')[1],
        'avg_attendance': line[5].inner_text()
    }]

    json_dump('stats', stats)


def get_fixtures(tree):
    fixtures = []
    rows = tree.locator('tr')

    for i in range(rows.count()):
        row = rows.nth(i)
        cells = row.locator('td')
        count = cells.count()

        if (count == 6):
            get_stats([cells.nth(i) for i in range(count)])

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
            print(
                f"{event} - {date_parsed[2]}-{date_parsed[1].zfill(2)}-{date_parsed[0].zfill(2)}")
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

    json_dump('fixtures', fixtures)


def json_dump(filename, data):
    with open(f"{filename}.json", 'wt') as file:
        json.dump(data, file)


def json_read(filename):
    array = [False]
    try:
        with open(f"{filename}.json", 'r') as file:
            array = json.load(file)
    except:
        pass

    return array


def parse_date_string(match_time):
    d = match_time.strip().split('.')
    t = d[len(d) - 1].split(':')

    if (len(d) == 3):
        return [d[0], d[1], t[0], t[1]]

    if (len(d) == 4):
        return [d[0], d[1], d[2], t[0], t[1]]


def is_date_in_future(match_time):
    d = parse_date_string(match_time)
    now = datetime.datetime.now()

    if (len(d) == 4):
        the_match = datetime.datetime(now.year, int(
            d[0]), int(d[1]), int(d[2]), int(d[3]))
    else:
        the_match = datetime.datetime(int(d[0]), int(
            d[1]), int(d[2]), int(d[3]), int(d[4]))

    return the_match > now


if __name__ == "__main__":

    # load old schedule
    old_schedule_json = json_read('schedule')

    # get new schedule
    view_source("schedule")
    new_schedule_json = json_read('schedule')

    # no old schedule JSON or no elclasico was scheduled at last run
    # new crawl has an actual date, so its either a first run or a new match was scheduled since last crawl, lets get list of fixtures
    # if they would equal, nothing changed, so lets not waste compute on crawling a long list of fixtures, since nothing changed
    #
    # IMPORTANT: old_schedule_json[0] is not THE ONLY elclasico scheduled, but THE NEXT elclasico
    # new match was scheduled since last crawl with a closer date, or a match was played and another is still scheduled so lets get list of fixtures
    # if they would equal, nothing was played, so no need to waste compute on loading fixtures, since they would be the same
    if (old_schedule_json[0] != new_schedule_json[0]):
        view_source("fixture")
