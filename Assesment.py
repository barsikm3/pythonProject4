def format_address(address_string):
  # Declare variables
  number = ''
  street = ''
  # Separate the address string into parts
  address_string = address_string.split()
  # Traverse through the address parts
  for add in address_string:
      # Determine if the address part is the
      # house number or part of the street name
      if add.isdigit():
          number += add
      # Does anything else need to be done
      # before returning the result?
      else :
          street += " " + add
      # Return the formatted string
      return "house number {} on street named {}".format(number, street)
# Does anything else need to be done
# before returning the result?

# Return the formatted string

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

def Minsk_adress(adress_names):
    adr = ""
    num = ""
    adress_names = adress_names.split()
    for number in adress_names:
        if number.isdigit():
            num += number
    else:
        adr += "" + number

    return "The {} street {}".format(adr,num)

print(Minsk_adress("10 Russianiva"))

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    list3 = list2
    # Followed by the elements of list1 in reverse order
    for elements in reversed(range(len(list1))):
        list3.append(list1[elements])

    return list3


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

def squares(start, end):
    return [x*x for x in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def car_listing(car_prices):
  result = ""
  for keys, values in car_prices.items():
        result += "{} costs {} dollars".format(keys, values) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

def combine_guests(guests1, guests2):
    guests2.update(guests1)
    return guests2
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter .isalpha() and letter not in result:
        result[letter] = text.lower().count(letter)
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}