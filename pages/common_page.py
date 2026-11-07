from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.voltar_para_home = page.get_by_role("button", name="Voltar para a Home")

    def assert_text(self, text):
        self.page.get_by_text(text).wait_for()
        expect(self.page.get_by_text(text)).to_be_visible(timeout=10000)

    def voltar_home(self):
        self.voltar_para_home.wait_for(state="visible", timeout=10000)
        self.voltar_para_home.click()
        