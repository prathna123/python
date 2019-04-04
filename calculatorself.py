class Calculator():
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b
x=Calculator().add(2,3)
print(x)
y=Calculator().sub(5,4)
print(y)
z=Calculator().mul(11,5)
print(z)
p=Calculator().div(22,2)
print(p)
