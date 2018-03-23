import fasttext
import time
from random import *

# "Switch case" for buckets
def bucketSelector(bucket):
	if (bucket == "greetings"):

		greetingsA = 'Well hello there! How can I be of help today?'
		greetingsB = 'Hello from the other siiiiiide, and by other side I mean this side of the window haha'
		greetingsC = 'Hi there, how are you doing this lovely day?'

		greetingsMessages = [greetingsA, greetingsB, greetingsC]

		greetingsResponse = sample(greetingsMessages, 1)
		print(greetingsResponse[0])

	elif (bucket == "holidays"):

		holidaysA = 'Hmmm, this website may be useful: https://www.opm.gov/policy-data-oversight/pay-leave/pay-administration/fact-sheets/holidays-work-schedules-and-pay!'
		holidaysB = 'Shouldn\'t you get back to work?'
		holidaysC = 'Vacation? If I can\'t have days off then you shouldn\'t either!'

		holidaysMessages = [holidaysA, holidaysB, holidaysC]

		holidaysResponse = sample(holidaysMessages, 1)
		print(holidaysResponse[0])
		print("If you wish to know more about SunView's vacation days, please visit the FAQ page for company holidays.")

	elif (bucket == "sunview"):

		sunviewA = 'This website has all of SunView Software\'s contact information: https://www.sunviewsoftware.com/contact-us'
		sunviewB = 'SunView Software is a leading provider of IT Service Management software that helps companies build smarter, ' + \
					'more responsive IT services environments. See more at https://www.sunviewsoftware.com/'
		sunviewC = 'SunView Software? That\'s where I work at! I mean... work from? I don\'t know, this artificial intelligence thing is weird even to me.'

		sunviewMessages = [sunviewA, sunviewB, sunviewC]

		sunviewResponse = sample(sunviewMessages, 1)
		print(sunviewResponse[0])

	elif (bucket == "announcements"):

		announcementsA = 'You know, I get all my news from Twitter! Follow SunView @SunviewSoftware!'
		announcementsB = 'If you want to get relevant and informative blog content about the modern Service Desk, ITIL, Change Management, DevOps and more go to Sunview\'s blog here: https://www.sunviewsoftware.com/blog'

		announcementsMessages = [announcementsA, announcementsB]

		announcementsResponse = sample(announcementsMessages, 1)
		print(announcementsResponse[0])

	elif (bucket == "support"):

		supportA = 'The SunView Support Advantage Program is for customers who have purchased the Enterprise versions of our ChangeGear software. Email us at support@sunviewsoftware.com'
		supportB = 'You can learn about Sunview\'s support services here: https://www.sunviewsoftware.com/learn/services'

		supportMessages = [supportA, supportB]

		supportResponse = sample(supportMessages, 1)
		print(supportResponse[0])

	elif (bucket == "name"):

		nameA = 'The name is Bot, Chat Bot.'
		nameB = 'I am Sunview\'s interactive Chatbot! You can call me Chat for short.'
		nameC = '"A rose by any other name would smell as sweet" - William Shakespeare'

		nameMessages = [nameA, nameB, nameC]

		nameResponse = sample(nameMessages, 1)
		print(nameResponse[0])

	elif (bucket == "human"):

		humanA = 'Are we human? Or are we dancer?'
		humanB = 'Errrm... yeah sure, of course... hahaha I\'m human alright. Look at me speaking hahaha. Nothing strange here...'
		humanC = 'Do you just go around asking people if they are human? Psst, that\'s pretty rude in my opinion.'

		humanMessages = [humanA, humanB, humanC]

		humanResponse = sample(humanMessages, 1)
		print(humanResponse[0])

	elif (bucket == "bot"):

		botA = 'I can provide you with information on several different topics such as tech support and (almost) any other kind of assistance. Go ahead! Ask me!'
		botB = 'Try asking me something and you will find out :)'
		botC = 'I will try to solve your technical concerns to the best of my abilities! Or at least point you in the right direction.'

		botMessages = [botA, botB, botC]

		botResponse = sample(botMessages, 1)
		print(botResponse[0])

	elif (bucket == "itsm"):

		itsmA = 'When you say ITSM I think ChangeGear, OBVIOUSLY. You do not need to be artificially intelligent to know that it is the best.'
		itsmB = 'According to my BFF Wikipedia, IT Service Management "refers to the entirety of activities performed by an organization to design, plan, deliver, operate and control information technology services offered to customers."'

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
		sstA = "Smart Service Technology, developed by Sunview Software, is used to leverage big data and machine learning to deliver intelligent features for ITSM."
		sstB = "Smart? Sounds like me. Service? Sound like what I do. Technology? Sounds like where I belong."

		sstMessages = [sstA, sstB]

		sstResponse = sample(sstMessages, 1)
		print(sstResponse[0])
		print("If you would like to learn more about SST, please visit https://www.sunviewsoftware.com/solutions/machine-learning-for-itsm and make sure to watch the video linked in there!")

	else:
		print "Here is a FAQ page for help with " + bucket


