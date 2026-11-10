# mellea-grounded-qa

## Grounded Q&A Assistant
Ask questions over a real set of documents and get answers that cite their source — and an honest "I don't know" when the answer isn't there, instead of a made-up one. Built with [Mellea](https://docs.mellea.ai).

## Setup

Requires Python 3.12+, `pip`, and a backend: Ollama running an IBM Granite model locally, or a hosted Granite endpoint.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Pick a document set:** the FIU course catalog / academic policies · a public product manual · government benefits or tax rules (e.g. IRS publications at `irs.gov`).

**Contribute:** fork, pick an issue, open a PR. Interface (CLI / notebook / web) is your team's choice.
