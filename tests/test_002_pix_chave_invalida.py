def test_002_fazer_pix(common_page, login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("a92d9a$%&*", "10,00")

    # Clique explícito no botão de voltar antes de validar o saldo na home
    common_page.voltar_home.click()

    home_page.assert_text("4.990,00")