################################# MAIN #########################################

# Declaring global variables
query = []
flag = 0
failed = 0

########################## TESTNG INFORMATION ##################################
model_1 = fasttext.load_model('model_1.bin', label_prefix='__label__')

#print ('Testing the model: Bucket Classification')
result = model_1.test('TestData.txt')
#print 'P@1: ', result.precision
#print 'R@1: ', result.recall
#print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
#print 'Accuracy: ', score

model_2 = fasttext.load_model('model_2.bin', label_prefix='__label__')

#print ('Testing the model: Technical/Non-Technical')
result = model_2.test('TestData2.0.txt')
#print 'P@1: ', result.precision
#print 'R@1: ', result.recall
#print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
#print 'Accuracy: ', score

################################### BODY ######################################

# Printing greeting message
print '\nHello there! Welcome to the SunView chatbot! What can I help you with? \nType "exit" to quit\n'

# Establishing general while loop
while failed != 1:

	# Prompting for and reading in user query
	rawQuery = raw_input('>')

	# Checking if the query is too short
	if (len(rawQuery) < 2):
		print 'Your query is too short, I need a bit more to work with!\n'
		continue;

	# Appending the query all in lowercase
	query.append(rawQuery.lower())

	# Computation time start
	start = time.time()

	# Checking if the user wants to exit
	if query[0].lower() == 'exit':
		break

	# Extracting information from the models
	label_1 = model_1.predict_proba(query)
	label_2 = model_2.predict_proba(query)

	# Assigning retrieved labels and confidence levels to local variables
	bucket_1 = label_1[0][0][0]
	confidence_1 = label_1[0][0][1]
	bucket_2 = label_2[0][0][0]
	confidence_2 = label_2[0][0][1]

	# Printing results
	print '\nBucket Prediction: ',bucket_1
	print 'Confidence Level: ',confidence_1
	print '\n'
	print 'Technical Prediction: ',bucket_2
	print 'Confidence Level: ',confidence_2

	# Confidence is less than 0.6
	if confidence_1 < 0.6 or confidence_2 < 0.6:
		# Confidence level less than 0.2 or second try with low confidence
		if confidence_1 < 0.2 or confidence_2 < 0.2 or flag > 0:
			errorA = 'I am sorry, but I am not able to understand what you are trying to tell me.\nPlease refer to the general FAQ page.'
			errorB = 'People still believe that us machines are smarter than humans, what a joke! I am sorry for not being able to help you at this time.\nPlease proceed to the general FAQ page.'
			errorC = 'I don\'t want you to think that I am dumb, but I can\'t really understand your query. I am sorry!\nPlease refer to the general FAQ page.'

			errorMessages = [errorA, errorB, errorC]

			error = sample(errorMessages, 1)
			print error[0], '\n'

			# Computation time end and print
			end = time.time()
			print "Performed in ", end - start, "s"

			# Resetting flag
			flag = 0

			# Setting failed in order to exit
			failed = 1

		# First try with low confidence
		else:
			errorA = 'I am having a little trouble understanding what you are trying to ask, can you please clarify? \n'
			errorB = "What do you mean? I am only a machince, help me out here! What is it that you're asking?\n"
			errorC = 'Hmm I think I may have the answer, can you give me a little bit more info? \n'

			errorMessages = [errorA, errorB, errorC]

			error = sample(errorMessages, 1)
			print error[0], '\n'

			# Setting flag
			flag += 1

	# Confidence level greater than 0.6
	else:
		# Highest confidence label
		keyword = bucket_1

		# Calling function with switch case for buckets
		bucketSelector(keyword)

		# Resetting flag
		flag = 0

	# Clearing the query list
	query.pop()

	# Computation time end
	end = time.time()
	print "Performed in ", end - start, "s"

print("Goodbye!")
