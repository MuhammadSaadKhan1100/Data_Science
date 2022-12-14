# Game script
"""

from NBAGameSimulator import *
import numpy as np

gsw = Team('GSW',[90,100,110,120],[85,90,100,110])
cle = Team('CLE',[90,99,108,117],[85,90,100,110])

msim = MatchupSimulator(gsw,cle)

msim.gamesSim(1000)

# Simulator.py:
"""

import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt


class Team:
    """Team creates an object that can be passed into the simulation. Takes a Team Name (String)
    points (list), and opp_points (List) """
    
    def __init__(self, TeamName,points, opp_points):
        self.TeamName = TeamName
        self.points = points
        self.opp_points = opp_points
    
    #Returns avg of points
    def pointsavg(self):
        return np.mean(self.points)
    
    #Returns standard deviation of points
    def pointsstd(self):
        return np.std(self.points)
    #returns avg of opponent points
    def opp_pointsavg(self):
        return np.mean(self.opp_points)
    #returns standard deviation of opponent points 
    def opp_pointsstd(self):
        return np.std(self.opp_points)

class MatchupSimulator:
    """ Simulates single game outcomes as well as multiple outcomes"""
    def __init__(self, Team1,Team2):
        self.Team1 = Team1
        self.Team2 = Team2
        self.results = []
    
    #Simulates a single game returns 1 if team 1 wins, returns -1 if Team 2 wins, and returns 0 if the game is tied
    def gameSim(self):
        #Averages the random sample of a teams points with a random sample of the number of points the opponent allows
        #Randomly samples from the two gaussian distributions to produce a probabilistic outcome
        T1 = (rnd.gauss(self.Team1.pointsavg(),self.Team1.pointsstd())+ rnd.gauss(self.Team2.opp_pointsavg(),self.Team2.opp_pointsstd()))/2
        T2 = (rnd.gauss(self.Team2.pointsavg(),self.Team2.pointsstd())+ rnd.gauss(self.Team1.opp_pointsavg(),self.Team1.opp_pointsstd()))/2
        if int(round(T1)) > int(round(T2)):
            return 1
        elif int(round(T1)) < int(round(T2)):
            return -1
        else: return 0
        
    def gamesSim(self,number_simulations):
        gamesout = []
        team1win = 0
        team2win = 0
        tie = 0
        for i in range(number_simulations):
            #calls the pervious game simulator and aggregates results
            gm = self.gameSim()
            gamesout.append(gm)
            if gm == 1:
                team1win +=1 
            elif gm == -1:
                team2win +=1
            else: tie +=1 
        print(self.Team1.TeamName + ' Win ', team1win/(team1win+team2win+tie),'%')
        print(self.Team2.TeamName + ' Win ', team2win/(team1win+team2win+tie),'%')
        print('Tie ', tie/(team1win+team2win+tie), '%')
        print('Number of Simulations: ',number_simulations)
        #can see all results using self.results
        self.results = gamesout
