# Análise de Casos de Dengue - DATASUS

Este projeto tem como objetivo a extração, tratamento e análise de dados de casos de dengue no Brasil, com foco específico no município de Belo Horizonte, utilizando a base de dados oficial do **SINAN (DATASUS)**.

O pipeline consiste na extração automática via API, processamento dos dados para limpeza e padronização, e uma análise exploratória visual através de um Jupyter Notebook.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **[PySUS](https://pysus.readthedocs.io/)**: Biblioteca para acesso e download de dados do DATASUS.
- **Pandas**: Manipulação e tratamento de dados.
- **Matplotlib**: Geração de gráficos e visualizações.
- **Pathlib**: Manipulação robusta de caminhos de arquivos.
- **Jupyter Notebook**: Ambiente para análise exploratória de dados (EDA).

## 📁 Estrutura do Projeto

```text
projeto/
├── data/
│   ├── processed/      # Dados limpos e prontos para análise (.csv)
│   └── raw/            # Dados brutos extraídos do DATASUS (.json / .parquet)
├── src/
│   ├── extract/        # Scripts de extração de dados
│   │   └── download_file.py
│   └── transform/      # Scripts de limpeza e padronização
│       └── tratamentos.py
├── notebook.ipynb      # Análise visual e exploratória
├── requirements.txt    # Dependências do projeto
└── README.md
```

## ⚙️ Como Executar

### 1. Configurar o Ambiente
Certifique-se de ter um ambiente virtual ativo e instale as dependências:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

### 2. Análise
Abra o arquivo `notebook.ipynb` em seu editor ou via Jupyter para extrair, tratar e visualizar os gráficos de:
- Distribuição por gênero.
- Sintomas mais comuns em mulheres e homens.
- Análise de casos por estado gestacional.

## 📊 Principais Funcionalidades
- **Extração Dinâmica**: Utiliza o PySUS para buscar arquivos específicos de Dengue por ano.
- **Limpeza Inteligente**: Mapeia códigos numéricos do SINAN para termos legíveis (ex: 'M' -> 'Masculino').
- **Caminhos Robustos**: Implementação com `pathlib` que garante funcionamento em qualquer sistema operacional e diretório.
- **Visualização Avançada**: Gráficos customizados para facilitar a tomada de decisão em saúde pública.

