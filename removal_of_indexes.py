def nfl_teams():
    teams = ['Bengals', 'Bills', 'Patriots', 'Ravens', 'Steelers', 'Browns']
    teams = [team for (t, team) in enumerate(teams) if t not in (0, 4, 5)]
    print(teams)
