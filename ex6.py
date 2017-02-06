#inserting the digit inline
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

#printing the two lines
print x
print y

#repeating the code above
#use %r for debugging because it displays the "raw" data of the variable
print "I said: %r." % x
print "I also said: '%s'." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#setting two strings to letters
w = "This is the left side of..."
e = "a string with a right side."

#concatenating the two strings together
print w + e