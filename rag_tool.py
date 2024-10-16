from serp_api import get_url_content
from chunking_algorithms import fixed_size_chunking, semantic_chunking, question_based_chunking
from firework_api import generate_answer_api, select_best_answer_api
from content_preprocessor import clean_content

def generate_answer(url, question, api_key_firework, chunking_method='fixed'):
    # Retrieve and clean content
    raw_content = ...
    try: 
      raw_content = get_url_content(url)
    except:
      return "Can't read url data"

    clean_text = clean_content(raw_content)
    # Apply the chosen chunking method (e.g., fixed-size, semantic, or question-based)
    if chunking_method == 'fixed':
        chunks = fixed_size_chunking(clean_text)
    elif chunking_method == 'semantic':
        chunks = semantic_chunking(clean_text)
    elif chunking_method == 'question':
        chunks = question_based_chunking(clean_text, question)
    else:
        raise ValueError("Invalid chunking method")

    # Collect answers for each chunk
    answers = []
    for chunk in chunks:
        print("chunk:", chunk)
        answer = generate_answer_api(chunk, question, api_key_firework)
        print('answer:', answer)
        answers.append(answer)

    if not answers:
      return "No answer found"

    return select_best_answer_api(answers,question,api_key_firework)