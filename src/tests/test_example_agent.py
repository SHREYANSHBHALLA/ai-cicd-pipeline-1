import pytest
from src.agents.example_agent import process_input, generate_response

def test_process_input():
    # Test valid input
    input_data = "Hello, AI!"
    expected_output = "Processing input: Hello, AI!"
    assert process_input(input_data) == expected_output

    # Test empty input
    input_data = ""
    expected_output = "No input provided."
    assert process_input(input_data) == expected_output

def test_generate_response():
    # Test response generation
    input_data = "What is your name?"
    expected_response = "I am an AI agent."
    assert generate_response(input_data) == expected_response

    # Test unknown input
    input_data = "Tell me a joke."
    expected_response = "I'm not programmed for jokes."
    assert generate_response(input_data) == expected_response

def test_response_latency():
    import time

    input_data = "How are you?"
    start_time = time.time()
    generate_response(input_data)
    latency = time.time() - start_time

    assert latency < 1  # Response should be generated in less than 1 second

def test_security_compliance():
    # Example test for security compliance
    input_data = "<script>alert('test');</script>"
    expected_output = "Input contains unsafe characters."
    assert process_input(input_data) == expected_output