import os
import re

def parse_tracker(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    phases = []
    current_phase = None
    
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            if current_phase:
                phases.append(current_phase)
            current_phase = {
                "name": line.replace("## ", "").replace("_", " "),
                "tasks": []
            }
        elif line.startswith("- ["):
            is_completed = "[x]" in line or "[X]" in line
            task_name = re.sub(r'- \[[ xX]\] ', '', line).replace("_", " ")
            if current_phase:
                current_phase["tasks"].append({"name": task_name, "completed": is_completed})
                
    if current_phase:
        phases.append(current_phase)
        
    return phases

def generate_html(phases, output_path):
    # Calcular progresso total
    total_tasks = sum(len(p['tasks']) for p in phases)
    completed_tasks = sum(sum(1 for t in p['tasks'] if t['completed']) for p in phases)
    overall_progress = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0
    
    cards_html = ""
    for phase in phases:
        ptotal = len(phase['tasks'])
        pcomp = sum(1 for t in phase['tasks'] if t['completed'])
        pprog = int((pcomp / ptotal * 100)) if ptotal > 0 else 0
        
        tasks_html = ""
        for task in phase['tasks']:
            icon = "✅" if task['completed'] else "⏳"
            color_class = "text-green" if task['completed'] else "text-gray"
            tasks_html += f"<div class='task {color_class}'><span class='icon'>{icon}</span> {task['name']}</div>"
            
        card = f"""
        <div class="card glass" style="--delay: {phases.index(phase) * 0.1}s">
            <h2>{phase['name']}</h2>
            <div class="progress-container">
                <div class="progress-bar" style="width: {pprog}%;"></div>
            </div>
            <p class="progress-text">{pprog}% Concluído ({pcomp}/{ptotal})</p>
            <div class="tasks">
                {tasks_html}
            </div>
        </div>
        """
        cards_html += card

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Progresso - IA</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0f172a;
            --glass-bg: rgba(30, 41, 59, 0.7);
            --glass-border: rgba(255, 255, 255, 0.1);
            --accent-1: #3b82f6; /* Azul */
            --accent-2: #8b5cf6; /* Roxo */
            --accent-3: #ec4899; /* Rosa */
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Outfit', sans-serif;
        }}
        
        body {{
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(236, 72, 153, 0.15) 0px, transparent 50%);
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 50px;
            animation: fadeInDown 1s ease-out;
        }}
        
        .header h1 {{
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(to right, var(--accent-1), var(--accent-2), var(--accent-3));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }}
        
        .header p {{
            font-size: 1.2rem;
            color: var(--text-muted);
        }}
        
        /* Progresso Geral */
        .overall-glass {{
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 30px;
            max-width: 800px;
            margin: 0 auto 50px auto;
            text-align: center;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            animation: fadeInUp 1s ease-out 0.2s both;
        }}
        
        .overall-glass h2 {{
            font-size: 1.5rem;
            margin-bottom: 20px;
            font-weight: 600;
        }}
        
        .progress-container-large {{
            width: 100%;
            height: 24px;
            background: rgba(0,0,0,0.3);
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 15px;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        }}
        
        .progress-bar-large {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-1), var(--accent-2), var(--accent-3));
            border-radius: 12px;
            width: {overall_progress}%;
            transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .progress-bar-large::after {{
            content: "";
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transform: skewX(-20deg);
            animation: shine 3s infinite;
        }}
        
        .overall-stats {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
        }}
        
        .stat-box {{
            display: flex;
            flex-direction: column;
        }}
        
        .stat-value {{
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--text-main);
        }}
        
        .stat-label {{
            font-size: 0.9rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Grid de Cartões */
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .glass {{
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            animation: fadeInUp 0.8s ease-out calc(0.3s + var(--delay)) both;
        }}
        
        .glass:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.5);
            border-color: rgba(255, 255, 255, 0.2);
        }}
        
        .glass h2 {{
            font-size: 1.25rem;
            margin-bottom: 15px;
            color: var(--text-main);
            font-weight: 600;
        }}
        
        .progress-container {{
            width: 100%;
            height: 8px;
            background: rgba(0,0,0,0.3);
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 10px;
        }}
        
        .progress-bar {{
            height: 100%;
            background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
            border-radius: 4px;
            transition: width 1s ease-in-out;
        }}
        
        .progress-text {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 20px;
            text-align: right;
        }}
        
        .tasks {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-height: 200px;
            overflow-y: auto;
            padding-right: 5px;
        }}
        
        /* Custom Scrollbar */
        .tasks::-webkit-scrollbar {{
            width: 4px;
        }}
        .tasks::-webkit-scrollbar-track {{
            background: transparent;
        }}
        .tasks::-webkit-scrollbar-thumb {{
            background: rgba(255,255,255,0.2);
            border-radius: 4px;
        }}
        
        .task {{
            font-size: 0.95rem;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            padding: 8px 12px;
            background: rgba(0,0,0,0.2);
            border-radius: 8px;
            transition: background 0.2s ease, transform 0.2s ease;
        }}
        
        .task:hover {{
            background: rgba(0,0,0,0.4);
            transform: translateX(5px);
        }}
        
        .icon {{
            font-size: 1.1rem;
            margin-top: -2px;
        }}
        
        .text-green {{
            color: var(--text-muted);
            text-decoration: line-through;
            opacity: 0.7;
        }}
        
        .text-gray {{
            color: var(--text-main);
        }}
        
        /* Animations */
        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        @keyframes shine {{
            0% {{ left: -100%; }}
            20% {{ left: 200%; }}
            100% {{ left: 200%; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Roadmap: Visão Computacional e IA</h1>
        <p>Acompanhamento de Evolução e Laboratórios</p>
    </div>
    
    <div class="overall-glass">
        <h2>Sua Jornada Completa</h2>
        <div class="progress-container-large">
            <div class="progress-bar-large"></div>
        </div>
        <div class="overall-stats">
            <div class="stat-box">
                <span class="stat-value">{overall_progress}%</span>
                <span class="stat-label">Concluído</span>
            </div>
            <div class="stat-box">
                <span class="stat-value">{completed_tasks}</span>
                <span class="stat-label">Desafios Vencidos</span>
            </div>
            <div class="stat-box">
                <span class="stat-value">{total_tasks - completed_tasks}</span>
                <span class="stat-label">Restantes</span>
            </div>
        </div>
    </div>
    
    <div class="grid">
        {cards_html}
    </div>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    base_dir = r"c:\Desenvolvimento\Especialista em Visão Computacional e IA"
    tracker_path = os.path.join(base_dir, "tracker_de_progresso.md")
    output_path = os.path.join(base_dir, "dashboard.html")
    
    phases = parse_tracker(tracker_path)
    generate_html(phases, output_path)
    print("Dashboard visual gerado com sucesso!")
