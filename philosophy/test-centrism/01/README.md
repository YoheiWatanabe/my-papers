# README

## Environment

### Activate

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Deactivate

```bash
deactivate
```

## Test Execution

```bash
Mac/Linux:
PYTHONPATH=src pytest -v -s

Windows
set PYTHONPATH=src
pytest -v -s
```
