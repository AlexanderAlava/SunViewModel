import fasttext
query = []

model = fasttext.load_model('modelMaster.bin', label_prefix='__label__')

print ('Testing the model')
result = model.test('TestData.txt')
print 'P@1: ', result.precision
print 'R@1: ', result.recall
print 'Number of examples: ', result.nexamples

score = 2 * ((result.precision * result.recall) / (result.precision + result.recall))
print 'Accuracy: ', score

while True: 
	query.append(raw_input('What is your query?\n'))
	if query == 'exit':
		break

	labels = model.predict_proba(query)
	
	if (labels[0][0][1] <= 0.60):
		query.pop(0)
		query.append(raw_input('Hmm, I do not fully understand. Can you clarify the question please.\n'))
		if query[0] == 'exit':
			break

	labels = model.predict_proba(query)	  
	print labels
	query.pop(0)

print("Goodbye!")
