# 🧹 Organizador de Arquivos Inteligente

Este projeto foi criado para **organizar automaticamente os arquivos de uma pasta**, separando-os por tipo (PDFs, imagens, vídeos, códigos, etc.) em subpastas, e gerando um **relatório completo com a data de modificação** de cada item.

---

## 📌 Funcionalidades

✅ Escolha de qualquer pasta do computador  
✅ Visualização dos arquivos que serão organizados  
✅ Organização automática por tipo de arquivo  
✅ Geração de relatório `.txt` com os dados  
✅ Abertura automática da pasta após a organização  
✅ Interface simples e amigável  
✅ Arquivo `.exe` para rodar sem precisar ter Python

---

## 🧠 Como funciona

Assim que o programa é iniciado:

1. Uma janela será aberta pedindo para você selecionar a pasta que deseja organizar.
2. Os arquivos encontrados serão listados (até 15 itens) antes da organização.
3. O programa organiza os arquivos em subpastas:
/Imagens /PDFs /Vídeos /Documentos /Códigos /Executáveis /Outros
4. Um arquivo `relatorio_organizador_DATA.txt` é gerado com os nomes e datas dos arquivos movidos.
5. A pasta é aberta automaticamente após a organização.

---

## ▶️ Como usar (com Python instalado e sem o Python instalado!)

1. Clone o projeto ou baixe o arquivo `organizador_arquivos.py`
2. Crie e ative uma virtualenv (opcional):
python -m venv .venv
source .venv/Scripts/activate
3. Instale o PyInstaller (caso queira gerar .exe):
pip install pyinstaller
4. Rode o script:
python organizador_arquivos.py

##  Como usar sem Python (arquivo .exe)
Baixe o arquivo OrganizaDocs.exe da pasta /dist

Dê dois cliques no .exe

Escolha a pasta que deseja organizar

Veja a mágica acontecer ✨

##💡 Tecnologias utilizadas
Python 3.13+

tkinter para interface gráfica

os e shutil para automação

datetime para controle de datas

PyInstaller para empacotamento

##👩‍💻 Desenvolvido por
Adriane Oliveira – Engenheira de Software em construção 💙
