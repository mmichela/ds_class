class Dog:

	def __init__(self, name, age):
		self.name = name
		self._age = age

	def bark(self):
		print("bark bark!")

	def doginfo(self):
		print(self.name + " is " + str(self.age) + " year(s) old.")

	def birthday(self):
		self.age +=1

	def setBuddy(self, buddy):
		self.buddy = buddy
		buddy.buddy = self

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		if value < 0:
			raise ValueError("Age cannot be negative")
		self._age = value

# A child class of Dog (inheriths from Dog class)
class BullDog(Dog):

	def __init__(self, name, age, speed):
		Dog.__init__(self, name, age)
		self.speed = speed

	def run(self):
		return "{} runs at {} mph".format(self.name, self.speed)

# Another child class of Dog (inheriths from Dog class)
class RusselTerrier(Dog):

	def run(self, speed):
		return "{} runs {}".format(self.name, speed)
	