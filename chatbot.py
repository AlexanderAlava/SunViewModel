import fasttext

model = fasttext.supervised('LabelsMaster.txt', 'model', label_prefix='__label__', lr = 1.0, epoch = 50)
