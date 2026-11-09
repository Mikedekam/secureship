docs/incident.md

# Incident Report: Hardcoded API Key

## Summary
A demo weather API key was hardcoded in config.py and committed to Git history. The exercise showed that deleting a secret from the current file does not remove it from earlier commits.

## Timeline
- Date/time unknown: API key committed in <commit id> (file: config.py)
- Date/time unknown: key deleted from the file in <commit id>, but still in history
- Date/time unknown: leak detected with gitleaks
- Date/time unknown: Key removal from history was attempted with git filter-repo; the attempts shown stopped with errors.
- Date/time unknown: history rewritten with git filter-repo and force-pushed
- Date/time unknown: secrets moved to a .env file that Git ignores
- Date/time unknown: .env was added to .gitignore; Git confirmed .env is ignored.

## What was exposed
A simulated weather API key was exposed. I’m not including the key itself in this report.

## Impact
A real key exposed in a public repository could be exposed, copied and misused by attackers.

## Actions taken
1. Rotated the key: simulated, because the key was fake
2. Removed the key from all history with git filter-repo
3. Moved configuration to environment variables and a .env file

## Still visible after cleanup
Even after a successful rewrite, old clones or forks can retain previous history.

## Prevention
1. Keep secrets in environment variables or an ignored .env file.
2. Commit a .env.example with placeholder values, never real keys.
3. Use secret scanning and rotate any real key immediately if exposed.

