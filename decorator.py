def bread(fn):
	def wrapper():
		print '======'
		fn()
		print "======"
	return wrapper

def veg(fn):
	def wrapper():
		print "</''\>"
		fn()
		print "<\../>"
	return wrapper

@bread
@veg
def ham():
	print '~~~~~'

ham()