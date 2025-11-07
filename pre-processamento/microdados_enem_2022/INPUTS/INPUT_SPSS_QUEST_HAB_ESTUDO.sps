/*****************************************************************************************************/
/*  INEP/Daeb-Diretoria de Avaliação da Educação Básica                                          */ 
/*                                   			                                    */
/*  Coordenação-Geral de Medidas da Educação Básica (CGMEB)		*/
/*----------------------------------------------------------------------------------------------------------------------------*/
/*  PROGRAMA:                                                                                                      */
/*           INPUT_SPSS_QUEST_HAB_ESTUDO                                                 	*/
/*----------------------------------------------------------------------------------------------------------------------------*/
/*  DESCRICAO: PROGRAMA PARA LEITURA DA BASE DE QUESTIONÁRIOS        */
/*                       SOBRE HÁBITOS DE ESTUDO NA PANDEMIA, QUE COMPÕE      */
/*                       OS MICRODADOSDO ENEM DE 2022       			*/ 
/*****************************************************************************************************/
/* Obs:                                                                                                                    */
/* 		                                                                                           */
/* Para abrir a base dos questionários é necessário salvar este programa e o arquivo     */
/* QUEST_HAB_ESTUDO.csv no diretório C:\ do computador.	                  	*/
/*							 */ 
/*							 */
/* Para a leitura dA base dos questionários é necessário a seleção do programa abaixo,*/
/* depois execute-o.						 */
/*							 */ 
/******************************************************************************************************/
/*                                                   ATENÇÃO                                                          */ 
/******************************************************************************************************/
/* Este programa abre a base de dados com os rótulos das variáveis de	                    */
/* acordo com o dicionário de dados que compõem os microdados. Para abrir                */
/* os dados sem os rótulos basta importar diretamente no SPSS.		  */
/* 							   */
/*******************************************************************************************************/

GET DATA
  /TYPE=TXT
  /FILE="C:\QUEST_HAB_ESTUDO.csv" /*local do arquivo*/
  /DELCASE=LINE
  /DELIMITERS=";"
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /IMPORTCASE= ALL
  /VARIABLES=
  NU_INSCRICAO F21.0
  TP_RESPOSTA F1.0
  Q001 A1    
  Q002 A1    
  Q003 A1    
  Q004 A1    
  Q005 A1    
  Q006 A1    
  Q007 A1    
  Q008 A1    
  Q009 A1    
  Q010 A1    
  Q011 A1    
  Q012 A1    
  Q013 A1    
  Q014 A1    
  Q015 A1    
  Q016 A1   
  Q017 A1    
  Q018 A1    
  Q019 A1    
  Q020 A1    
  Q021 A1    
  Q022 A1    
  Q023 A1   
  Q024 A1   
  Q025A A1   
  Q025B A1   
  Q025C A1   
  Q025D A1   
  Q025E A1   
  Q025F A1   
  Q026A A1   
  Q026B A1  
  Q026C A1   
  Q026D A1   
  Q026E A1   
  Q026F A1   
  Q026G A1   
  Q026H A1   
  Q027  A1   
  Q028A A1   
  Q028B A1   
  Q028C A1  
  Q028D A1   
  Q028E A1   
  Q028F A1   
  Q028G A1   
  Q028H A1   
  Q028I  A1  
  Q028J A1   
  Q028K A1   
  Q028L A1   
  Q028M A1   
  Q028N A1   
  Q028O A1   
  Q028P A1   
  Q028Q A1   
  Q028R A1   
  Q029  A1   
  Q030A A1   
  Q030B A1   
  Q030C A1   
  Q030D A1  
  Q030E A1   
  Q030F A1   
  Q030G A1   
  Q031  A1   
  Q032A A1   
  Q032B A1   
  Q032C A1   
  Q032D A1   
  Q032E A1   
  Q032F A1   
  Q032G A1   
  Q033A A1   
  Q033B A1   
  Q033C A1  
  Q033D A1   
  Q033E A1   
  Q033F A1  
  Q033G A1   
  Q033H A1   
  Q033I  A1  
  Q033J A1   
  Q034  A1.
