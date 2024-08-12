import xml.etree.ElementTree as ET


def evaluate(evidence):
    try:
        # Parse the XML evidence string
        evidence_str = "".join(evidence)
        root = ET.fromstring(evidence_str)

        # Find the specific training video
        training_video = root.find(".//TrainingVideo[Title='Introduction to Security Policies']")

        if training_video is None:
            return (
                "inconclusive", "The training video 'Introduction to Security Policies' was not found in the evidence.")

        # Extract the status and score
        status = training_video.find("Status").text
        score_str = training_video.find("Score").text

        # Convert score to integer, handle potential ValueError
        try:
            score = int(score_str.strip('%'))
        except ValueError:
            return "error", f"Failed to parse the score: {score_str}"

        # Determine the outcome based on status and score
        if status == "Completed" and score > 70:
            return "pass", (f"The training video 'Introduction to Security Policies' is completed and the score is "
                            f"greater than 70% at {score}%.")
        elif status == "Completed":
            return ("fail",
                    f"The training video 'Introduction to Security Policies' is completed but the score is {score}%, "
                    f"which is not greater than 70%.")
        else:
            return "inconclusive", "The training video 'Introduction to Security Policies' is not completed."

    except ET.ParseError as e:
        return "error", f"An error occurred while parsing the XML: {str(e)}"
    except Exception as e:
        return "error", f"An unexpected error occurred: {str(e)}"
