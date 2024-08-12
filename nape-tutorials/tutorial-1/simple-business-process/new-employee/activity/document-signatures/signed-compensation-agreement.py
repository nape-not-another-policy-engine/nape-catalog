import json


def evaluate(evidence):
    """
    Evaluates the evidence to check if the Compensation Agreement is signed.

    :param evidence: List of strings, each representing a line of the JSON evidence file.
    :return: Tuple of (outcome, reason)
    """
    try:
        # Join the lines to form the complete JSON string
        json_data = ''.join(evidence)

        # Parse the JSON data
        data = json.loads(json_data)

        # Navigate to the documents_signed section
        documents = data.get("onboarding", {}).get("documents_signed", [])

        # Search for the Compensation Agreement
        for document in documents:
            if document.get("name") == "Compensation Agreement":
                if document.get("signed") is True:
                    return "pass", "Compensation Agreement is signed."
                else:
                    return "fail", "Compensation Agreement is found but not signed."

        # If Compensation Agreement is not found
        return "inconclusive", "Compensation Agreement is not found in the evidence."

    except Exception as e:
        # Handle any runtime error and return error outcome
        return "error", f"An error occurred during evaluation: {str(e)}"
