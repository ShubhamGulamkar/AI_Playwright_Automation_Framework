import os
from datetime import datetime

def capture_screenshot(page, test_name, status):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{test_name}_{status}_{timestamp}.png"
    page.screenshot(path=path)
