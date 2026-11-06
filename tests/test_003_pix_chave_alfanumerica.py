def test_002_fazer_pix(common_page, login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    home_page.acessar_menu("Fazer Pix")
    pix_page.fazer_pix("QY.A9T.PGK/0001-68", "30,00")
    pix_page.assert_pix_realizado()
    common_page.voltar_home()
    home_page.assert_text("4.970,00")
    home_page.acessar_menu("Ver Extrato")
    common_page.assert_text("Pix para QY.A9T.PGK/0001-68 - R$ -30,00")
