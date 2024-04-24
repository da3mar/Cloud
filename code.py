import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # Tokenize text
        words = nltk.word_tokenize(text)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
        # Count word frequency
        word_freq = Counter(filtered_words)
        return word_freq

if __name__ == "__main__":
    file_path = "random_paragraphs.txt"
    word_freq = process_text(file_path)
    print(word_freq)
