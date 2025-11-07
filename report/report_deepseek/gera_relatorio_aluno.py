from ollama import chat
from ollama import ChatResponse
import json
from gera_cci import gera_cci_aluno
from gera_prompt_aluno import gera_prompt

prompt_file = "prompt_aluno.txt"
report_output_file_html = "report_examples/report_aluno_v8.html"
report_raw_output = "report_examples/report_raw_aluno_v8.txt"

def gera_relatorio_deepseek():
    with open(prompt_file, "r", encoding="utf-8") as file:
        prompt = file.read()

    response: ChatResponse = chat(
        model="deepseek-r1:14b", 
        messages = [{'role': 'user', 'content': prompt}],
    )

    report_txt = response['message']['content']

    with open(report_raw_output, "w", encoding="utf-8") as f:
        f.write(report_txt)
    
    print("Report gerado e salvo em ", report_raw_output)

    report_html = report_txt.split("===INICIO_HTML===")[1].split("===FIM_HTML===")[0].strip()

    with open(report_output_file_html, "w", encoding="utf-8") as f:
        f.write(report_html)


matricula = "210054649904"
questao = 18
area_conhecimento = "CN"
estado = "PA"

cci_file = gera_cci_aluno(matricula, questao, area_conhecimento, estado)
print("Informações reunidas")

gera_prompt(matricula, questao, estado, area_conhecimento, cci_file)
print("Prompt gerado")

gera_relatorio_deepseek()