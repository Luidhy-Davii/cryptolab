import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

from constantes import MENU_PRINCIPAL
from utils import validar_inteiro
from criptografias import cesar, vigenere, rsa, base64_crypto, sha256_hash
from laboratorio import executar_laboratorio


console = Console()


def mostrar_menu():
    menu = """
[cyan]1[/cyan] - Cifra de César
[cyan]2[/cyan] - Vigenère
[cyan]3[/cyan] - RSA
[cyan]4[/cyan] - Base64
[cyan]5[/cyan] - SHA-256
[cyan]6[/cyan] - Laboratório
[red]0[/red] - Sair
"""
    console.print(
        Panel.fit(
            menu,
            title="[bold green]🔐 CryptoLab[/bold green]",
            border_style="bright_blue"
        )
    )


def iniciar():
    from logger_config import configurar_logger
    configurar_logger()

    while True:
        mostrar_menu()

        opcao = Prompt.ask("[bold yellow]Escolha uma opção[/bold yellow]")

        try:
            if opcao == "1":
                mensagem = Prompt.ask("Mensagem")
                chave = validar_inteiro(Prompt.ask("Chave numérica"))
                resultado = cesar.criptografar(mensagem, chave)

                console.print(f"[bold green]Resultado:[/bold green] {resultado}")
                logging.info("César utilizado")

            elif opcao == "2":
                mensagem = Prompt.ask("Mensagem")
                chave = Prompt.ask("Chave textual")
                resultado = vigenere.criptografar(mensagem, chave)

                console.print(f"[bold green]Resultado:[/bold green] {resultado}")
                logging.info("Vigenère utilizado")

            elif opcao == "3":
                mensagem = Prompt.ask("Mensagem")

                chave_publica, chave_privada = rsa.gerar_chaves()
                cifra = rsa.criptografar(mensagem, chave_publica)
                texto_original = rsa.descriptografar(cifra, chave_privada)

                table = Table(title="🔑 RSA", box=box.ROUNDED)

                table.add_column("Tipo", style="cyan", no_wrap=True)
                table.add_column("Valor", style="magenta")

                table.add_row("Chave Pública", str(chave_publica))
                table.add_row("Chave Privada", str(chave_privada))
                table.add_row("Mensagem Criptografada", str(cifra))
                table.add_row("Mensagem Descriptografada", texto_original)

                console.print(table)

            elif opcao == "4":
                mensagem = Prompt.ask("Mensagem")
                resultado = base64_crypto.criptografar(mensagem)

                console.print(f"[bold green]Resultado:[/bold green] {resultado}")
                logging.info("Base64 utilizado")

            elif opcao == "5":
                mensagem = Prompt.ask("Mensagem")

                console.print("[bold red]⚠ SHA-256 não pode ser revertido.[/bold red]")
                console.print(
                    f"[bold green]Hash:[/bold green] {sha256_hash.gerar_hash(mensagem)}"
                )
                logging.info("SHA-256 utilizado")

            elif opcao == "6":
                mensagem = Prompt.ask("Mensagem para laboratório")
                executar_laboratorio(mensagem)

            elif opcao == "0":
                console.print("[bold red]Encerrando CryptoLab...[/bold red]")
                break

            else:
                console.print("[bold red]Opção inválida.[/bold red]")

        except Exception as erro:
            console.print(f"[bold red]Erro:[/bold red] {erro}")
            logging.error(f"Erro ocorrido: {erro}")


if __name__ == "__main__":
    iniciar()