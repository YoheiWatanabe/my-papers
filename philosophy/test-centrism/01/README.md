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

```bash
PYTHONPATH=src pytest tests/test_my_module.py -v -s
PYTHONPATH=src pytest tests/test_my_module.py::test_add -v -s
```

```bash
pytest tests/tdd_gcd_tutorial/my_module/test_my_module.py -v -s
pytest tests/tdd_gcd_tutorial/my_module/ -v -s
```
