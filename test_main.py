import subprocess
import sys


def test_main_prints_expected_message():
    result = subprocess.run(
        [sys.executable, "main.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "hello world with medium priority"