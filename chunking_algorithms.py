# pip install nltk sklearn
# python -m spacy download en_core_web_sm

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

def fixed_size_chunking(content, chunk_size=500):
    words = content.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]



def semantic_chunking(content):
    # Ensure you've downloaded the 'punkt' tokenizer model
    nltk.download('punkt')
    # Split the content into sentences
    sentences = nltk.sent_tokenize(content)
    paragraphs = []
    current_paragraph = []

    # Combine sentences into paragraphs (based on full stops or empty lines)
    for sent in sentences:
        current_paragraph.append(sent)
        # Assuming a paragraph ends with a period or empty line (this can be tweaked)
        if sent.endswith('.') or len(sent.strip()) == 0:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    # If there are remaining sentences that don't form a complete paragraph
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return paragraphs



def question_based_chunking(content, question):
    # Use NLTK's semantic chunking to get paragraphs or sentences
    chunks = semantic_chunking(content)

    # Use TF-IDF to calculate the similarity between the question and each chunk
    vectorizer = TfidfVectorizer().fit_transform([question] + chunks)
    vectors = vectorizer.toarray()
    
    # Calculate cosine similarity between the question and each chunk
    cosine_similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    
    # Select chunks with the highest similarity scores (you can adjust how many chunks to return)
    relevant_chunks = [chunks[i] for i in cosine_similarities.argsort()[::-1][:5]]
    
    return relevant_chunks