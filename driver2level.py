import fasttext
query = []

model_1 = fasttext.load_model('model_1.bin', label_prefix='__label__')

print ('Testing the model')
result = model_1.test('TestData.txt')
print 'P@1: ', result.precision
print 'R@1: ', result.recall
print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
print 'Accuracy: ', score

print '******************************************************************'
model_2 = fasttext.load_model('model_2.bin', label_prefix='__label__')

print ('Testing the model')
result = model_2.test('TestData2.0.txt')
print 'P@1: ', result.precision
print 'R@1: ', result.recall
print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
print 'Accuracy: ', score

while True: 
	query.append(raw_input('What is your query?\n'))
	if query == 'exit':
		break

	label_1 = model_1.predict_proba(query)
	label_2 = model_2.predict_proba(query)
	
	##if (labels[0][0][1] <= 0.60):
	#	query.pop(0)
	#	query.append(raw_input('Hmm, I do not fully understand. Can you clarify the question please.\n'))
	#	if query[0] == 'exit':
	#		break

	#label_1 = model_1.predict_proba(query)
	#label_2 = model_2.predict_proba(query)	
	  
	print label_1
	print label_2
	query.pop(0)

print("Goodbye!")
