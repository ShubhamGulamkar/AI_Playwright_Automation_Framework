import pytest
from ai.failure_analyzer import analyze_failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    try:
        yield
    except Exception as e:
        explanation = analyze_failure(str(e), item.name)
        print("\n🤖 AI Failure Analysis:\n", explanation)
        raise


# import pytest
# from playwright.sync_api import sync_playwright
# from ai.failure_analyzer import analyze_failure


# # 🔥 VISIBLE PLAYWRIGHT FIXTURE
# @pytest.fixture(scope="function")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=False,   # 👈 MUST be False to see execution
#             slow_mo=800       # 👈 Slow down actions so you can SEE
#         )

#         context = browser.new_context(
#             viewport={"width": 1400, "height": 900}
#         )

#         page = context.new_page()
#         yield page

#         # keep browser visible briefly
#         page.wait_for_timeout(5000)

#         context.close()
#         browser.close()


# # 🤖 AI FAILURE ANALYSIS (KEEP THIS)
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_call(item):
#     try:
#         yield
#     except Exception as e:
#         explanation = analyze_failure(str(e), item.name)
#         print("\n🤖 AI Failure Analysis:\n", explanation)
#         raise


# import pytest
# from ai.failure_analyzer import analyze_failure

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_call(item):
#     try:
#         yield
#     except Exception as e:
#         explanation = analyze_failure(str(e), item.name)
#         print("\n🤖 AI Failure Analysis:\n", explanation)
#         raise
