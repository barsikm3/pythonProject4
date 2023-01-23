def build_string(*args):
  return "I like {}!".format(args)

print(build_string('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!', 'Return the correct String')
print(build_string('Cheese','Milk'), 'I like Cheese, Milk!', 'Return the correct String')


def solution(string):
  return string[::-1]
print(solution("El gringo "))

print(dir())
help(__spec__)