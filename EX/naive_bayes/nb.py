import csv
from collections import defaultdict
import math

# Read and Preprocess Data
def read_and_preprocess(file_name):
    data = []
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        for topic, text in reader:
            words = [w.lower() for w in text.split() if len(w) > 3]
            data.append((topic, words))
    return data

# Train the Naive Bayes Model
def train_naive_bayes(data):
    word_counts = defaultdict(lambda: defaultdict(int))
    total_words = defaultdict(int)
    vocab = set()

    for topic, words in data:
        for word in words:
            word_counts[topic][word] += 1
            total_words[topic] += 1
            vocab.add(word)

    vocab_size = len(vocab)
    probabilities = defaultdict(dict)

    for topic, word_dict in word_counts.items():
        for word in vocab:
            word_prob = (word_dict[word] + 1) / (total_words[topic] + vocab_size)
            probabilities[topic][word] = math.log(word_prob)

    class_probabilities = {}
    num_docs = len(data)
    for topic in word_counts:
        class_probabilities[topic] = math.log(len(word_counts[topic]) / num_docs)

    return probabilities, class_probabilities, vocab_size, total_words

# Classify an Article
def classify(article, probabilities, class_probabilities, vocab_size, total_words):
    best_class, best_score = None, -float('inf')

    for topic in class_probabilities:
        score = class_probabilities[topic]
        for word in article:
            score += probabilities.get(topic, {}).get(word, math.log(1 / (total_words[topic] + vocab_size)))
        if score > best_score:
            best_class, best_score = topic, score

    return best_class

# Main program
train_data = read_and_preprocess("bbc_train.csv")
probabilities, class_probabilities, vocab_size, total_words = train_naive_bayes(train_data)

test_data = read_and_preprocess("bbc_test.csv")
correct = 0

for actual_topic, words in test_data:
    predicted_topic = classify(words, probabilities, class_probabilities, vocab_size, total_words)
    print(f"Actual: {actual_topic}, Predicted: {predicted_topic}")
    if predicted_topic == actual_topic:
        correct += 1

accuracy = correct / len(test_data)
print(f"\nAccuracy: {accuracy * 100:.2f}%")

