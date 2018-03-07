# Driver without FastText #

# import fasttext
import time
import random

query = []
confidence = 0.6
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


	if confidence < 0.6:
		if confidence < 0.2:
			print ("Con < 0.2") # Print error message
		# elif flag = 0
			# Ask for clarification or for a different query
			# flag++;
		# elif
		 	# Print error message

	else:
		keyword = query[0] # This should be the first label
		print("Con > 0.6")# Switch case for buckets
		# flag = 0
	query.pop()
	end = time.time()
	print "Performed in ", end - start, "s"

print("Goodbye!")
