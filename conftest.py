import pytest
from pywinauto import Application, Desktop
import time



@pytest.fixture()
def Setup_teardown():
    app = Application(backend="uia").start("calc.exe")
    time.sleep(2)

    # Connect to Calculator window
    calc = Desktop(backend="uia").window(title="Calculator")
    return calc