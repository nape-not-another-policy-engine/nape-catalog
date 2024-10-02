def evaluate(evidence):
    try:
        return "fail", r"Unit Test Greater than 80% Needs Implementation"
    except Exception as e:
        # Return an error outcome with the error message
        return "error", f"An error occurred during evaluation: {str(e)}"