CACHE.
EXECUTE.
DATASET NAME QUEST_HAB_ESTUDO WINDOW=FRONT.

VARIABLE LABELS
NU_INSCRICAO			"Número de inscrição"
TP_RESPOSTA  			"Tipo de opção de resposta ao questionário"
Q001  				"Considerando a etapa de Ensino Médio, qual dessas situações está de acordo com o seu vínculo escolar durante a pandemia?"
Q002  				"Considerando a continuidade do vínculo escolar na pandemia, qual dessas situações está de acordo com sua realidade?"
Q003   				"Considerando o ano de 2021 (o segundo ano da pandemia), qual dessas situações está de acordo com sua experiência?"
Q004   				"Como você percebe o seu processo de aprendizagem durante a pandemia?"
Q005   				"Frequência de atividades de estudo no segundo ano da pandemia: Organizei cronograma de estudos com tempos mais longos e mais curtos para estudar de acordo com a dificuldade das matérias."
Q006   				"Frequência de atividades de estudo no segundo ano da pandemia: Reservei tempos mais longos e mais curtos para estudar de acordo com a dificuldade das matérias."
Q007   				"Frequência de atividades de estudo no segundo ano da pandemia: Organizei material para ser estudado."
Q008   				"Frequência de atividades de estudo no segundo ano da pandemia: Eu me dediquei aos horários programados de estudo de acordo com a dificuldade das matérias."
Q009   				"Frequência de atividades de estudo no segundo ano da pandemia: Li os textos indicados em cada matéria antes de assistir as aulas ou videoaulas sobre o assunto dos textos."
Q010   				"Frequência de atividades de estudo no segundo ano da pandemia: Resumi os textos das matérias, destacando as partes mais importantes."
Q011   				"Frequência de atividades de estudo no segundo ano da pandemia: Resumi as videoaulas ou os podcasts, destacando as partes mais importantes."
Q012   				"Frequência de atividades de estudo no segundo ano da pandemia: Fiz as atividades das matérias para fixação de conteúdo."
Q013   				"Frequência de atividades de estudo no segundo ano da pandemia: Fiz atividades avaliativas, inclusive simulados, para verificar o quanto aprendi durante a pandemia."
Q014   				"Frequência de atividades de estudo no segundo ano da pandemia: Aproveitei o tempo das aulas online ou atividades de reforço, sem desperdiçá-lo com distrações."
Q015   				"Frequência de atividades de estudo no segundo ano da pandemia: Anotei as explicações obtidas em videoaulas ou podcasts das matérias."
Q016  				"Frequência de atividades de estudo no segundo ano da pandemia: Anotei as informações que obtive ao assistir vídeos complementares de assuntos do meu interesse."
Q017   				"Frequência de atividades de estudo no segundo ano da pandemia: Destaquei as dúvidas que tive ao ler os textos das disciplinas para esclarecer com os professores."
Q018   				"Frequência de atividades de estudo no segundo ano da pandemia: Estruturei as principais ideias para produzir redações."
Q019  				"Frequência de atividades de estudo no segundo ano da pandemia: Treinei redação."
Q020   				"Frequência de atividades de estudo no segundo ano da pandemia: Participei de fóruns de discussão por matéria para tirar dúvidas."
Q021   				"Frequência de atividades de estudo no segundo ano da pandemia: Entrei nas aulas online por videoconferência sem atraso da minha parte."
Q022  				"Frequência de atividades de estudo no segundo ano da pandemia: Assisti todas as aulas online nas datas programadas para estudo."
Q023   				"Frequência de atividades de estudo no segundo ano da pandemia: Revisei as anotações das aulas, os resumos e anotações dos demais materiais que li ou assisti."
Q024   				"Frequência de atividades de estudo no segundo ano da pandemia: Reassisti as videoaulas e os podcasts das matérias."
Q025A  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Aparelho de rádio."
Q025B  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Computador/notebook."
Q025C  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Livros/apostilas/materiais impressos."
Q025D  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Tablet."
Q025E  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Telefone celular."
Q025F  				"Qual meio você MAIS utilizou para estudar ou para manter-se informado(a)? Televisão."
Q026A  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Audioaula/podcast avulsos."
Q026B  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Audioaula/podcast em plataforma de educação a distância."
Q026C  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Grupos de Whatsapp, Facebook, Telegram e similares."
Q026D  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Livros/apostilas/materiais digitais."
Q026E  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Programa de rádio."
Q026F  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Programa de TV."
Q026G  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Videoaula avulsa."
Q026H  				"Qual ou quais tipo(s) de acesso remoto você MAIS utilizou para estudar ou para manter-se informado(a)? Videoaula em plataforma de educação a distância."
Q027   				"Você vivenciou problemas em sua rotina para estudar ou manter-se informado(a) durante a pandemia?"
Q028A  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: eu me senti desestimulado(a) por não ter colegas com quem interagir sobre o que eu estava estudando."
Q028B  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: tive dificuldade de compreender os conteúdos por falta de explicações de um professor em tempo real."
Q028C  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: fiquei por muito tempo diante das telas, sem pequenos intervalos para descansar."
Q028D  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: reduzi a prática de atividades físicas."
Q028E  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: dormi por menos tempo."
Q028F  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: tive episódios de insônia."
Q028G  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: senti dificuldade em manter a motivação para estudar por minha conta."
Q028H  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: senti dificuldade em me motivar a cumprir meu cronograma."
Q028I  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: senti medo de não conseguir aprender os conteúdos."
Q028J  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: senti ansiedade devido ao isolamento social e ao receio de contágio da doença."
Q028K  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: dediquei tempo para ajudar algum familiar a estudar em casa."
Q028L  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: precisei ficar em repouso porque tive Covid com sintomas."
Q028M  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: precisei ficar em repouso porque tive outra doença."
Q028N  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: precisei cuidar de algum familiar que teve Covid com sintomas."
Q028O  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: precisei cuidar de algum familiar que teve outra doença."
Q028P  				"Em 2021, eu não consgui me dedicar aos estudos ou manter-me informado(a) porque: tive que cuidar do(s) meu(s) irmão(s) menor(es) para meus pais trabalharem."
Q028Q  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: tive que começar a trabalhar em casa para obter renda."
Q028R  				"Em 2021, eu não consegui me dedicar aos estudos ou manter-me informado(a) porque: tive que trabalhar em serviço considerado essencial durante a pandemia."
Q029   				"Você teve dificuldades de infraestrutura para estudar ou manter-se informado(a) durante 2021?"
Q030A  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Equipamento (computador pessoal ou notebook) pouco disponível por ser compartilhado com outros familiares."
Q030B  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Conexão ruim ou limitada com a internet."
Q030C  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Equipamento (computador pessoal ou notebook) com configuração insuficiente para estudar ou acessar materiais"
Q030D  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Material pedagógico insuficiente para estudar, faltando livros, apostilas, textos, vídeos."
Q030E  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Local de estudos faltando boa iluminação, higiene, ventilação e silêncio."
Q030F  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Local de estudos sem mobília para guardar e para dispor os materiais de estudo."
Q030G  				"PRINCIPAIS dificuldades de infraestrutura que você teve para estudar ou manter-se informado(a) durante 2021: Recursos insuficientes para alimentação."
Q031   				"Você precisou da ajuda de alguém para estudar ou manter-se informado(a) em 2021?"
Q032A  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Amigo(s)/colega(s)/conhecido(s)."
Q032B  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Filho(s)/sobrinho(s)."
Q032C  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Irmão(s)/primo(s)."
Q032D 				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Namorado(a)/cônjuge/companheiro(a)."
Q032E  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Pai/mãe."
Q032F  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Professor(a) / orientador(a)."
Q032G  				"Quem ajudou você com mais frequência a estudar ou manter-se informado(a) em 2021? Tio(s)/Avô,avó."
Q033A  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Com a alimentação."
Q033B  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para acessar à internet."
Q033C  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para comprar livros/apostilas ou fazer cópias."
Q033D  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para comprar cursos online."
Q033E  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Financeira para me inscrever em provas ou no Enem."
Q033F  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para elaborar um cronograma de estudos."
Q033G  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para pesquisar materiais na internet."
Q033H  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Para preencher formulários de inscrição."
Q033I  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Por meio de empréstimo de algum equipamento (celular, computador, notebook, tablet) para eu estudar."
Q033J  				"Que tipo de ajuda você recebeu com mais frequência para estudar ou manter-se informado(a) em 2021? Por meio de explicação de conteúdos que eu não havia entendido."
Q034   				"A partir da sua experiência de estudos em 2021, o quanto você se sente preparado(a) para conduzir o seu processo de aprendizagem?".

