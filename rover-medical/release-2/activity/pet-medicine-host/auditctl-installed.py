def evaluate(evidence):
    try:
        active_status = None
        for line in evidence:
            if 'Active:' in line:
                active_status = line.strip().split('Active:')[1].strip()
                break

        if active_status is None:
            return ("inconclusive", "No 'Active:' status found in the evidence.")

        if active_status == 'active (running)':
            return ("pass", "The service is active and running as expected the evidence shows as: 'Active: active (running)'.")

        return ("fail", f"The service is not active and running. Found status: '{active_status}'.")

    except Exception as e:
        return ("error", f"An error occurred while evaluating the evidence: {str(e)}")