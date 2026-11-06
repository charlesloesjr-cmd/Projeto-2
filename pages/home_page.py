from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
                
    def acessar_menu(self, menu):
        self.page.get_by_role("button", name=f"{menu}").click()

    def assert_saldo_atual(self, saldo_ataual_esperado):
        self.page.get_by_text(saldo_ataual_esperado)

    def assert_text(self, texto):
        expect(self.page.get_by_text(texto)).to_be_visible()