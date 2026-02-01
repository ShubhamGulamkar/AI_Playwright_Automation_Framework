from ai.step_parser import parse_steps
from core.executor import execute_steps

def test_login_using_ai(page):
    steps_in_english = """
    Open the login page
    Enter username as tomsmith
    Enter password as SuperSecretPassword!
    Click on Login
    Verify successful login
    """

    steps = parse_steps(steps_in_english)
    execute_steps(page, steps)