VALUE LABELS
/VALUE TP_RESPOSTA
	0	"Não (Participante optou por não responder o questionário)."
	1	"Sim (Participante optou por responder o questionário)."
	2	"Responder Depois"
/Q001 
	"A"	"Eu estive matriculado(a) no Ensino Médio regular."
	"B"	"Eu estive matriculado(a) no Ensino Médio, em turma de EJA."
	"C"	"Eu estive matriculado(a) no Ensino Médio integrado à Educação Profissional."
	"D"	"Eu concluí o Ensino Médio antes de 2021."
	"E"	"Eu não concluí o Ensino Médio e nem estive matriculado(a) nesse período."
/Q002 
	"A"	"Eu continuei os estudos sem interromper o ano letivo."
	"B"	"Eu decidi interromper os estudos no primeiro ano da pandemia, mas me rematriculei em 2021."
	"C"	"Eu fui levado a interromper os estudos no primeiro ano da pandemia por não ter recebido suporte da escola, mas me rematriculei em 2021."
/Q003 
	"A"	"Eu apenas tive aulas presenciais nesse período."
	"B"	"Eu apenas estudei em casa de forma remota nesse período."
	"C"	"Eu estudei de forma híbrida, ou seja, em casa remotamente e em aulas presenciais."
	"D"	"Eu realizei atividades de estudo diversas, mas sem estar matriculado(a) no Ensino Médio."
	"E"	"Eu não estive matriculado(a) regularmente, nem realizei atividades de estudo."
