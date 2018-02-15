from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from nfldata.models import PlayerStats, TeamStats
import csv


# Create views
def index(request):
    return render(request, 'nfldata/homepage.html')

# adds stats to table
def view_nfldata(request):
    return HttpResponse('Table empty')

# adds stats to table
def add_nfldata(request):

    # delete data in database first

    # get data sheets
    player_sheet = '/Users/deirdre/Documents/AAI/NFLF-players.csv'
    team_sheet = '/Users/deirdre/Documents/AAI/NFLF-team-records.csv'

    # read in and save team data
    with open(team_sheet) as pf:
        reader = csv.reader(pf)

        # skip headers iterate through teams
        next(pf)
        for row in reader:
            team = TeamStats(team=row[0], team_name=row[1],
                wins=row[2], losses=row[3], ties=row[4],
                percentage=row[5], division=row[6], conference=row[7],
                year=row[8], bye=row[9])
            team.save()

    # read in and save player data
    with open(player_sheet) as pf:
        reader = csv.reader(pf)

        # skip headers iterate through players
        next(pf)
        for row in reader:
            player = PlayerStats(rank=row[0], player=row[1],
                position=row[2], team=row[3], games=row[4],
                completions=row[5], attempts=row[6], percentage=row[7], 
                yards=row[8], yards_per_attempt=row[9], touch_downs=row[10],
                interceptions=row[11], qb_rating=row[12], avg_attempts=row[13], 
                avg_yards=row[14], avg_yards_per_attempt=row[15], 
                avg_touch_downs=row[16], targets=row[17], receptions=row[18], 
                fumbles=row[19], lost=row[20], longs=row[21], yards_per_target=row[22],
                yards_per_reception=row[23], rushing=row[24], fg_made=row[25], 
                fg_attempts=row[26], xp_made=row[27], xp_attempts=row[28], 
                tackle_loss=row[29], sacks=row[30], qb_hits=row[31], 
                fum_rec=row[32], safeties=row[33], def_td=row[34], 
                return_td=row[35], pts_allowed=row[36], ppg=row[37], 
                fantasy_points=row[38], year=row[39], points=row[40])
            player.save()

    return HttpResponse('Data added')

# runs fantasy draft
def begin_draft(request):
    return HttpResponse('Not started')
