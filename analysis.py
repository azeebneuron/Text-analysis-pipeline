import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize, sent_tokenize
import os

# nltk.download('punkt')
# nltk.download('cmudict')
print("halla bol")
# Function to calculate the number of syllables in a word
d = cmudict.dict()
def count_syllables(word):
    try:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    except KeyError:
        # Handle the case where the word is not found in the dictionary
        return 0

# Function to calculate the FOG index
def calculate_fog_index(avg_sentence_length, percentage_complex_words):
    return 0.4 * (avg_sentence_length + percentage_complex_words)

# Function to calculate the number of personal pronouns
def count_personal_pronouns(text):
    tokens = word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    return len([word for word, tag in tags if tag == 'PRP'])

# Initialize the output data list
output_data = []

# Read text files from the 'article-texts' folder
for filename in os.listdir('article-texts'):
    with open(os.path.join('article-texts', filename), 'r', encoding='utf-8') as file:
        text = file.read()

        # TextBlob analysis
        blob = TextBlob(text)
        positive_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity > 0)
        negative_score = sum(1 for sentence in blob.sentences if sentence.sentiment.polarity < 0)
        polarity_score = blob.sentiment.polarity
        subjectivity_score = blob.sentiment.subjectivity

        sentences = sent_tokenize(text)
        word_count = len(word_tokenize(text))
        syllable_count = sum(count_syllables(word) for word in word_tokenize(text))
        personal_pronouns = count_personal_pronouns(text)
        avg_sentence_length = word_count / len(sentences)
        avg_words_per_sentence = word_count / len(sentences)
        complex_word_count = sum(1 for word in word_tokenize(text) if count_syllables(word) > 2)
        percentage_complex_words = complex_word_count / word_count * 100
        fog_index = calculate_fog_index(avg_sentence_length, percentage_complex_words)
        avg_word_length = sum(len(word) for word in word_tokenize(text)) / word_count

        output_data.append([positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
                           percentage_complex_words, fog_index, complex_word_count, word_count, syllable_count, personal_pronouns,
                           avg_word_length, avg_words_per_sentence])

# Create output DataFrame
output_df = pd.DataFrame(output_data, columns=['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH',
                                              'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'COMPLEX WORD COUNT', 'WORD COUNT',
                                              'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH', 'AVG NUMBER OF WORDS PER SENTENCE'])

# Read the URLs from 'Input.xlsx'
input_data = pd.read_excel('Input.xlsx')

# Add the 'URL_ID' and 'URL' columns from the input data to the output data
output_df['URL_ID'] = input_data['URL_ID']
output_df['URL'] = input_data['URL']

# Save the output to an Excel file
output_df.to_excel('Output.xlsx', index=False)

