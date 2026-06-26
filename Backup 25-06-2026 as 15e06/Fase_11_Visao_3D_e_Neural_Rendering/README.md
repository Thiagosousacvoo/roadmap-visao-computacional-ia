# 🧊 Fase 11 — Visão 3D e Neural Rendering

A Inteligência Artificial ganha profundidade geométrica.
A área de visão não é apenas tentar "reconstruir" o espaço como um joguinho de videogame vazio, mas sim modelar fotorrealismo puro simulando a passagem da luz e as distâncias reais de forma neural.

## 🗺️ MAPA DE NAVEGAÇÃO

```
Fase_11_Visao_3D_e_Neural_Rendering/
│
├── Bloco_01_A_Matematica_da_Camera/     ← Coordenadas Homogêneas, Translação, Rotação e [R|t].
├── Bloco_02_Profundidade_e_Point_Clouds/← Adicionando Profundidade a JPGs estáticos (DepthAnything).
├── Bloco_03_Structure_from_Motion_COLMAP/← (Em breve) Padrão Ouro para Fotogrametria.
├── Bloco_04_A_Revolucao_Neural/         ← (Em breve) NeRF vs 3D Gaussian Splatting.
└── Projetos_Finais_Visao_3D/            ← (Em breve)
```

## ⏱️ ORDEM DE EXECUÇÃO

| # | Notebook | Bloco | Prioridade |
|---|---|---|---|
| 1 | `01_coordenadas_homogeneas` | Bloco 01 | 🔴 Crítico |
| 2 | `02_intrinsecas_e_extrinsecas` | Bloco 01 | 🔴 Crítico |
| 3 | `01_estimativa_de_profundidade_monocular` | Bloco 02 | 🟠 Importante |
| 4 | `02_point_clouds_com_open3d` | Bloco 02 | 🟠 Importante |

| 5 | `01_colmap_na_pratica` | Bloco 03 | 🔴 Crítico |
| 6 | `01_volume_rendering_e_nerf` | Bloco 04 | 🔴 Crítico |
| 7 | `02_3d_gaussian_splatting` | Bloco 04 | 🔴 Crítico |
| 8 | `Projeto_01_Scanner_3D_Caseiro` | Projetos Finais | 🔴 Obrigatório |
| 9 | `Projeto_02_Renderizacao_Gaussian_Splatting` | Projetos Finais | 🔴 Obrigatório |

## ✅ CRITÉRIOS DE SAÍDA (FASE 11)

Antes de ir para a última fase (Carreira e Portfólio):
- [ ] Entender perfeitamente o papel de uma Matriz Intrínseca `K` na lente de uma câmera.
- [ ] Compreender por que a geometria clássica exige COLMAP antes de podermos rodar IAs mais recentes como o NeRF.
- [ ] (Ainda a vir) Treinar a sua primeira cena de Splatting Gaussiano.
