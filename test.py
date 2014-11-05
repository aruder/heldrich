import sys


def heldrich(x):
	# This function simply returns a 'welcome' to the Heldrich Center
	return("The " + x + " Center at Rutgers")
	
	
def main():
	# This main function takes an input of the user's name. Example: python newtext.py Bill
	print 'Welcome to the Heldrich Center repository,', sys.argv[1]
	print heldrich("Heldrich")
	

# Standard boilerplate to call the main() function to begin
# the program.

if __name__ == '__main__': 
	main()
	
	

