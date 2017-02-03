name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_in_cm = height * 2.54
weight_in_kg = weight * 0.45

print "Let's talk about %s." % name
print "He's %d inches tall or %d centimeters tall." % (height, height_in_cm)
print "He weighs %d pounds and %d kilograms." % (weight, weight_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)