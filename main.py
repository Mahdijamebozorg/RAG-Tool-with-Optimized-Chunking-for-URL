from  testing_suite import evaluate_chunking_methods, report_results

if __name__ == "__main__":

    # api_key_serp = "9214eda095aea59fb778940dd62b03ce28c7a175"
    api_key_firework = "fw_3Zi8BcFgfk6DibZoDNq4Z7Qp"

    test_cases = [
        {
            "url": "https://en.wikipedia.org/wiki/Climate_change",
            "question": "What are the impacts of climate change?"
        },
        {
            "url": "https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm",
            "question": "What are the health benefits of physical activity?"
        }
    ]

    results = evaluate_chunking_methods(test_cases, api_key_firework)
    report_results(results)