/Q004 
	"A"	"Eu aprendi mais no ensino remoto (estudando somente em casa)."
	"B"	"Eu aprendi mais estudando de forma híbrida."
	"C"	"Eu aprendi mais estudando de forma presencial."
	"D"	"Eu aprendi no ensino remoto ou híbrido na mesma medida de quando eu estava no ensino presencial."
	"E"	"Eu não estive matriculado(a) em 2021, mas aprendi estudando por conta própria."
	"F"	"Eu não estive matriculado(a) em 2021 e nem estudei."
/Q005 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q006 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q007 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q008 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q009 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q010 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q011 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q012 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q013 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q014 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q015 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q016 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q017 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q018 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q019 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q020 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q021 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q022 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q023 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q024 
	"A"	"Nenhuma vez."
	"B"	"Poucas vezes."
	"C"	"Muitas vezes."
	"D"	"Em todas as vezes."
/Q025A 
	"A"	"Sim."
	"B"	"Não."
/Q025B 
	"A"	"Sim."
	"B"	"Não."
/Q025C 
	"A"	"Sim."
	"B"	"Não."
/Q025D 
	"A"	"Sim."
	"B"	"Não."
/Q025E 
	"A"	"Sim."
	"B"	"Não."
/Q025F 
	"A"	"Sim."
	"B"	"Não."
/Q026A 
	"A"	"Sim."
	"B"	"Não."
/Q026B 
	"A"	"Sim."
	"B"	"Não."
