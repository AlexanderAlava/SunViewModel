# Driver without FastText #

# import fasttext
import time
from random import *

# "Switch case" for buckets
def bucketSelectorNonTech(bucket):
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
