# Tela inicial:
    # Título: Hashzap (mas vou mudar para ficar a minha cara)
    # Botão: Iniciar Chat
        # Quando clicar no botão:
        # Abrir um popup/modal/alerta
            # Título: Bem vindo ao Hashzap
            # Caixa de texto: Escreva seu nome no chat
            # Botão: entrar no chat
                # Quando clicar no botão
                # Fechar o popup 
                # Sumir com o título
                # sumir com o botão Iniciar Chat 
                    # Carregar o chat
                    # Carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # Botão Enviar
                        # Quando clicar no botão Enviar
                        # enviar a mensagem
                        # Limpar a caixa de mensagem

# flet

# importar o flet
import flet as ft 

# criar uma função principal para rodar o seu aplicativo
def main(pagina):
    # titulo
    titulo = ft.Text("Caiozap")
    pagina.add(titulo)

    def enviar_mensagem_tunel(mensagem):
        # Executar tudo oq eu quero que aconteça para todos os usuários
        # que receberem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # Limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem",
                                                    on_submit=enviar_mensagem) 

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # Fechar o popup
        popup.open = False 
        # Sumir com o título
        pagina.remove(titulo)
        # sumir com o botão Iniciar Chat
        pagina.remove(botao)
        # Carregar o chat
        pagina.add(chat)
        # carregar o campo de enviar mensagem
        # carregar o botão Enviar 
        pagina.add(linha_enviar)

        # adicionar no chat a mensagem "Cleber entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # Criar o botão (pop up)
    titulo_popup = ft.Text("Bem Vindo ao Caiozap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, 
                           actions=[botao_popup])

    # botao incial      
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True # Demorei mais de 8 horas para perceber que
        pagina.update()   # troquei o popup.open por pagina.open
                          # Que óóóóóódioooooooooooooooooo
                          # Falta de atenção do caralho!!!   
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(botao)

# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)