/Q026C 
	"A"	"Sim."
	"B"	"Não."
/Q026D 
	"A"	"Sim."
	"B"	"Não."
/Q026E 
	"A"	"Sim."
	"B"	"Não."
/Q026F 
	"A"	"Sim."
	"B"	"Não."
/Q026G 
	"A"	"Sim."
	"B"	"Não."
/Q026H 
	"A"	"Sim."
	"B"	"Não."
/Q027 
	"A"	"Sim."
	"B"	"Não."
/Q028A 
	"A"	"Sim."
	"B"	"Não."
/Q028B
	"A"	"Sim."
	"B"	"Não."
/Q028C 
	"A"	"Sim."
	"B"	"Não."
/Q028D 
	"A"	"Sim."
	"B"	"Não."
/Q028E 
	"A"	"Sim."
	"B"	"Não."
/Q028F 
	"A"	"Sim."
	"B"	"Não."
/Q028G 
	"A"	"Sim."
	"B"	"Não."
/Q028H 
	"A"	"Sim."
	"B"	"Não."
/Q028I 
	"A"	"Sim."
	"B"	"Não."
/Q028J 
	"A"	"Sim."
	"B"	"Não."
/Q028K 
	"A"	"Sim."
	"B"	"Não."
/Q028L 
	"A"	"Sim."
	"B"	"Não."
/Q028M 
	"A"	"Sim."
	"B"	"Não."
/Q028N 
	"A"	"Sim."
	"B"	"Não."
/Q028O 
	"A"	"Sim."
	"B"	"Não."
/Q028P 
	"A"	"Sim."
	"B"	"Não."
/Q028Q 
	"A"	"Sim."
	"B"	"Não."
/Q028R 
	"A"	"Sim."
	"B"	"Não."
/Q029 
	"A"	"Sim."
	"B"	"Não."
/Q030A 
	"A"	"Sim."
	"B"	"Não."
/Q030B 
	"A"	"Sim."
	"B"	"Não."
/Q030C 
	"A"	"Sim."
	"B"	"Não."
/Q030D 
	"A"	"Sim."
	"B"	"Não."
/Q030E 
	"A"	"Sim."
	"B"	"Não."
/Q030F 
	"A"	"Sim."
	"B"	"Não."
/Q030G 
	"A"	"Sim."
	"B"	"Não."
/Q031 
	"A"	"Sim."
	"B"	"Não."
	"C"	"Precisei de ajuda para estudar, mas não tive ninguém para me auxiliar."
/Q032A 
	"A"	"Sim."
	"B"	"Não."
/Q032B 
	"A"	"Sim."
	"B"	"Não."
/Q032C 
	"A"	"Sim."
	"B"	"Não."
/Q032D 
	"A"	"Sim."
	"B"	"Não."
/Q032E 
	"A"	"Sim."
	"B"	"Não."
/Q032F 
	"A"	"Sim."
	"B"	"Não."
/Q032G 
	"A"	"Sim."
	"B"	"Não."
/Q033A 
	"A"	"Sim."
	"B"	"Não."
/Q033B 
	"A"	"Sim."
	"B"	"Não."
/Q033C 
	"A"	"Sim."
	"B"	"Não."
/Q033D 
	"A"	"Sim."
	"B"	"Não."
/Q033E 
	"A"	"Sim."
	"B"	"Não."
/Q033F 
	"A"	"Sim."
	"B"	"Não."
/Q033G 
	"A"	"Sim."
	"B"	"Não."
/Q033H 
	"A"	"Sim."
	"B"	"Não."
/Q033I 
	"A"	"Sim."
	"B"	"Não."
/Q033J 
	"A"	"Sim."
	"B"	"Não."
/Q034
	"A"	"Nada preparado(a)."
	"B"	"Um pouco preparado(a)."
	"C"	"Bem preparado(a)."
	"D"	"Muito preparado(a)."
	"E"	"Totalmente preparado(a).".