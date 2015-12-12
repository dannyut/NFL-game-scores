# built using python 2.7.11
# this took me 38.2s to finish
import nflgame

f = open('games_data','w')
msg = 'week, away, home, score_away, score_home\n'
#print(msg)
f.write(msg)
for i in range (1,15):
	games = nflgame.games(2015, week=i)
	for g in games:
		msg = '%d, %s, %s, %d, %d \n' % (i,g.away,g.home,g.score_away,g.score_home)
		#print msg
		f.write(msg)
