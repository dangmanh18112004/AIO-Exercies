from abc import ABC, abstractmethod

class Ward:
	def __init__(self, name) -> None:
		self.__name = name
		self.__listMember = []

	def add_person(self, person):
		self.__listMember.append(person)

	def count_doctor(self):
		count = 0
		for p in self.__listMember:
			if isinstance(p, Doctor):
				count += 1
		return count

	def describe(self):
		print(f"Ward Name: {self.__name}")
		for p in self.__listMember:
			p.describe()

	def sort_age(self):
		self.__listMember.sort(key=lambda p: p.get_yob(), reverse=True)

	def compute_average(self):
		total_yob = 0
		number_of_teachers = 0
		for p in self.__listMember:
			if isinstance(p, Teacher):
				number_of_teachers += 1
				total_yob += p.get_yob()
		return total_yob / number_of_teachers
	
class Person(ABC):
	def __init__(self, name, yob) -> None:
		self._name = name
		self._yob = yob

	def get_name(self):
		return self._name
	
	def get_yob(self):
		return self._yob
	
	@abstractmethod
	def describe(self):
		return f"Name: {self._name} - YoB: {self._yob}"
	
class Student(Person):
	def __init__(self, name, yob, grade) -> None:
		self.__grade = grade
		super().__init__(name, yob)

	def describe(self):
		print(f"Student - {super().describe()} - Grade: {self.__grade}")

class Doctor(Person):
	def __init__(self, name, yob, specialist) -> None:
		self.__specialist = specialist
		super().__init__(name, yob)

	def describe(self):
		print(f"Doctor - {super().describe()} - Grade: {self.__specialist}")

class Teacher(Person):
	def __init__(self, name, yob, subject) -> None:
		self.__subject = subject
		super().__init__(name, yob)

	def describe(self):
		print(f"Teacher - {super().describe()} - Subject: {self.__subject}")

if __name__ == '__main__':
	# 2a)
	student1 = Student(name="studentA", yob=2010, grade="7")
	student1.describe()

	teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
	teacher1.describe()

	doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
	doctor1.describe()

	# 2b)
	print()
	teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
	doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
	ward1 = Ward(name="Ward1")
	ward1.add_person(student1)
	ward1.add_person(teacher1)
	ward1.add_person(teacher2)
	ward1.add_person(doctor1)
	ward1.add_person(doctor2)
	ward1.describe()

	# 2c)
	print(f"\nNumber of doctors: {ward1.count_doctor()}")

	# 2d)
	print(f"\nAfter sorting Age of Ward1 people")
	ward1.sort_age()
	ward1.describe()

	# 2e)
	print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")




