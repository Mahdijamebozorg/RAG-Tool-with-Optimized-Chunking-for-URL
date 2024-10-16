import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Fixed-Size Chunking
def fixed_size_chunking(content, chunk_size=500):
    words = content.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# Semantic Chunking
def semantic_chunking(content, chunk_size=500):
    sentences = nltk.sent_tokenize(content)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_length = sentence_length
        else:
            current_chunk.append(sentence)
            current_length += sentence_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

# Question-Based Chunking
def question_based_chunking(content, question, top_n=5):
    chunks = semantic_chunking(content)
    vectorizer = TfidfVectorizer().fit_transform([question] + chunks)
    vectors = vectorizer.toarray()
    cosine_similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    relevant_indices = cosine_similarities.argsort()[::-1][:top_n]
    return [chunks[i] for i in relevant_indices]