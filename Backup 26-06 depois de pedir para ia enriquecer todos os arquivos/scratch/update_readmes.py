import os
import re

base_path = r"c:\Desenvolvimento\Especialista em Visão Computacional e IA"
roadmap_path = os.path.join(base_path, "Roadmap")

def get_blocks_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    blocks = []
    current_title = "Intro"
    current_content = []
    
    for line in lines:
        # Procurar por cabeçalhos que tenham BLOCO ou PROJETO
        if line.startswith('#') and ('BLOCO' in line.upper() or 'PROJETO' in line.upper()):
            if current_content:
                blocks.append((current_title, '\n'.join(current_content)))
            current_title = line.strip('# *')
            current_content = [line]
        else:
            current_content.append(line)
            
    if current_content:
        blocks.append((current_title, '\n'.join(current_content)))
        
    return blocks

for phase_folder in os.listdir(base_path):
    if not phase_folder.startswith("Fase_"):
        continue
        
    phase_num = phase_folder.split('_')[1]
    
    # Encontrar o arquivo do roadmap correspondente (ex: Fase 0.md, Fase 4 .md)
    roadmap_file = None
    for f in os.listdir(roadmap_path):
        if f.startswith(f"Fase {int(phase_num)}") and f.endswith(".md"):
            roadmap_file = os.path.join(roadmap_path, f)
            break
            
    if not roadmap_file:
        print(f"Roadmap não encontrado para {phase_folder}")
        continue
        
    blocks = get_blocks_from_file(roadmap_file)
    
    phase_path = os.path.join(base_path, phase_folder)
    for block_folder in os.listdir(phase_path):
        block_path = os.path.join(phase_path, block_folder)
        if not os.path.isdir(block_path):
            continue
            
        match = re.search(r'Bloco_(\d+)', block_folder, re.IGNORECASE)
        content_to_write = ""
        
        if match:
            b_num = match.group(1)
            for title, b_content in blocks:
                # Se for BLOCO 4, vai pegar BLOCO 4, BLOCO 4.2, BLOCO 4.3, etc.
                if f"BLOCO {b_num}" in title.upper():
                    content_to_write += b_content + "\n\n"
        elif "Projeto" in block_folder or "Projetos" in block_folder:
            for title, b_content in blocks:
                if "PROJETO" in title.upper():
                    content_to_write += b_content + "\n\n"
                    
        if not content_to_write:
            content_to_write = "Conteúdo não extraído. Verifique o Roadmap original."
            
        readme_path = os.path.join(block_path, "README.md")
        
        final_content = f"""# 🎯 {block_folder.replace('_', ' ')}

{content_to_write.strip()}

---
## 🚀 Como Proceder
- Crie seus scripts Python (`.py`) ou Notebooks (`.ipynb`) dentro desta pasta.
- Não copie e cole código pronto da internet. Digite e entenda linha por linha.
- Quando terminar, chame a IA (Antigravity) para avaliação e sabatina!
"""
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(final_content)

print("READMES atualizados com o conteúdo dos roadmaps!")
