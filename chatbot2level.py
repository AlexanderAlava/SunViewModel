import fasttext

model_1 = fasttext.supervised('LabelsMaster.txt', 'model_1', label_prefix='__label__', lr = 1.0, epoch = 50)
model_2 = fasttext.supervised('LabelsMaster2.0.txt', 'model_2', label_prefix='__label__', lr = 1.0, epoch = 50)
