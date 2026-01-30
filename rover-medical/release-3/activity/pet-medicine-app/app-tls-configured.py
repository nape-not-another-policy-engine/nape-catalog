import tomllib

def evaluate(evidence):
    try:
        # Expected values
        expected_references = {
            "cert_ref": "secrets://vault/prod/pet-med-app_tls_cert_pem",
            "key_ref": "secrets://vault/prod/pet-med-app_tls_key_pem",
            "ca_bundle_ref": "secrets://vault/prod/trusted_client_ca_bundle_pem"
        }

        # Convert evidence list to a single string and parse as TOML
        evidence_content = ''.join(evidence)
        config = tomllib.loads(evidence_content)

        # Extract actual values from parsed config
        actual_references = {
            "cert_ref": config.get("app", {}).get("tls", {}).get("cert_ref"),
            "key_ref": config.get("app", {}).get("tls", {}).get("key_ref"),
            "ca_bundle_ref": config.get("app", {}).get("tls", {}).get("ca_bundle_ref")
        }

        # Evaluate each reference
        outcomes = []
        for key, expected_value in expected_references.items():
            found_value = actual_references.get(key)

            if found_value is None:
                outcomes.append((key, "inconclusive", f"\n\tThe {key} field is not found in the evidence."))
            elif found_value != expected_value:
                outcomes.append((key, "fail", f"\nThe {key} does not match.\n\tExpected: {expected_value}\n\tActual: {found_value}."))
            else:
                outcomes.append((key, "pass", f"\nThe {key} matches the expected value: {expected_value}."))

        # Determine overall outcome
        if all(outcome[1] == "pass" for outcome in outcomes):
            expected_values = "".join(f"\n\t{key}: {val}" for key, val in expected_references.items())
            return "pass", f"All references match their expected values.{expected_values}"

        if any(outcome[1] == "fail" for outcome in outcomes):
            fail_reasons = [outcome[2] for outcome in outcomes if outcome[1] == "fail"]
            return "fail", f"One or more references do not match.{''.join(fail_reasons)}"

        if any(outcome[1] == "inconclusive" for outcome in outcomes):
            inconclusive_reasons = [outcome[2] for outcome in outcomes if outcome[1] == "inconclusive"]
            return "inconclusive", f"One or more references are inconclusive.{''.join(inconclusive_reasons)}"
        return None

    except Exception as e:
        return "error", f"An error occurred during evaluation: {str(e)}"