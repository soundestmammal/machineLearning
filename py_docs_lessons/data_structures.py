# Looping Technique: When looping through dictionaries the key and corresponding value can be retruiedved at the same time using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

# gallahad the pure
#robin the brave.