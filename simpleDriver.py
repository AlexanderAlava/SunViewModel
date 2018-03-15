# Driver without FastText #

# import fasttext
import time
from random import *

# "Switch case" for buckets
def bucketSelectorNonTech(bucket):
	if (bucket == "greetings"):
		# Print option(s) for greetings
		print("greetings")
	elif (bucket == "holidays"):
		# Print option(s) for holidays
		print("holidays")
	elif (bucket == "sunview"):
		# Print option(s) for sunview
		print("sunview")
	elif (bucket == "announcements"):
		# Print option(s) for announcements
		print("announcements")
	elif (bucket == "support"):
		# Print option(s) for support
		print("support")
	elif (bucket == "name"):
		# Print option(s) for name
		print("name")
	elif (bucket == "human"):
		# Print option(s) for human
		print("human")
	elif (bucket == "bot"):
		# Print option(s) for bot
		print("bot")
	elif (bucket == "itsm"):
		itsmA = "a"
		itsmB = "b"

		itsmMessages = [itsmA, itsmB]
		itsmResponse = sample(itsmMessages, 1)

		print(itsmResponse[0])

	elif (bucket == "halloween"):
		halloweenA = "Spooky!\nLast year I dressed up as human for Halloween, I had a great time but people looked at me like a freak when I talked to anyone. Maybe I was a little bit too robotic?"
		halloweenB = "Good friends share their Halloween candy!\nThankfully, I am not a good friend and kept all the candy for myself last year. I remember I dressed as a . . . . chatbot?"

		halloweenMessages = [halloweenA, halloweenB]
		halloweenResponse = sample(halloweenMessages, 1)

		print(halloweenResponse[0])
		print("If you wish to know more about Halloween related vacations, please visit the FAQ page for company holidays.")

	elif (bucket == "changegear"):
		changegearA = "ChangeGear? Mmmmmm, why does that sound so familiar to me?\nOh! That's right! I am part of it!"
		changegearB = "Great that you ask me!\nChangeGear and I have been great friends since my creation. We work together, we live together, we do everyhting together!"

		changegearMessages = [changegearA, changegearB]
		changegearResponse = sample(changegearMessages, 1)

		print(changegearResponse[0])
		print("ChangeGear products, developed by SunView Software, deliver intelligent, people-centric IT service management with critical enterprise-grade features you need to ensure that your solution is able to meet your current and future business requirements.\nIf you would like more information about the different available products, please refer to SunView's Software website at https://www.sunviewsoftware.com/products")

	elif (bucket == "sst"):
		sstA = "a"
		sstB = "b"

		sstMessages = [sstA, sstB]
		sstResponse = sample(sstMessages, 1)

		print(sstResponse[0])


################################# MAIN #########################################

query = []
confidence = 0.7
flag = 0

#model = fasttext.load_model('model.bin', label_prefix='__label__')

#print ('Testing the model')
#result = model.test('TestData.txt')
#print 'P@1: ', result.precision
#print 'R@1: ', result.recall
#print 'Number of examples: ', result.nexamples

#score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
#print 'Accuracy: ', score

while True:
	query.append(raw_input('What is your query? Type "exit" to quit\n'))
	start = time.time()
	if query[0].lower() == 'exit':
		break
	#labels = model.predict_proba(query, k = 3)
	#print labels

	# Confidence level is less than 0.6
	if confidence < 0.6:
		# Confidence level is less than 0.2 or second try with low confidence
		if confidence < 0.2 or flag > 0:
			errorA = 'I am sorry, but I am not able to understand what you are trying to tell me.\nPlease refer to the general FAQ page.'
			errorB = 'People still believe that us machines are smarter than humans, what a joke! I am sorry for not being able to help you at this time.\nPlease proceed to the general FAQ page.'
			errorC = 'I don\'t want you to think that I am dumb, but I can\'t really understand your query. I am sorry!\nPlease refer to the general FAQ page.'

			errorMessages = [errorA, errorB, errorC]

			error = sample(errorMessages, 1)
			print(error[0])

			# Resetting flag
			flag = 0

			print ("Con < 0.2") # Print error message
		# First try with low confidence
		else:
			# Ask for clarification or for a different query
			# Setting flag
			flag += 1

	# Confidence level is greater than 0.6
	else:
		keyword = query[0] # This should be the first label
		print("Con > 0.6")
		bucketSelectorNonTech(query[0]) # "Switch case" for buckets

		# Resetting flag
		flag = 0

	query.pop()
	end = time.time()
	print "Performed in ", end - start, "s"

print("Goodbye!")
