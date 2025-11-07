# Projeto de Análise TRI (Teoria da Resposta ao Item)

## 📦 Bibliotecas necessárias

### 🐍 Python
- pandas  
- chardet  
- numpy  
- matplotlib  
- reportlab  
- plotly  

### 📊 R
- dplyr  
- eRm  
- ltm  

---

## 🗂️ Estrutura e Funções dos Arquivos

### **pre-processamento/Itens_prova_geral_2022.ipynb**
- **Função:** Extrair as provas usadas na análise do banco ENEM e salvar nas pastas `Itens_provas_amarela` e `Itens_provas_azul`
- **Execução:** Notebook — basta executar todas as células após instalar `pandas` e `chardet`

---

### **pre-processamento/tratamento_geracao_matriz_binaria.ipynb**
- **Função:** Ler itens das pastas `Itens_provas_amarela` e `Itens_provas_azul` e gerar matrizes binárias em `matrizes_binarias`
- **Execução:** Notebook — executar após instalar `pandas`, `numpy` e `chardet`

---

### **codigos_R/ERM/erm_1PL.R**
- **Função:** Carregar matrizes binárias, transformá-las em objetos ERM, extrair parâmetros de habilidade e dificuldade e salvar os resultados
- **Execução:** Arquivo Rmd — executar células após instalar `eRm` e `dplyr`

---

### **codigos_R/ERM/probabilidade_ERM_1PL.R**
- **Função:** Calcular a probabilidade de acerto com base nos parâmetros gerados e salvar na pasta `probabilidades`
- **Execução:** Arquivo Rmd — executar após instalar `dplyr`

---

### **codigos_R/ERM/gera_graficos.py**
- **Função:** Ler o CSV de probabilidades e gerar curvas características do item (CCI)
- **Execução:** Rodar após instalar `pandas` e `plotly`

---

### **codigos_R/LTM_2PL/ltm_2PL.Rmd**
- **Função:** Transformar matrizes binárias em objetos `ltm`, extrair habilidade, dificuldade e discriminação e salvar resultados
- **Execução:** Arquivo Rmd — instalar `ltm` e `dplyr`

---

### **codigos_R/LTM_2PL/probabilidade_LTM_2PL.Rmd**
- **Função:** Calcular probabilidade de acerto e salvar em `probabilidades`
- **Execução:** Arquivo Rmd — instalar `dplyr`

---

### **codigos_R/LTM_2PL/gera_graficos.py**
- **Função:** Gerar CCI baseado no CSV de probabilidades
- **Execução:** Rodar após instalar `pandas` e `plotly`

---

### **codigos_R/LTM_3PL/ltm_3PL.Rmd**
- **Função:** Transformar matrizes em objetos `ltm`, extrair habilidade, dificuldade, discriminação e acerto ao acaso e salvar resultados
- **Execução:** Arquivo Rmd — instalar `ltm` e `dplyr`

---

### **codigos_R/LTM_3PL/probabilidade_LTM_3PL.Rmd**
- **Função:** Calcular probabilidade de acerto e salvar na pasta `probabilidades`
- **Execução:** Arquivo Rmd — instalar `dplyr`

---

### **codigos_R/LTM_3PL/gera_graficos.py**
- **Função:** Gerar curvas CCI a partir dos CSVs de probabilidades
- **Execução:** Rodar após instalar `pandas` e `plotly`

---

### **report/create_report.py**
- **Função:** Carregar resultados gerados (examinando + questões) e gerar relatório final para um aluno e uma questão
- **Execução:**
```bash
cd report
python create_report.py
