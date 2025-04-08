# 🔁 Para interagir com sistema de arquivos
import os

# 📦 Para mover arquivos
import shutil

# 🪟 Interface gráfica
from tkinter import Tk, filedialog, messagebox

# 📅 Data e hora
from datetime import datetime

# 📁 Tipos de arquivos organizados por categorias
TIPOS_DE_ARQUIVOS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Vídeos": [".mp4", ".mov", ".avi"],
    "Documentos": [".docx", ".doc", ".txt", ".odt"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Executáveis": [".exe", ".msi"],
    "Códigos": [".py", ".js", ".java", ".html", ".css"]
}

def criar_pasta(destino: str) -> None:
    """Cria a pasta se ela ainda não existir."""
    if not os.path.exists(destino):
        os.makedirs(destino)

def mover_arquivo(origem: str, destino: str) -> None:
    """Move o arquivo da origem para o destino."""
    shutil.move(origem, destino)

def classificar_arquivo(extensao: str) -> str:
    """Classifica o arquivo com base na extensão."""
    for tipo, extensoes in TIPOS_DE_ARQUIVOS.items():
        if extensao.lower() in extensoes:
            return tipo
    return "Outros"

def organizar_arquivos(pasta: str) -> list:
    """
    Organiza os arquivos da pasta e retorna uma lista com:
    (nome do arquivo, categoria, data de modificação)
    """
    arquivos_movidos = []

    for nome_arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(nome_arquivo)
            categoria = classificar_arquivo(extensao)

            destino = os.path.join(pasta, categoria)
            criar_pasta(destino)

            ultima_mod = os.path.getmtime(caminho_arquivo)
            data_mod = datetime.fromtimestamp(ultima_mod).strftime('%Y-%m-%d %H:%M:%S')

            mover_arquivo(caminho_arquivo, os.path.join(destino, nome_arquivo))
            arquivos_movidos.append((nome_arquivo, categoria, data_mod))

    return arquivos_movidos

def gerar_relatorio(arquivos: list, pasta: str) -> None:
    """Cria um relatório com os arquivos organizados e suas datas."""
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    relatorio_path = os.path.join(pasta, f"relatorio_organizador_{agora}.txt")

    with open(relatorio_path, "w", encoding="utf-8") as rel:
        rel.write("RELATÓRIO DE ORGANIZAÇÃO DE ARQUIVOS\n")
        rel.write(f"Gerado em: {agora}\n\n")
        for nome, categoria, data_mod in arquivos:
            rel.write(f"{nome} → {categoria} (modificado em {data_mod})\n")

def escolher_pasta():
    """Permite o usuário escolher uma pasta, mostra os arquivos, organiza e abre a pasta."""
    pasta = filedialog.askdirectory(title="Selecione a pasta que deseja organizar")

    if pasta:
        # Mostra os arquivos encontrados antes de organizar
        arquivos_na_pasta = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
        
        if not arquivos_na_pasta:
            messagebox.showinfo("Nada encontrado", "A pasta está vazia ou só contém subpastas.")
            return

        # Mostra até 15 arquivos para visualização
        lista_arquivos = "\n".join(arquivos_na_pasta[:15])
        if len(arquivos_na_pasta) > 15:
            lista_arquivos += "\n..."

        messagebox.showinfo("Arquivos encontrados", f"{len(arquivos_na_pasta)} arquivos serão organizados:\n\n{lista_arquivos}")

        # Executa a organização
        arquivos = organizar_arquivos(pasta)
        gerar_relatorio(arquivos, pasta)
        os.startfile(pasta)  # Abre a pasta automaticamente

        messagebox.showinfo("Pronto!", f"{len(arquivos)} arquivos organizados!\nRelatório criado na pasta.")

def main():
    """Inicia o programa com interface oculta até abrir a caixa de seleção."""
    app = Tk()
    app.withdraw()
    escolher_pasta()

if __name__ == "__main__":
    main()
