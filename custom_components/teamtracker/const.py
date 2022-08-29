# API
LEAGUE_LIST = [
    ["MLB", "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard", "mdi:baseball"],
    ["NBA", "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard", "mdi:basketball"],
    ["WNBA", "https://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard", "mdi:basketball"],
    ["NCAAM", "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard", "mdi:basketball"],
    ["NCAAW", "https://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/scoreboard", "mdi:basketball"],
    ["NCAAF", "http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard", "mdi:football"],
    ["NFL", "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard", "mdi:football"],
    ["NHL", "http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard", "mdi:hockey-puck"],
    ["BUND", "http://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard", "mdi:soccer"],
    ["EPL", "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard", "mdi:soccer"],
    ["LIGA", "http://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard", "mdi:soccer"],
    ["LIG1", "http://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard", "mdi:soccer"],
    ["MLS", "http://site.api.espn.com/apis/site/v2/sports/soccer/usa.1/scoreboard", "mdi:soccer"],
    ["NWSL", "http://site.api.espn.com/apis/site/v2/sports/soccer/usa.nwsl/scoreboard", "mdi:soccer"],
    ["SERA", "http://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard", "mdi:soccer"]
    ]
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"

# Config
CONF_TIMEOUT = "timeout"
CONF_TEAM_ID = "team_id"
CONF_LEAGUE_ID = "league_id"

# Defaults
DEFAULT_ICON = "mdi:scoreboard"
DEFAULT_NAME = "team_tracker"
DEFAULT_LEAGUE = "NFL"
DEFAULT_TIMEOUT = 120
DEFAULT_PROB = 0.0
DEFAULT_LEAGUE_LOGO = "https://cdn0.iconfinder.com/data/icons/shift-interfaces/32/Error-512.png"
DEFAULT_API_ENDPOINT = "http://site.api.espn.com/apis/site/v2/sports/league/not/found"

# Misc
TEAM_ID = ""
VERSION = "0.1"
ISSUE_URL = "https://github.com/vasqued2/ha-teamtracker"
DOMAIN = "teamtracker"
PLATFORM = "sensor"
ATTRIBUTION = "Data provided by ESPN"
COORDINATOR = "coordinator"
PLATFORMS = ["sensor"]
