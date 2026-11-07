from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.chave_pix = self.page.locator("input[placeholder*='Chave Pix']").first
        self.valor_pix = self.page.locator("input[placeholder*='Valor']").first
        self.enviar_pix_button = page.get_by_role("button", name="Enviar Pix")
        
    def fazer_pix(self, chave, valor):
        self.chave_pix.wait_for()
        self.chave_pix.fill(chave)
        self.valor_pix.fill(valor)
        self.enviar_pix_button.click()

    def assert_pix_realizado(self):
        expect(self.page.get_by_text("Transação Realizada com Sucesso!")).to_be_visible()
        
    