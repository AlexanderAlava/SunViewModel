# Timed driver #

import fasttext
import time

query = []

model = fasttext.load_model('model.bin', label_prefix='__label__')

print ('Testing the model')
result = model.test('TestData.txt')
print 'P@1: ', result.precision
print 'R@1: ', result.recall
print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
print 'Accuracy: ', score

while True:
	query.append(raw_input('What is your query? Type "exit" to quit\n'))
	start = time.time()
	if query[0].lower() == 'exit':
		break
	labels = model.predict_proba(query, k = 3)
	print labels
	query.pop()
	end = time.time()
	print "Performed in ", end - start, "s"

print("Goodbye!")
