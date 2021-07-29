import json
from pathlib import Path

from selenium.webdriver import Chrome as Driver

from .wrapper import evaluateOnNewDocument


def with_utils(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/utils.js").read_text()
    )
