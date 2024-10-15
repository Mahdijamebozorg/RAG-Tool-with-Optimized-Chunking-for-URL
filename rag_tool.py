from firework_api import call_firework_api
from serp_api import get_url_content
from content_preprocessor import clean_content
from chunking_algorithms import fixed_size_chunking, semantic_chunking, question_based_chunking


def _select_best_answer(answers):
    # Sort answers by relevance and return the most relevant one
    best_answer = max(answers, key=lambda x: x.get('relevance', 0))
    return best_answer['text'] if 'text' in best_answer else "No relevant answer found"

def generate_answer(url, question, api_key_serp, api_key_firework):
    # Retrieve and clean content
    raw_content = get_url_content(url, api_key_serp)
    clean_text = clean_content(raw_content)

    # Apply chunking methods
    fixed_chunks = fixed_size_chunking(clean_text)
    semantic_chunks = semantic_chunking(clean_text)
    question_chunks = question_based_chunking(clean_text, question)

    # Combine chunks for processing (or prioritize one type)
    all_chunks = fixed_chunks + semantic_chunks + question_chunks

    # Send each chunk to Firework API and collect responses
    answers = []
    for chunk in all_chunks:
        answer = call_firework_api(chunk, question, api_key_firework)
        answers.append(answer)

    # Evaluate and select the best answer
    return _select_best_answer(answers)
