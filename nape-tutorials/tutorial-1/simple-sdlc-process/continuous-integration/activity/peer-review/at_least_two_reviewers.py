import json

def evaluate(lines):
    min_pr_reviewers = 2
    pull_request = json.loads(''.join(lines))
    reviewers = pull_request['requested_reviewers']
    if len(reviewers) >= min_pr_reviewers:
        return 'pass', f'There are {len(reviewers)} PR Reviewers.'
    else:
        return 'fail', (f'There are only {len(reviewers)} PR Reviewers, when there needs to '
                          f'be a minimum of {min_pr_reviewers} PR Reviewers.')
