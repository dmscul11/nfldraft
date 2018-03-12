from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from nfldata.models import PlayerStats, TeamStats
from django.db.models import Sum
import csv
import numpy as np


# Create views
def index(request):
    return render(request, 'nfldata/homepage.html')


# adds stats to table
def view_nfldata(request):
    players = PlayerStats.objects.order_by('-position', '-year', '-fantasy_points')
    config = {'players': players}
    return render(request, 'view_nfldata.html', config)


# adds stats to table
def view_teamdata(request):
    teams = TeamStats.objects.order_by('team', 'year')
    config = {'teams': teams}
    return render(request, 'view_teamdata.html', config)


# adds stats to table
def view_myteam(request):
    players = PlayerStats.objects.filter(owner='team Mine')\
        .order_by('-position', 'player', '-year')
    config = {'players': players}
    return render(request, 'view_myteam.html', config)


# pick best player left for current team
def draft_best(team):
    team_pos = ['RB','WR','QB','TE','DST','K']

    for pos in team_pos:
        # check for next open position
        owned = PlayerStats.objects.filter(position=pos, owner='team ' + str(team),\
            year='2016', points='Points')

        if (len(owned) < 1) or (len(owned) <= 1 and pos in ['RB','WR']):

            # get players left for position, sort by points, select first
            player = PlayerStats.objects.filter(position=pos, owner='Free Agent',\
                year='2016', points='Points').order_by('-fantasy_points')[0]
            PlayerStats.objects.filter(position=pos, owner='Free Agent', player=player.player)\
                .update(owner='team ' + str(team))
            break


# update all owners to free agent
def clear_owners():
    PlayerStats.objects.all().update(owner='Free Agent')


# compile draft outputs
def view_draftresults(request, num_teams, my_team):
    # display draft results
    output = []
    for t in range(1, num_teams+1):
        if t != my_team:
            team_name = 'team ' + str(t)
        else:
            team_name = 'team Mine'

        #teams.append(team_name)
        fp = PlayerStats.objects.filter(owner=team_name, year='2017', points='Points').aggregate(Sum('fantasy_points'))
        tn = PlayerStats.objects.filter(owner=team_name, year='2017', points='Points').order_by('team').values('team').distinct()
        bye = TeamStats.objects.filter(year='2017', team__in=tn).order_by('bye').values('bye').distinct()
        pl = PlayerStats.objects.filter(owner=team_name, year='2017', points='Points').order_by('player').values('player').distinct()
        output.append({'team_name': team_name, 'total_pts': fp['fantasy_points__sum'], 'byes': list(bye.values_list('bye', flat=True)),
            'teams': list(tn.values_list('team', flat=True)), 'players': list(pl.values_list('player', flat=True))})

    config = {'output': output}
    return render(request, 'view_draftresults.html', config)


# runs fantasy draft
def begin_draft(request):

    # set params if not as input
    clear_owners()
    num_teams = 10
    my_team = np.random.randint(1, num_teams)

    # loop through teams forward then backward for draft
    iterations = list(range(1, num_teams+1, 1)) + list(range(num_teams, 0, -1))\
        + list(range(1, num_teams+1, 1)) + list(range(num_teams, 0, -1))\
        + list(range(1, num_teams+1, 1)) + list(range(num_teams, 0, -1))\
        + list(range(1, num_teams+1, 1)) + list(range(num_teams, 0, -1))
    for i in iterations:
        #if random team draft best player for position
        if i != my_team:
            draft_best(i)

        # if my team then draft special
        elif i == my_team:
            draft_best('Mine')

    return view_draftresults(request, num_teams, my_team)



# adds stats to table
def add_nfldata(request):

    # delete data in database first

    # get data sheets
    player_sheet = '/Users/deirdre/Documents/AAI/Project/NFLF-players.csv'
    team_sheet = '/Users/deirdre/Documents/AAI/Project/NFLF-team-records.csv'

    # read in and save team data
    with open(team_sheet) as tf:
        reader = csv.reader(tf)

        # skip headers iterate through teams
        next(tf)
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
            player = PlayerStats(rank=row[0], player=row[1], owner='Free Agent',
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

