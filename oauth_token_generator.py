import os
import hashlib

def generatePBKDF2():
	hashType = "sha256"
	passw = ""
	salt = ""
	hasSalt = ""
	hashType = ""
	iterations = 0
	passw = input("Enter your password")
	hasSalt = input("Do you have a salt? Enter 'yes' or 'no'.")
	if hasSalt == 'yes':
		salt = input("Enter your salt.")
	elif hasSalt == 'no':
		salt = os.urandom(16)
	else:
		print("You entered an invalid option. Try again.");
		generatePBKDF2()
	hashType = input("What is your preferred hash type? Press enter to use the default type. Possible hash types are printed below.")
	printHashTypes()
	try:
		iterations = int(input("Enter the number of iterations"))
	except ValueError as valueErr:
		print("Incorrect iteration. Restarting.")
		generatePBKDF2()
	except Exception as ex:
		printf("Generalized error " + ex + ". Restarting.")
		generatePBKDF2()
	
	if(hashType == 	 
