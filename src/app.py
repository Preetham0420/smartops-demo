New-Item -ItemType Directory -Force "src" | Out-Null
@'
def add(a, b):
    return a + b
'@ | Set-Content -NoNewline -Encoding UTF8 src\app.py
