from django.db import models


class TeamStats(models.Model):
    team = models.CharField(max_length=30, verbose_name='Team', default="")
    team_name = models.CharField(max_length=30, verbose_name='Team Name', default="")
    wins = models.IntegerField(verbose_name='Wins', default=0)
    losses = models.IntegerField(verbose_name='Losses', default=0)
    ties = models.IntegerField(verbose_name='Ties', default=0)
    percentage = models.FloatField(verbose_name='Percentage', default=0.0)
    division = models.CharField(max_length=30, verbose_name='Division', default="")
    conference = models.CharField(max_length=30, verbose_name='Conference', default="")
    year = models.CharField(max_length=30, verbose_name='Year', default="")
    bye = models.CharField(max_length=30, verbose_name='Bye', default="")

    def __unicode__(self):
        return f"{self.team} {self.team_name} {self.wins} {self.losses} {self.ties} \
        {self.percentage} {self.division} {self.conference} {self.year} {self.bye}"

    def __str__(self):
        return self.__unicode__()


class PlayerStats(models.Model):
    rank = models.IntegerField(verbose_name='Rank', default=0)
    player = models.CharField(max_length=30, verbose_name='Player', default="")
    position = models.CharField(max_length=30, verbose_name='Position', default="")
    team = models.CharField(max_length=30, verbose_name='Team', default="")
    games = models.IntegerField(verbose_name='Games', default=0)
    completions = models.CharField(max_length=30, verbose_name='Completions', default="")
    attempts = models.CharField(max_length=30, verbose_name='Attempts', default="")
    percentage = models.CharField(max_length=30, verbose_name='Percentage', default="")
    yards = models.CharField(max_length=30, verbose_name='Yards', default="")
    yards_per_attempt = models.CharField(max_length=30, verbose_name='Yards per Attempt', default="")
    touch_downs = models.CharField(max_length=30, verbose_name='Touchdowns', default="")
    interceptions = models.CharField(max_length=30, verbose_name='Interceptions', default="")
    qb_rating = models.CharField(max_length=30, verbose_name='QB Rating', default="")
    avg_attempts = models.CharField(max_length=30, verbose_name='Average Attempts', default="")
    avg_yards = models.CharField(max_length=30, verbose_name='Average Yards', default="")
    avg_yards_per_attempt = models.CharField(max_length=30, verbose_name='Average Yards per Attempt', default="")
    avg_touch_downs = models.CharField(max_length=30, verbose_name='Average Touchdowns', default="")
    targets = models.CharField(max_length=30, verbose_name='Targets', default="")
    receptions = models.CharField(max_length=30, verbose_name='Receptions', default="")
    fumbles = models.CharField(max_length=30, verbose_name='Fumbles', default="")
    lost = models.CharField(max_length=30, verbose_name='Lost', default="")
    longs = models.CharField(max_length=30, verbose_name='Longs', default="")
    yards_per_target = models.CharField(max_length=30, verbose_name='Yards per Target', default="")
    yards_per_reception = models.CharField(max_length=30, verbose_name='Yards per Reception', default="")
    rushing = models.CharField(max_length=30, verbose_name='Rushing', default="")
    fg_made = models.CharField(max_length=30, verbose_name='Field Goals Made', default="")
    fg_attempts = models.CharField(max_length=30, verbose_name='Field Goals Attempts', default="")
    xp_made = models.CharField(max_length=30, verbose_name='Extra Points Made', default="")
    xp_attempts = models.CharField(max_length=30, verbose_name='Extra Point Attempts', default="")
    tackle_loss = models.CharField(max_length=30, verbose_name='Tackles for Loss', default="")
    sacks = models.CharField(max_length=30, verbose_name='Sacks', default="")
    qb_hits = models.CharField(max_length=30, verbose_name='QB Hits', default="")
    fum_rec = models.CharField(max_length=30, verbose_name='Fumbles Recovered', default="")
    safeties = models.CharField(max_length=30, verbose_name='Safeties', default="")
    def_td = models.CharField(max_length=30, verbose_name='Defensive Touchdowns', default="")
    return_td = models.CharField(max_length=30, verbose_name='Return Touchdowns', default="")
    pts_allowed = models.CharField(max_length=30, verbose_name='Points Allowed', default="")
    ppg = models.FloatField(verbose_name='Points per Game', default=0.0)
    fantasy_points = models.FloatField(verbose_name='Fantasy Points', default=0.0)
    year = models.CharField(max_length=30, verbose_name='Year', default="")
    points = models.CharField(max_length=30, verbose_name='Points', default="")

    def __unicode__(self):
        return f"{self.rank} {self.player} {self.position} {self.team} {self.games} {self.completions} {self.attempts} {self.percentage} {self.yards} \
        {self.yards_per_attempt} {self.touch_downs} {self.interceptions} {self.qb_rating} {self.avg_attempts} {self.avg_yards} {self.avg_yards_per_attempt} \
        {self.avg_touch_downs} {self.targets} {self.receptions} {self.fumbles} {self.lost} {self.longs} {self.yards_per_target} {self.yards_per_reception} \
        {self.rushing} {self.fg_made} {self.fg_attempts} {self.xp_made} {self.xp_attempts} {self.tackle_loss} {self.sacks} {self.qb_hits} {self.fum_rec} \
        {self.safeties} {self.def_td} {self.return_td} {self.pts_allowed} {self.ppg} {self.fantasy_points} {self.year} {self.points}"

    def __str__(self):
        return self.__unicode__()
