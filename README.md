# PerceptronClassifier-HotelReviews--NLP

# Overview
In this assignment you will write perceptron classifiers (vanilla and averaged) to identify hotel reviews as either true or fake, and either positive or negative. You may using the word tokens as features, or any other features you can devise from the text. The assignment will be graded based on the performance of your classifiers, that is how well they perform on unseen test data compared to the performance of a reference classifier.

# Data
The training and development data are the same as for Coding Exercise 2, and are available as a compressed ZIP archive on Blackboard. The uncompressed archive contains the following files:

One file train-labeled.txt containing labeled training data with a single training instance (hotel review) per line (total 960 lines). The first 3 tokens in each line are:
a unique 7-character alphanumeric identifier
a label True or Fake
a label Pos or Neg
These are followed by the text of the review.
One file dev-text.txt with unlabeled development data, containing just the unique identifier followed by the text of the review (total 320 lines).
One file dev-key.txt with the corresponding labels for the development data, to serve as an answer key.
Readme and license files (which you won’t need for the exercise).

# Programs
The perceptron algorithms appear in Hal Daumé III, A Course in Machine Learning (v. 0.99 draft), Chapter 4: The Perceptron.

You will write two programs: perceplearn.py will learn perceptron models (vanilla and averaged) from the training data, and percepclassify.py will use the models to classify new data. If using Python 3, you will name your programs perceplearn3.py and percepclassify3.py. The learning program will be invoked in the following way:

> python perceplearn.py /path/to/input

The argument is a single file containing the training data; the program will learn perceptron models, and write the model parameters to two files: vanillamodel.txt for the vanilla perceptron, and averagedmodel.txt for the averaged perceptron. The format of the model files is up to you, but they should follow the following guidelines:

The model files should contain sufficient information for percepclassify.py to successfully label new data.
The model files should be human-readable, so that model parameters can be easily understood by visual inspection of the file.
The classification program will be invoked in the following way:

> python percepclassify.py /path/to/model /path/to/input

The first argument is the path to the model file (vanillamodel.txt or averagedmodel.txt), and the second argument is the path to a file containing the test data file; the program will read the parameters of a perceptron model from the model file, classify each entry in the test data, and write the results to a text file called percepoutput.txt in the same format as the answer key.

# Notes
Problem formulation. Since a perceptron is a binary classifier, you need to treat the problem as two separate binary classification problems (true/fake and positive/negative); each of the model files (vanilla and averaged) needs to have the model parameters for both classifiers.
Features and tokenization. You’d need to develop some reasonable method of identifying features in the text. Some common options are removing certain punctuation, or lowercasing all the letters. You may also find it useful to ignore certain high-frequency or low-frequency tokens. You may use any tokenization method which you implement yourselves. Experiment, and choose whichever works best.
Runtime efficiency. Vocareum imposes a limit on running times, and if a program takes too long, Vocareum will kill the process. Your program therefore needs to run efficiently. You need an efficient way to store the training instances, in order to avoid reading them over and over again (reading and parsing text is slow). Also, feature vectors for individual training instances are typically fairly sparse: for a reference solution with about 1000 features, the mean number of non-zero features per training instance is about 77; it would be highly inefficient to multiply and add all the 900+ zeros at every step. The reference solution stores the training data as a python dict indexed by the unique identifiers of the reviews, and the feature vector for each training instance as a dict of the form feature:count. With about 1000 features and 100 iterations (which is far more than needed, due to overfitting), run times for the reference solution are under 5 seconds for running perceplearn.py on the training data, running on a MacBook Pro from 2016.
Overfitting. The perceptron has a tendency to overfit the training data. For example, with about 1000 features, the reference solution models the training data perfectly after about 30 iterations.

