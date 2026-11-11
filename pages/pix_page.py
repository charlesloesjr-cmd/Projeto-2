
# from playwright.sync_api import Page, expect


# class PixPage:
#     def __init__(self, page: Page):
#         self.page = page
#         self.chave_pix = page.get_by_role(
#             "textbox", name="Chave Pix", exact=False
#         )
#         self.valor_pix = page.get_by_role("textbox", name="Valor")
#         self.enviar_pix_button = page.get_by_role(
#             "button", name="Enviar Pix"
#         )

#     # def fazer_pix(self, chave, valor):
#     #     expect(self.chave_pix).to_be_visible(timeout=15000)
#     #     self.chave_pix.fill(chave)
#     #     self.valor_pix.fill(valor)
#     #     self.enviar_pix_button.click()

#     def fazer_pix(self, chave, valor):
#         expect(self.chave_pix).to_be_visible(timeout=15000)

#     self.chave_pix.fill(chave)
#     self.valor_pix.fill(valor)

#     print("Chave Pix preenchida:", self.chave_pix.input_value())
#     print("Valor preenchido:", self.valor_pix.input_value())

#     self.enviar_pix_button.click()

#     self.page.wait_for_timeout(2000)

#     print("URL após envio:", self.page.url)
#     print("Conteúdo após envio:")
#     print(self.page.locator("body").inner_text())

#     def assert_pix_realizado(self):
#         expect(
#             self.page.get_by_text("Transação Realizada com Sucesso!")
#         ).to_be_visible()

#         expect(
#             self.page.get_by_text(
#                 "A transação foi concluída com sucesso. "
#                 "Você pode voltar para a página principal e continuar suas operações."
#             )
#         ).to_be_visible()


from playwright.sync_api import Page, expect


class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.chave_pix = page.get_by_role(
            "textbox", name="Chave Pix", exact=False
        )
        self.valor_pix = page.get_by_role("textbox", name="Valor")
        self.enviar_pix_button = page.get_by_role(
            "button", name="Enviar Pix"
        )

    def fazer_pix(self, chave, valor):
        expect(self.chave_pix).to_be_visible(timeout=15000)

        self.chave_pix.click()
        self.chave_pix.press_sequentially(chave, delay=100)

        self.valor_pix.click()
        self.valor_pix.press_sequentially(valor, delay=100)

        self.enviar_pix_button.click()

    def assert_pix_realizado(self):
        expect(
            self.page.get_by_text("Transação Realizada com Sucesso!")
        ).to_be_visible()

        expect(
            self.page.get_by_text(
                "A transação foi concluída com sucesso. "
                "Você pode voltar para a página principal e continuar suas operações."
            )
        ).to_be_visible()
