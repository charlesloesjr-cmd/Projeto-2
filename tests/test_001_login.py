def test_001_login_successful(login_page) -> None:
    login_page.login("user1", "pass1")
    login_page.assert_login_successful()