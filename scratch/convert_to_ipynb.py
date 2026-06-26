import os
import json

directory = r"c:\Desenvolvimento\Especialista em Visão Computacional e IA\Fase_00_Fundamentos_Python\Bloco_1_Fundamentos"

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        cells = []
        current_md = []
        current_code = []
        
        for line in lines:
            stripped = line.strip()
            
            # Se for linha de comentário ou divisória
            if stripped.startswith("#"):
                if current_code:
                    # Finalizar bloco de código
                    # Remove trailing empty lines from code
                    while current_code and not current_code[-1].strip():
                        current_code.pop()
                    if current_code:
                        cells.append({
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "outputs": [],
                            "source": current_code
                        })
                    current_code = []
                
                # Transformar em Markdown
                md_text = line[1:]
                if md_text.startswith(" "):
                    md_text = md_text[1:]
                current_md.append(md_text)
                
            else:
                # Código (ou linhas em branco entre códigos)
                if current_md:
                    # Finalizar bloco de markdown
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": current_md
                    })
                    current_md = []
                    
                current_code.append(line)
                
        if current_md:
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": current_md
            })
        if current_code:
            while current_code and not current_code[-1].strip():
                current_code.pop()
            if current_code:
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": current_code
                })
            
        notebook = {
            "cells": cells,
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 5
        }
        
        ipynb_filename = filename.replace(".py", ".ipynb")
        ipynb_filepath = os.path.join(directory, ipynb_filename)
        
        with open(ipynb_filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
            
        # Remover o script py antigo para evitar duplicidade
        os.remove(filepath)

print("Convertido para ipynb!")
