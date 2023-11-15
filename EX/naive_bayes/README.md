# BBC News Article Classifier with Naive Bayes

 This project implements a Naive Bayes classifier to categorize BBC news articles into topics like tech, politics, business, entertainment, and sport.
 The model is trained on a dataset of 2000 articles, with preprocessing involving conversion of all words to lowercase and removal of short words. 
 It calculates word frequencies per category, using Laplace smoothing for probability estimation. The classifier then predicts the category of each article in a separate test set by multiplying the probabilities of its words for each topic, choosing the topic with the highest probability as its prediction.
 This approach achieved an accuracy of 96.00 %, showcasing its capability in text classification tasks.