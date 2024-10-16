import time
from sklearn.metrics import accuracy_score
from rag_tool import generate_answer

def evaluate_chunking_methods(test_cases, api_key_firework, chunking_methods=['fixed', 'semantic', 'question']):
    results = []

    for test in test_cases:
        url = test["url"]
        question = test["question"]
        print('url:',url)
        print('question:',question)
        
        # Initialize metrics storage for this test case
        method_results = {"url": url, "question": question}

        for method in chunking_methods:
            print("mechod:", method)

            # Track start time for efficiency
            start_time = time.time()
            
            # Generate the answer based on the chosen chunking method
            answer = generate_answer(url, question, api_key_firework, chunking_method=method)
            print("best answer:",answer)
            elapsed_time = time.time() - start_time

            expected_answer = test.get("expected_answer", None)
            accuracy = None
            if expected_answer:
                accuracy = accuracy_score([expected_answer], [answer])

            # Store the results for this method
            method_results[method] = {
                "answer": answer,
                "time": elapsed_time,  # Efficiency metric
                "accuracy": accuracy if accuracy is not None else "Not available"
            }

        results.append(method_results)
    
    return results

def report_results(results):
    for result in results:
        print(f"URL: {result['url']}")
        print(f"Question: {result['question']}")
        
        for method, metrics in result.items():
            if method not in ['url', 'question']:
                print(f"  Method: {method.capitalize()}")
                print(f"    Answer: {metrics['answer']}")
                print(f"    Time: {metrics['time']} seconds")
                print(f"    Accuracy: {metrics['accuracy']}")
                print()