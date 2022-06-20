import unittest

def lwsum(a,b):
    i=a+b
    return i 

def lwsub(c,d):
    j=c-d
    return j

class mycl(unittest.TestCase):
	def test_n(self):
		self.assertEqual(lwsum(4,5) , 9 , msg="If fail please give error")
	def test_n2(self):
		self.assertEqual(lwsub(14,5) , 9 , msg="If fail please give error")
newobj= mycl()

newobj.test_n()
newobj.test_n2()