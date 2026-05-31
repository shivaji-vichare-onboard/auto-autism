import subprocess
import sys


def test_hello_script():
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "hello world with low priority"