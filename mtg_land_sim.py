import random
import copy

runs = 50000
def draw(n):
	for x in range(0,n):
		draw_key=random.randint(0,len(deck)-1)
		hand.append(deck.pop(draw_key))


#------------------construct a deck ---------------------#
lands = 23
dorks = 8
spells = 60-dorks-lands

deck_list =[]
deck_list.append(lands*['land'])
deck_list.append(dorks*['dork'])
deck_list.append(spells*['spell'])
flatten = lambda deck_list: [item for sublist in deck_list for item in sublist]
deck_list = flatten(deck_list)

successes = 0

for i in range(0,runs):
	deck = copy.deepcopy(deck_list)
	hand =[]

	#------------------initial draws and mulligans ---------------------#
	draw(7)
	mull_no=0
	while mull_no <3:   #Only lets you draw a new hand a maximum of 2 times

		#mulligan conditions:
		#with 7: To keep, need at least 2 spells, and at least 2 mana sources.
		#with 6: Same as 7
		#with 5: To keep, need at least 1 land, at least 1 spell.

		if mull_no == 0:
			mull_criteria = hand.count('land')<= 1 and hand.count('land')+hand.count('dork')<=2 and hand.count('spell') < 2
		elif mull_no == 1:
			mull_criteria = (hand.count('land') <= 1 or hand.count('land')>= 6) and hand.count('spell') >= 1
		elif mull_no == 2:
			mull_criteria = hand.count('land')== 0 and hand.count('spell') < 1

		if mull_criteria:
			mull_no=mull_no+1
			deck = copy.deepcopy(deck_list)
			hand =[]
			draw(7-mull_no)
		else:
			break
	if mull_no>=3:    #If you did mull three times, e.g to 4, concede
		continue

	#---------------checking consistency of mana-------------------#

	draw(2) #T3 on the play
	success_condition = hand.count('land')+hand[:len(hand)-1].count('dork')>=3
	#4 mana sources by T3 including dorks. A dork doesn't count as a source if you drew it on T3 i.e your 2nd draw

	if success_condition:
		successes = successes+1
print(successes/runs)





