from config.settings import BASE_URL
from core.screenshot import capture_screenshot

def execute_steps(page, steps, test_name="ai_test"):
    try:
        for step in steps:
            action = step["action"]

            if action == "goto":
                page.goto(BASE_URL)

            elif action == "fill":
                page.get_by_role(step["role"], name=step["name"]).fill(step["value"])

            elif action == "click":
                page.get_by_role(step["role"], name=step["name"]).click()

            elif action == "assert_text":
                page.get_by_text(step["text"]).is_visible()

        capture_screenshot(page, test_name, "PASS")

    except Exception:
        capture_screenshot(page, test_name, "FAIL")
        raise


# def execute_steps(page, steps):
#     for step in steps:
#         action = step["action"]

#         if action == "goto":
#             page.goto(step["value"], wait_until="domcontentloaded")

#         elif action == "fill":
#             page.get_by_label(step["field"]).fill(step["value"])

#         elif action == "click":
#             page.get_by_role(step["role"], name=step["name"]).click()

#         elif action == "assert_text":
#             assert page.get_by_text(step["value"]).is_visible()
