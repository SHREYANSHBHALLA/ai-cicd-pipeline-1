def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def validate_input(data):
    """Validates the input data for the AI agent."""
    if not isinstance(data, str) or not data.strip():
        raise ValueError("Input must be a non-empty string.")
    return True

def measure_performance(start_time, end_time):
    """Calculates the performance duration."""
    return end_time - start_time