from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.collocations import *

def doNaiveBayesSentiment():
	n_instances = 100
	subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
	obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

	train_subj_docs = subj_docs[:80]
	test_subj_docs = subj_docs[80:100]
	train_obj_docs = obj_docs[:80]
	test_obj_docs = obj_docs[80:100]
	training_docs = train_subj_docs+train_obj_docs
	testing_docs = test_subj_docs+test_obj_docs
	sentim_analyzer = SentimentAnalyzer()
	all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

	unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
	sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

	training_set = sentim_analyzer.apply_features(training_docs)
	test_set = sentim_analyzer.apply_features(testing_docs)

	trainer = NaiveBayesClassifier.train
	classifier = sentim_analyzer.train(trainer, training_set)
	for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	    print ('{0}: {1}'.format(key, value))
 
def word_feats(words):
    return dict([(word, True) for word in words])

def doNaiveBayes():
	negids = movie_reviews.fileids('neg')
	posids = movie_reviews.fileids('pos')
 
	negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
	posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
	negcutoff = len(negfeats)*3/4
	poscutoff = len(posfeats)*3/4
 
	trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
	testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
	print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
	classifier = NaiveBayesClassifier.train(trainfeats)
	print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
	classifier.show_most_informative_features()

def doCollocation(html):
	"""
	Performs NLTK Collcations on Local HTML File
	"""
	bigram_measures = nltk.collocations.BigramAssocMeasures()
	trigram_measures = nltk.collocations.TrigramAssocMeasures()
	#finder = BigramCollocationFinder.from_words(html)
	#finder.nbest(bigram_measures.pmi, 10)  # doctest: +NORMALIZE_WHITESPACE
	#finder.apply_freq_filter(3) #ignoring all bigrams that occur less than 3 in the corpus

	tokens = nltk.wordpunct_tokenize(html)
	finderTag = BigramCollocationFinder.from_words(tokens)
	finderTag.apply_freq_filter(3)
	scored = finderTag.score_ngrams(bigram_measures.raw_freq)
	print sorted(bigram for bigram, score in scored)  # doctest: +NORMALIZE_WHITESPACE