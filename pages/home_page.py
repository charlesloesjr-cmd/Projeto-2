from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def acessar_menu(self, menu):
        botao = self.page.get_by_role(
            "button", name=menu, exact=True
        )

        expect(botao).to_be_visible()
        botao.click()

        if menu == "Fazer Pix":
            expect(
                self.page.get_by_role(
                    "heading", name="Faça um Pix"
                )
            ).to_be_visible(timeout=10000)

    def assert_saldo_atual(self, saldo_atual_esperado):
        expect(
            self.page.get_by_text(saldo_atual_esperado)
        ).to_be_visible()

    def assert_text(self, texto):
        expect(self.page.get_by_text(texto)).to_be_visible()