from testing_suite import test_chunking_methods

if __name__ == "__main__":

    urls = [
        "https://en.wikipedia.org/wiki/Climate_change",
        "https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm",
    ]
    questions = [
        "What are the impacts of climate change?",
        "What are the health benefits of physical activity",
    ]
    api_key_serp = "9214eda095aea59fb778940dd62b03ce28c7a175"
    api_key_firework = "fw_3Zi8BcFgfk6DibZoDNq4Z7Qp"
    
    test_chunking_methods(
        urls=urls,
        questions=questions,
        api_key_serp=api_key_serp,
        api_key_firework=api_key_firework
    )