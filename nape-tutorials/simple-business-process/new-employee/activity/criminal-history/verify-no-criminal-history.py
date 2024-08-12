def evaluate(evidence):
    try:
        # Join the lines to search for the section
        document_text = "".join(evidence)

        # Find the start of the "Criminal History" section
        criminal_history_start = document_text.find("Criminal History")
        
        # Find the start of the next section after "Criminal History"
        next_section_start = document_text.find("\n\n", criminal_history_start)

        # Extract the "Criminal History" section
        if criminal_history_start == -1:
            return "inconclusive", "The 'Criminal History' section cannot be found."
        elif next_section_start == -1:
            criminal_history_section = document_text[criminal_history_start:]
        else:
            criminal_history_section = document_text[criminal_history_start:next_section_start]

        # Determine the outcome based on the content of the "Criminal History" section
        if "No criminal records found" in criminal_history_section:
            return "pass", "The evidence contains the expected statement: 'No criminal records found'."
        elif "No criminal records found" not in criminal_history_section:
            return "fail", "The evidence does not contain the expected statement: 'No criminal records found'."

    except Exception as e:
        # Return an error outcome with the error message
        return "error", f"An error occurred during evaluation: {str(e)}"