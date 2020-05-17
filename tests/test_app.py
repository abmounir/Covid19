from covid19 import Covid

def test_covid19():
    assert Covid().get_population('algeria') == '43,748,441 '
