from math import factorial as fac

def out_of(n, r):
	return fac(n) / (fac(n-r) * fac(r))

class DiceAnalyzer():

	def prob(self, initial=0, left=4):
		free = 5 - initial
		result = 0
		# the first option is to hit all now in this throw
		result += (1./6 ** free)
		# if this is the first dice, then actually you will always hit
		if initial == 0:
			result *= 6
		# if no more options are left, than that's it
		if left == 0:
			return result
		# there is still hope == throws left
		if free > 4:
			# if we have all dices free, we can have 4 matches now and still go on
			result += (1./6 ** 4) * (5./6 ** 1) * 5 * self.prob(initial + 4, left - 1)
		if free > 3:
			# with 4 dices, we can draw three now and go on
			result += (1./6 ** 3) * (5./6 ** (free-3)) * out_of(free, 3) * self.prob(initial + 3, left - 1)
		if free > 2:
			# two matches possible with 3 dices
			result += (1./6 ** 2) * (5./6 ** (free-2)) * out_of(free, 2) * self.prob(initial + 2, left - 1)
		if free > 1:  	
			# we can have one match
			result += 1./6 * (5./6 ** (free-1)) * free * self.prob(initial + 1, left - 1)
		# any given sunday, we can have no luck
		result += 5./6 ** free * self.prob(initial, left - 1)
		return result

if __name__ == "__main__":
	da = DiceAnalyzer()
	print da.prob()