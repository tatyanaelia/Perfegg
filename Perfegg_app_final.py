import flet as ft
import time

def main(page: ft.Page):
    page.title = "Perfegg"
    page.window_width = 400
    page.window_height = 700
    page.bgcolor = "#E6F4F1"  # Cor de fundo azul clara

    # Função Timer
    def iniciar_timer(tempo, tipo, imagem):
        page.clean()

        titulo = ft.Text(tipo, size=30, weight=ft.FontWeight.BOLD, color="#F5A623", font_family="Arial")
        img = ft.Image(src=imagem, width=200, height=200)

        contador = ft.Text(f"00:{tempo // 60:02}:{tempo % 60:02}", size=26, weight=ft.FontWeight.BOLD)

        timer_box = ft.Container(
            content=ft.Row([
                ft.Image(src="assets/timer_icon.png", width=30, height=30),
                contador
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="#E96A5E",
            border_radius=20,
            padding=15
        )

        page.add(
            ft.Column(
                [
                    ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(img, bgcolor="#FBC02D", border_radius=20, padding=20),
                    timer_box
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
            )
        )
        page.update()

        # Contagem regressiva
        for i in range(tempo, 0, -1):
            contador.value = f"00:{i // 60:02}:{i % 60:02}"
            page.update()
            time.sleep(1)

            # Quando o tempo acaba, mostra tela de alerta
        tela_alarme(tipo)

    # Tela de Alarme
    def tela_alarme(tipo):
        page.clean()

        #titulo = ft.Text(f"Seu {tipo} está pronto!", size=26, weight=ft.FontWeight.BOLD, color="#F5A623")
        imagem_alarme = ft.Image(src="assets/Alarme Final.png", width=250, height=250)
        botao_voltar = ft.ElevatedButton(
            text="Voltar",
            style=ft.ButtonStyle(
                bgcolor="#F5A623",
                color="white",
                text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
            ),
            on_click=lambda e: tela_inicial()  # Usando lambda para ignorar o argumento 'e'
        )

        page.update()

        page.add(
            ft.Column(
                [
                    #titulo,
                    imagem_alarme,
                    botao_voltar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )
        page.update()

    # Tela Inicial
    def tela_inicial():
        page.clean()

        titulo = ft.Text("Escolha seu Perfegg", size=18, color="#D8A87A")

        img_logo = ft.Image(src="assets/logo.png", width=150, height=150)

        botao_poche = ft.GestureDetector(
            content=ft.Column(
                [ft.Image(src="assets/Botão_poche.png", width=80, height=80), ft.Text("poché", color="#F5A623")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            on_tap=lambda e: iniciar_timer(180, "Poché", "assets/ovo_poche.png")
        )

        botao_cremoso = ft.GestureDetector(
            content=ft.Column(
                [ft.Image(src="assets/botao_cremoso.png", width=80, height=80), ft.Text("cremoso", color="#D8A87A")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            on_tap=lambda e: iniciar_timer(420, "Cremoso", "assets/ovo_cremoso.png")
        )

        botao_duro = ft.GestureDetector(
            content=ft.Column(
                [ft.Image(src="assets/botao_duro.png", width=80, height=80), ft.Text("duro", color="#D8A87A")],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            on_tap=lambda e: iniciar_timer(600, "Duro", "assets/ovo_duro.png")
        )

        page.add(
            ft.Column(
                [
                    img_logo,
                    titulo,
                    ft.Row([botao_poche, botao_cremoso, botao_duro], alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )
        page.update()

    tela_inicial()


ft.app(target=main)