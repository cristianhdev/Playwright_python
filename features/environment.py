import os
from datetime import datetime
import re
import allure
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright


def before_all(context):

    # fecha única por ejecución
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    context.run_path = Path("reports") / fecha

    context.video_path = context.run_path / "videos"
    context.screenshot_path = context.run_path / "screenshots"
    context.trace_path = context.run_path / "traces"

    # crear carpetas
    context.video_path.mkdir(parents=True, exist_ok=True)
    context.screenshot_path.mkdir(parents=True, exist_ok=True)
    context.trace_path.mkdir(parents=True, exist_ok=True)


# Screenshot después de cada step
def after_step(context, step):

    if step.status == "failed":

        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', step.name)
        screenshot = context.screenshot_path / "test_error.png"

        context.page.screenshot(path=screenshot)

        # adjuntar screenshot
        with open(screenshot, "rb") as img:
            allure.attach(
                img.read(),
                name=step.name,
                attachment_type=allure.attachment_type.PNG
            )

        # capturar mensaje de error
        error_message = str(step.exception)

        allure.attach(
            error_message,
            name="Error Message",
            attachment_type=allure.attachment_type.TEXT
        )

    if hasattr(context, "page"):
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', step.name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = context.screenshot_path / f"{safe_name}_{timestamp}.png"

        context.page.screenshot(path=screenshot_path)

        with open(screenshot_path, "rb") as img:
            allure.attach(
                img.read(),
                name=f"{step.name}_{timestamp}",
                attachment_type=allure.attachment_type.PNG
            )


def before_scenario(context, scenario):

    context.playwright = sync_playwright().start()

    browser_name = os.getenv("BROWSER", "chromium")

    if browser_name == "chromium":
        browser_type = context.playwright.chromium
        launch_args = [
            "--start-maximized",
            "--ignore-certificate-errors",
            "--disable-notifications",
            "--disable-extensions",
            "--allow-running-insecure-content",
            "--disable-web-security"
        ]
    elif browser_name == "firefox":
        browser_type = context.playwright.firefox
        launch_args = []
    elif browser_name == "webkit":
        browser_type = context.playwright.webkit
        launch_args = []
    else:
        raise Exception(f"Browser no soportado: {browser_name}")

    context.browser = browser_type.launch(
        #channel="chrome",
        headless=True,
        slow_mo=50,
        args=launch_args
    )

    context.context = context.browser.new_context(
        no_viewport=True,
        record_video_dir=str(context.video_path),
        record_video_size={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )

    context.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    context.page = context.context.new_page()


def after_scenario(context, scenario):

    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', scenario.name)
    timestamp = datetime.now().strftime("%H%M%S")

    # -------------------------
    # Guardar TRACE
    # -------------------------

    trace_file = context.trace_path / f"{safe_name}_{timestamp}.zip"

    context.context.tracing.stop(path=str(trace_file))

    with open(trace_file, "rb") as f:
        allure.attach(
            f.read(),
            name="trace",
            attachment_type=allure.attachment_type.ZIP
        )

    context.context.close()

    # -------------------------
    # Guardar VIDEO
    # -------------------------

    video_path = context.page.video.path()

    new_video_path = context.video_path / f"{safe_name}_{timestamp}.webm"

    shutil.move(video_path, new_video_path)

    context.browser.close()
    context.playwright.stop()