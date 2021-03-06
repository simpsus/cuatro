from math import factorial as fac

def out_of(n, r):
	return fac(n) / (fac(n-r) * fac(r))

class DiceAnalyzer():

	def yathzee(self, initial=0, left=4):
		free = 5 - initial
		result = 0
		# the first option is to hit all now in this throw
		result += ((1./6) ** free)
		# if this is the first dice, then actually you will always hit
		if initial == 0:
			result *= 6
		# if no more options are left, than that's it
		if left == 0:
			return result
		# there is still hope == throws 
		# eaxmine what can happen in this throw and branch
		if free > 4:
			# if we have all dices free, we can have 4 matches now and still go on
			result += ((1./6) ** 4) * ((5./6) ** 1) * 5 * self.yathzee(initial + 4, left - 1)
		if free > 3:
			# with 4 dices, we can draw three now and go on
			result += ((1./6) ** 3) * ((5./6) ** (free-3)) * out_of(free, 3) * self.yathzee(initial + 3, left - 1)
		if free > 2:
			# two matches possible with 3 dices
			result += ((1./6) ** 2) * ((5./6) ** (free-2)) * out_of(free, 2) * self.yathzee(initial + 2, left - 1)
		if free > 1:  	
			#if free < 5:
				# there already is a chosen face
			# we can have one match
			result += 1./6 * ((5./6) ** (free-1)) * free * self.yathzee(initial + 1, left - 1)
		# any given sunday, we can have no luck
		result += ((5./6) ** free) * self.yathzee(initial, left - 1)
		return result

	def single_roll(self, target):
		if target == "yathzee":
			return 6 * (1./6) ** 5
		if target == "four of a kind":
			return 6 * 5 * (1./6) ** 4 * 5./6
		if target == "three of a kind":
			return 6 * out_of(5,3) * (1./6) ** 3 * (5./6) ** 2
		if target == "pair":
			# a true pair, so no full house
			return 6 * out_of(5,2) * (1./6) ** 2 * (5./6) ** 2 * 4./6
		if target == "no match":
			return fac(6) * 1. / (6 ** 5)

	def y(self, roles=0):
		single_roll = self.single_roll("yathzee")
		if roles == 1:
			return single_roll
		# now with two rolls
		# four of a kind with a single 
		four_single = self.single_roll("four of a kind") * (1./6)
		# three of a kind and then two matching
		three_two = self.single_roll("three of a kind") * (1./6) ** 2
		# a pair and then three that match
		pair_three = self.single_roll("pair") * (1./6) ** 3
		# no match and then matching four
		no_four = self.single_roll("no match") * (1./6) ** 4
		two_roll = four_single
		two_roll += three_two
		two_roll += no_four
		two_roll += pair_three
		if roles == 2:
			return two_roll
		return single_roll + two_roll

	

	def full_house(self, dice):
		pass
		

def is_yathzee(dice):
	face = dice.faces[0]
	for f in dice.faces:
		if f != face:
			return False
	return True

import dice

def simulate_yathzee():
	attempts = 0
	probability = 0
	prev_probability = 0
	hits = 0
	stepsize = 1000000
	error = 1
	while error > 1.0 / 100000:
		for attempt in range(stepsize):
			attempts += 1
			yathzee = False
			d = dice.Dice()
			face = 0
			keep= []
			for throw in range(5):
				d.roll(keep)
				if face == 0:
					face = d.max_face
				else:
					keep = [face for i in range(d.max_count)]
				if is_yathzee(d):
					yathzee = True
					break
			if yathzee:
				hits += 1
		prev_probability = probability
		probability = hits * 1.0 / attempts
		error = abs(probability - prev_probability)
		print "Finished ", attempts, " attempts. Hits: ", hits, ". Probability of ", (hits * 1.0 /attempts), " Error ", error
	print "Result ", probability, " with ", attempts, " attempts"



if __name__ == "__main__":
	da = DiceAnalyzer()
	print da.single_roll("yathzee")
	print da.y()
	#print da.yathzee(0,0)
	#simulate_yathzee()