#--------------------------------------------------------
#  INEP/Daeb-Diretoria de Avaliação da Educação Básica 
#  Coordenação-Geral de Medidas da Educação Básica (CGMEB)			
#--------------------------------------------------------

#--------------------------------------------------------
#  PROGRAMA:                                                                                                      
#           INPUT_R_QUEST_HAB_ESTUDO
#--------------------------------------------------------
#  DESCRIÇÃO: PROGRAMA PARA LEITURA DA BASE DE QUESTIONÁRIOS SOBRE       
#             HÁBITOS DE ESTUDO NA PANDEMIA, QUE COMPÕE OS MICRODADOS    
#             DO ENEM DE 2022
#--------------------------------------------------------

#------------------------------------------------------------------------
# Obs:                                                                                                                    
#     Para abrir a base dos questionários é necessário salvar este programa                     
#     e o arquivo QUEST_HAB_ESTUDO.csv no mesmo diretório.	                  
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#                   ATENÇÃO              
#------------------------------------------------------------------------
# Este programa abre a base de dados com os rótulos das variáveis de	                    
# acordo com o dicionário de dados que compõem os microdados. 		  
#------------------------------------------------------------------------

#--------------------
# Intalação do pacote Data.Table
# Se não estiver instalado
#--------------------
if(!require(data.table)){install.packages('data.table')}

#--------------------
# Caso deseje trocar o local do arquivo, 
# edit a função setwd() a seguir informando o local do arquivo.
# Ex. Windows setwd("C:/temp")
#     Linux   setwd("/home")
#--------------------
setwd("C:/")  

#---------------
# Alocação de memória
#---------------
memory.limit(24576)

#------------------
# Carga dos microdados
QUEST_HAB_ESTUDO <- data.table::fread(input='QUEST_HAB_ESTUDO.csv',
                                integer64='character',
                                skip=0,  #Ler do inicio
                                nrow=-1, #Ler todos os registros
                                na.strings = "", 
                                showProgress = TRUE)

#---------------------------
# A script a seguir formata os rótulos das respostas
# Para formatar um item retire o caracter de comentário (#) no início na linha desejada 
#---------------------------

#QUEST_HAB_ESTUDO$TP_RESPOSTA = factor(QUEST_HAB_ESTUDO$TP_RESPOSTA, levels = c(0, 1, 2), labels = c('Não (Participante optou por não responder o questionário).', 'Sim (Participante optou por responder o questionário).', 'Responder Depois'))

#QUEST_HAB_ESTUDO$Q001  = factor(QUEST_HAB_ESTUDO$Q001, levels = c('A', 'B', 'C', 'D', 'E'), labels = c('Eu estive matriculado(a) no Ensino Médio regular.','Eu estive matriculado(a) no Ensino Médio, em turma de EJA.', 'Eu estive matriculado(a) no Ensino Médio integrado à Educação Profissional.', 'Eu concluí o Ensino Médio antes de 2021.', 'Eu não concluí o Ensino Médio e nem estive matriculado(a) nesse período.'))        

#QUEST_HAB_ESTUDO$Q002  = factor(QUEST_HAB_ESTUDO$Q002, levels = c('A', 'B', 'C'), labels = c('Eu continuei os estudos sem interromper o ano letivo.','Eu decidi interromper os estudos no primeiro ano da pandemia, mas me rematriculei em 2021.','Eu fui levado a interromper os estudos no primeiro ano da pandemia por não ter recebido suporte da escola, mas me rematriculei em 2021.')) 

#QUEST_HAB_ESTUDO$Q003  = factor(QUEST_HAB_ESTUDO$Q003, levels = c('A', 'B', 'C', 'D', 'E'), labels = c('Eu apenas tive aulas presenciais nesse período.','Eu apenas estudei em casa de forma remota nesse período.','Eu estudei de forma híbrida, ou seja, em casa remotamente e em aulas presenciais.','Eu realizei atividades de estudo diversas, mas sem estar matriculado(a) no Ensino Médio.','Eu não estive matriculado(a) regularmente, nem realizei atividades de estudo.'))

