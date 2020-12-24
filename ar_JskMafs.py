import math
from fractions import Fraction


globals()["\x5f\x5f\x6e\x61\x6d\x65\x5f\x5f"] = "\x4a\x73\x6b\x4d\x61\x66\x73\x2e\x70\x79"
__description__ = "Jsk Troll's Python toolkit for easy maths ;) "
if not __name__ in __file__:
	rename(__file__, __name__)
	message = "Try again."
	raise Exception(message)
def sign(n):
	req = [int, float, str]
	if type(n) not in req:
		raise TypeError("{} type not allowed.".format(type(n)))
	n=float(n)
	if n>=0:
		n_sign='+'
	else:
		n_sign='-'
	return n_sign
def signed(n):
	req = [float, int, str]
	if type(n) not in req:
		raise TypeError("{} type not allowed.".format(type(n)))
	if isint(n):
		unsigned_n = int(abs(float(n)))
	else:
		unsigned_n = abs(float(n))
	signed_n = "{} {}".format(sign(n), unsigned_n)		#sign(n), str(abs(n))
	return signed_n
def isint(n):
	req = [int, float, str, Fraction]
	if type(n) not in req:
		raise TypeError("{} type not allowed.".format(type(n)))
	if float(n)>=0:
		result = math.ceil(float(n)) == int(n)
	else:
		result = math.floor(float(n)) == int(n)
	return result
def intify(n):
	req = [int, float, str, Fraction]
	if type(n) not in req:
		raise TypeError("{} type not allowed.".format(type(n)))
	n = float(n)
	if isint(n):
		return int(n)
	return n
def ikhtizal(bast, maqam, form="default"):
	req = [int, float, str, Fraction, "default"]
	for n in [bast, maqam, form]:
		if type(n) not in req:
			raise TypeError("{} type not allowed.".format(type(n)))
	l7asil = bast / maqam
	bast = int(bast)
	maqam = int(maqam)
	pgcd = math.gcd(bast, maqam)
	bast = int(bast / pgcd)
	maqam = int(maqam / pgcd)
	if form=="default":
		result = Fraction(bast, maqam)
		result = intify(result)
	elif form==str:
		result = str(Fraction(bast, maqam))
	elif form==float:
		result = float(Fraction(bast, maqam))
	elif form==int:
		result = int(Fraction(bast, maqam))
	elif form==Fraction:
		result = Fraction(bast, maqam)
	return result
def solve1():
	print("حل معادلة من الدرجة الأولى من الشكل ax=b")
	# passing variables
	a = input("a = ")
	b = input("b = ")
	# equation form
	equation = f"{a}x = {b}"
	print("\n" + equation)
	# solving
	print(f'x = {b}/{a}\n')

	x = ikhtizal(float(b), float(a))
	print(f"حل المعادلة {equation} هو :")
	print(f"x = ", end="")
	return x
def solve2():
	print("حل معادلة من الدرجة الثانية من الشكل ax²+bx+c=0")
	
	# passing variables
	a = input("a = ")
	if float(a) == 0:
		raise ValueError("a≠0")
	b = input("b = ")
	c = input("c = ")
	
	# equation form
	equation = f"{a}x² {signed(b)}x {signed(c)} = 0"
	print("\n" + equation)
	
	# converting
	a = intify(a)
	b = intify(b)
	if b>=0:
		dB = b
	else:
		dB = "({0})".format(b)
	c = intify(c)
	
	# solving
	print("\tحساب المميز ∆ : ")
	print("∆ = b² - 4ac\n")
	print(f"∆ = {b}² - 4({a})({c})")
	print(f"∆ = {b**2} {signed((-4) * a * c)}")
	delta = (b**2) - (4*a*c)
	delta = intify(delta)
	print(f"∆ = {delta}")
	if delta>0: # 										2 different solutions
		print(f"بما أن 0<∆ فإن المعادلة {equation} تقبل حلين مختلفين وهما : \n")
		rootDelta = intify(math.sqrt(delta))
		lbast1 = intify(-b-rootDelta)
		lbast2 = intify(-b+rootDelta)
		x = ( ikhtizal(lbast1, 2*a), ikhtizal(lbast2, 2*a) )	#double "()" to make it a tuple array
		print(f"x1 = (-b-√∆)/2a = -{dB}-√{delta}/2({a}) = {-b}-{rootDelta}/{2*a} = {lbast1}/{2*a} = {x[0]}")
		print(f"x2 = (-b+√∆)/2a = -{dB}+√{delta}/2({a}) = {-b}+{rootDelta}/{2*a} = {lbast2}/{2*a} = {x[1]}\n")
		print("S = ", end="")
		return x
		
	elif delta==0: # 										2 doubled solutions
		print(f"بما أن 0=∆ فإن المعادلة {equation} تقبل حل مضاعف وهو : \n")
		x = ikhtizal(-b, 2*a)
		print(f"x1 = x2 = -b/2a = -{dB}/2({a}) = {-b}/{2*a} = {x}")
		print("x1 = x2 = ", end="")
		return x
		
	else: # 													No solutions
		print(f"بما أن 0>∆ فإن المعادلة {equation} لا تقبل حلول .\n")
		print("S = ", end="")
		return None

def solve3():
	pass

def solve():
	passage = "حل معادلة من الدرجة : (1-3) \n"
	degree = input(passage)
	if degree == '1':
		print(solve1())
	elif degree == '2':
		print(solve2())
	elif degree == '3':
		print("unfinished project")
		return None
		print(solve3())
if __name__=="__main__":
	solve()


# usage : simply click on this file to run it or import it to your script
