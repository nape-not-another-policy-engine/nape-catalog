import json


def evaluate(lines):
    pull_request = json.loads(''.join(lines))
    requestor = pull_request['user']['login']
    reviewers = [reviewer['login'] for reviewer in pull_request['requested_reviewers']]
    if requestor in reviewers:
        return 'failed', f'The PR Requestor is also a reviewer. Requestor: [{requestor}], Reviewer(s): {reviewers}'
    else:
        return 'passed', f'The PR Requestor is not a reviewer. Requestor: [{requestor}], Reviewer(s): {reviewers}'


def description():
    return 'Verify the peer review requestor is not one of the people who approve the peer review.'
