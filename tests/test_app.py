New-Item -ItemType Directory -Force "tests" | Out-Null
@'
from src.app import add

def test_add():
    assert add(2, 2) == 4
'@ | Set-Content -NoNewline -Encoding UTF8 tests\test_app.py
