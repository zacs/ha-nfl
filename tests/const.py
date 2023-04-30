"""Constants for tests."""

CONFIG_DATA = {
    "league_id": "MLB",
    "team_id": "MIA",
    "name": "test_tt_all_test01",
    "timeout": 120,
    "conference_id": "9999",
}

CONFIG_DATA2 = {
    "league_id": "NCAAF",
    "team_id": "OSU",
    "name": "test_tt_all_test02",
    "timeout": 120,
    "conference_id": "5",
}

TEST_DATA = [
    {
        "sensor_name": "test_tt_all_test01",
        "sport": "baseball",
        "league": "MLB",
        "team_abbr": "MIA",
    },
    {
        "sensor_name": "test_tt_all_test02",
        "sport": "baseball",
        "league": "MLB",
        "team_abbr": "MIL",
    },
    {
        "sensor_name": "test_tt_all_test03",
        "sport": "baseball",
        "league": "MLB",
        "team_abbr": "CIN",
    },
    {
        "sensor_name": "test_tt_all_test04",
        "sport": "football",
        "league": "NCAAF",
        "team_abbr": "BGSU",
    },
    {
        "sensor_name": "test_tt_all_test05",
        "sport": "football",
        "league": "NCAAF",
        "team_abbr": "ALA",
    },
    {
        "sensor_name": "test_tt_all_test06",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "BUF",
    },
    {
        "sensor_name": "test_tt_all_test07",
        "sport": "soccer",
        "league": "NWSL",
        "team_abbr": "ORL",
    },
    {
        "sensor_name": "test_tt_all_test08",
        "sport": "soccer",
        "league": "MLS",
        "team_abbr": "CLB",
    },
    {
        "sensor_name": "test_tt_all_test09",
        "sport": "soccer",
        "league": "WC",
        "team_abbr": "ARG",
    },
    {
        "sensor_name": "test_tt_all_test10",
        "sport": "basketball",
        "league": "NBA",
        "team_abbr": "DET",
    },
    {
        "sensor_name": "test_tt_all_test11",
        "sport": "basketball",
        "league": "NBA",
        "team_abbr": "UTAH",
    },
    {
        "sensor_name": "test_tt_all_test12",
        "sport": "basketball",
        "league": "NBA",
        "team_abbr": "CHA",
    },
    {
        "sensor_name": "test_tt_all_test13",
        "sport": "hockey",
        "league": "NHL",
        "team_abbr": "WPG",
    },
    {
        "sensor_name": "test_tt_all_test14",
        "sport": "hockey",
        "league": "NHL",
        "team_abbr": "NYI",
    },
    {
        "sensor_name": "test_tt_all_test15",
        "sport": "hockey",
        "league": "NHL",
        "team_abbr": "CBJ",
    },
    {
        "sensor_name": "test_tt_all_test16",
        "sport": "volleyball",
        "league": "NCAAVBW",
        "team_abbr": "PEPP",
    },
    {
        "sensor_name": "test_tt_all_test17",
        "sport": "volleyball",
        "league": "NCAAVBW",
        "team_abbr": "MSST",
    },
    {
        "sensor_name": "test_tt_all_test18",
        "sport": "volleyball",
        "league": "NCAAVBW",
        "team_abbr": "ARMY",
    },
    {
        "sensor_name": "test_tt_all_test19",
        "sport": "tennis",
        "league": "WTA",
        "team_abbr": "KALININA",
    },
    {
        "sensor_name": "test_tt_all_test20",
        "sport": "tennis",
        "league": "WTA",
        "team_abbr": "BOGDAN",
    },
    {
        "sensor_name": "test_tt_all_test21",
        "sport": "tennis",
        "league": "WTA",
        "team_abbr": "PARTAUD",
    },
    {
        "sensor_name": "test_tt_all_test22",
        "sport": "mma",
        "league": "UFC",
        "team_abbr": "STRICKLAND",
    },
    {
        "sensor_name": "test_tt_all_test23",
        "sport": "mma",
        "league": "UFC",
        "team_abbr": "CACERES",
    },
    {
        "sensor_name": "test_tt_all_test24",
        "sport": "mma",
        "league": "UFC",
        "team_abbr": "FAKHRETDINOV",
    },
    {
        "sensor_name": "test_tt_all_test25",
        "sport": "golf",
        "league": "PGA",
        "team_abbr": "CONNERS",
    },
    {
        "sensor_name": "test_tt_all_test26",
        "sport": "cricket",
        "league": "XXX",
        "team_abbr": "BH",
    },
    {
        "sensor_name": "test_tt_all_test27",
        "sport": "cricket",
        "league": "XXX",
        "team_abbr": "MR",
    },
    {
        "sensor_name": "test_tt_all_test28",
        "sport": "cricket",
        "league": "XXX",
        "team_abbr": "IND",
    },
    {
        "sensor_name": "test_tt_all_test29",
        "sport": "racing",
        "league": "F1",
        "team_abbr": "SAINTZ",
    },
    {
        "sensor_name": "test_tt_all_test30",
        "sport": "racing",
        "league": "F1",
        "team_abbr": "VERSTAPPEN",
    },
    {
        "sensor_name": "test_tt_all_test31",
        "sport": "racing",
        "league": "F1",
        "team_abbr": "STROLLZ",
    },
]

MULTIGAME_DATA = [
    {
        "sensor_name": "test_tt_all_test01",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "CLE",  #PRE, PRE
        "expected_event_name": "BAL @ CLE"
    },
    {
        "sensor_name": "test_tt_all_test02",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "CIN", # PRE, IN
        "expected_event_name": "PIT @ CIN"
    },
    {
        "sensor_name": "test_tt_all_test03",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "BAL", # PRE, POST
        "expected_event_name": "TB @ BAL"
    },
    {
        "sensor_name": "test_tt_all_test04",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "PIT",  #IN, PRE
        "expected_event_name": "PIT @ CIN"
    },
    {
        "sensor_name": "test_tt_all_test05",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "GB", # IN, IN
        "expected_event_name": "GB @ ATL"
    },
    {
        "sensor_name": "test_tt_all_test06",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "TB", # IN, POST
        "expected_event_name": "TB @ BAL"
    },
    {
        "sensor_name": "test_tt_all_test07",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "NE",  #POST, PRE
        "expected_event_name": "NE @ TB"
    },
    {
        "sensor_name": "test_tt_all_test08",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "JAX", # POST, IN
        "expected_event_name": "JAX @ WSH"
    },
    {
        "sensor_name": "test_tt_all_test09",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "BUF", # POST, POST
        "expected_event_name": "IND @ BUF"
    },
    {
        "sensor_name": "test_tt_all_test10",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "*",  #PRE, PRE
        "expected_event_name": "GB @ ATL"
    },
    {
        "sensor_name": "test_tt_all_test11",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "KNC", # PRE, IN
        "expected_event_name": "KNC @ ARI"
    },
    {
        "sensor_name": "test_tt_all_test12",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "TNT", # PRE, POST
        "expected_event_name": "NYG @ TNT"
    },
    {
        "sensor_name": "test_tt_all_test13",
        "sport": "football",
        "league": "NFL",
        "team_abbr": "NOT_FOUND", # PRE, POST
        "expected_event_name": None
    },
]