#QUEST_HAB_ESTUDO$Q004  = factor(QUEST_HAB_ESTUDO$Q004, levels = c('A', 'B', 'C', 'D', 'E', 'F'), labels = c('Eu aprendi mais no ensino remoto (estudando somente em casa).','Eu aprendi mais estudando de forma híbrida.','Eu aprendi mais estudando de forma presencial.','Eu aprendi no ensino remoto ou híbrido na mesma medida de quando eu estava no ensino presencial.','Eu não estive matriculado(a) em 2021, mas aprendi estudando por conta própria.','Eu não estive matriculado(a) em 2021 e nem estudei.'))

#QUEST_HAB_ESTUDO$Q005  = factor(QUEST_HAB_ESTUDO$Q005, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))

#QUEST_HAB_ESTUDO$Q006  = factor(QUEST_HAB_ESTUDO$Q006, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q007  = factor(QUEST_HAB_ESTUDO$Q007, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q008  = factor(QUEST_HAB_ESTUDO$Q008, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q009  = factor(QUEST_HAB_ESTUDO$Q009, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q010  = factor(QUEST_HAB_ESTUDO$Q010, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q011  = factor(QUEST_HAB_ESTUDO$Q011, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q012  = factor(QUEST_HAB_ESTUDO$Q012, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q013  = factor(QUEST_HAB_ESTUDO$Q013, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q014  = factor(QUEST_HAB_ESTUDO$Q014, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q015  = factor(QUEST_HAB_ESTUDO$Q015, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q016  = factor(QUEST_HAB_ESTUDO$Q016, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q017  = factor(QUEST_HAB_ESTUDO$Q017, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q018  = factor(QUEST_HAB_ESTUDO$Q018, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q019  = factor(QUEST_HAB_ESTUDO$Q019, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q020  = factor(QUEST_HAB_ESTUDO$Q020, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q021  = factor(QUEST_HAB_ESTUDO$Q021, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q022  = factor(QUEST_HAB_ESTUDO$Q022, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q023  = factor(QUEST_HAB_ESTUDO$Q023, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))        

#QUEST_HAB_ESTUDO$Q024  = factor(QUEST_HAB_ESTUDO$Q024, levels = c('A', 'B', 'C', 'D'), labels = c('Nenhuma vez.','Poucas vezes.','Muitas vezes.','Em todas as vezes.'))

#QUEST_HAB_ESTUDO$Q025A = factor(QUEST_HAB_ESTUDO$Q025A, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q025B = factor(QUEST_HAB_ESTUDO$Q025B, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q025C = factor(QUEST_HAB_ESTUDO$Q025C, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q025D = factor(QUEST_HAB_ESTUDO$Q025D, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q025E = factor(QUEST_HAB_ESTUDO$Q025E, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q025F = factor(QUEST_HAB_ESTUDO$Q025F, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026A = factor(QUEST_HAB_ESTUDO$Q026A, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026B = factor(QUEST_HAB_ESTUDO$Q026B, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026C = factor(QUEST_HAB_ESTUDO$Q026C, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026D = factor(QUEST_HAB_ESTUDO$Q026D, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026E = factor(QUEST_HAB_ESTUDO$Q026E, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026F = factor(QUEST_HAB_ESTUDO$Q026F, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026G = factor(QUEST_HAB_ESTUDO$Q026G, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q026H = factor(QUEST_HAB_ESTUDO$Q026H, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q027  = factor(QUEST_HAB_ESTUDO$Q027, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028A = factor(QUEST_HAB_ESTUDO$Q028A, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028B = factor(QUEST_HAB_ESTUDO$Q028B, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028C = factor(QUEST_HAB_ESTUDO$Q028C, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028D = factor(QUEST_HAB_ESTUDO$Q028D, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028E = factor(QUEST_HAB_ESTUDO$Q028E, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028F = factor(QUEST_HAB_ESTUDO$Q028F, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028G = factor(QUEST_HAB_ESTUDO$Q028G, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028H = factor(QUEST_HAB_ESTUDO$Q028H, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028I = factor(QUEST_HAB_ESTUDO$Q028I, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028J = factor(QUEST_HAB_ESTUDO$Q028J, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028K = factor(QUEST_HAB_ESTUDO$Q028K, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028L = factor(QUEST_HAB_ESTUDO$Q028L, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028M = factor(QUEST_HAB_ESTUDO$Q028M, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028N = factor(QUEST_HAB_ESTUDO$Q028N, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028O = factor(QUEST_HAB_ESTUDO$Q028O, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028P = factor(QUEST_HAB_ESTUDO$Q028P, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028Q = factor(QUEST_HAB_ESTUDO$Q028Q, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q028R = factor(QUEST_HAB_ESTUDO$Q028R, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q029  = factor(QUEST_HAB_ESTUDO$Q029, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030A = factor(QUEST_HAB_ESTUDO$Q030A, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030B = factor(QUEST_HAB_ESTUDO$Q030B, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030C = factor(QUEST_HAB_ESTUDO$Q030C, levels = c('A', 'B'), labels = c('Sim','Não'))        

