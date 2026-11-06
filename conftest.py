import pytest
from playwright.sync_api import Page

from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage


@pytest.fixture(autouse=True)
def setup_page(page: Page):
    page.set_viewport_size({"width": 1500, "height": 750})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")

@pytest.fixture
def common_page(page: Page):
    return CommonPage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture
def pix_page(page: Page):
    return PixPage(page)