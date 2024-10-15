from rag_tool import generate_answer

def test_chunking_methods(urls, questions, api_key_serp, api_key_firework):
    for url, question in zip(urls, questions):
        answer = generate_answer(url, question, api_key_serp, api_key_firework)
        print(f"URL: {url}, Question: {question}, Answer: {answer}")