#QUEST_HAB_ESTUDO$Q030D = factor(QUEST_HAB_ESTUDO$Q030D, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030E = factor(QUEST_HAB_ESTUDO$Q030E, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030F = factor(QUEST_HAB_ESTUDO$Q030F, levels = c('A', 'B'), labels = c('Sim','Não'))       

#QUEST_HAB_ESTUDO$Q030G = factor(QUEST_HAB_ESTUDO$Q030G, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q031  = factor(QUEST_HAB_ESTUDO$Q031, levels = c('A', 'B', 'C'), labels = c('Sim','Não','Precisei de ajuda para estudar, mas não tive ninguém para me auxiliar.'))

#QUEST_HAB_ESTUDO$Q032A = factor(QUEST_HAB_ESTUDO$Q032A, levels = c('A', 'B'), labels = c('Sim','Não'))   

#QUEST_HAB_ESTUDO$Q032B = factor(QUEST_HAB_ESTUDO$Q032B, levels = c('A', 'B'), labels = c('Sim','Não'))  

#QUEST_HAB_ESTUDO$Q032C = factor(QUEST_HAB_ESTUDO$Q032C, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q032D = factor(QUEST_HAB_ESTUDO$Q032D, levels = c('A', 'B'), labels = c('Sim','Não'))  

#QUEST_HAB_ESTUDO$Q032E = factor(QUEST_HAB_ESTUDO$Q032E, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q032F = factor(QUEST_HAB_ESTUDO$Q032F, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q032G = factor(QUEST_HAB_ESTUDO$Q032G, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033A = factor(QUEST_HAB_ESTUDO$Q033A, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033B = factor(QUEST_HAB_ESTUDO$Q033B, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033C = factor(QUEST_HAB_ESTUDO$Q033C, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033D = factor(QUEST_HAB_ESTUDO$Q033D, levels = c('A', 'B'), labels = c('Sim','Não'))  

#QUEST_HAB_ESTUDO$Q033E = factor(QUEST_HAB_ESTUDO$Q033E, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033F = factor(QUEST_HAB_ESTUDO$Q033F, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033G = factor(QUEST_HAB_ESTUDO$Q033G, levels = c('A', 'B'), labels = c('Sim','Não'))  

#QUEST_HAB_ESTUDO$Q033H = factor(QUEST_HAB_ESTUDO$Q033H, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033I = factor(QUEST_HAB_ESTUDO$Q033I, levels = c('A', 'B'), labels = c('Sim','Não')) 

#QUEST_HAB_ESTUDO$Q033J = factor(QUEST_HAB_ESTUDO$Q033J, levels = c('A', 'B'), labels = c('Sim','Não'))  

#QUEST_HAB_ESTUDO$Q034  = factor(QUEST_HAB_ESTUDO$Q034, levels = c('A', 'B', 'C', 'D', 'E'), labels = c('Nada preparado(a).','Um pouco preparado(a).','Bem preparado(a).','Muito preparado(a).','Totalmente preparado(a).'))
