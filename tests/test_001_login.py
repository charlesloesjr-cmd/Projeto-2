
def test_001_login_successful(login_page, setup_page, page) -> None:
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()

    page.screenshot(
        path="evidencias/login/login_sucesso.png",
        full_page=True
    )
