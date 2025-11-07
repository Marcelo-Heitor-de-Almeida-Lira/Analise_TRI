library(dplyr)
library(htmlwidgets)
library(plotly)
library(glue)
library(jsonlite)

scatter_plot <- function(df, vetor_itens, valor1, examinando = "",titulo = "") {
  Scatter <- plot_ly(x = df$theta,
                     y = df[, vetor_itens[1] + 1],
                     name = names(df)[vetor_itens[1] + 1],
                     type = "scatter",
                     mode = "lines"
  ) %>% 
    layout(title = titulo,
           xaxis = list(title = 'Habilidade θ',
                        zeroline = FALSE
           ),
           yaxis = list(title = 'Probabilidade P(θ)',
                        zeroline = FALSE
           ))
  
  Scatter <- Scatter %>% add_annotations(
    x = valor1$theta,
    y = valor1$probabilidade,
    text = paste(examinando,"<br>Habilidade (θ):", round(valor1$theta, 2),
                 "<br>Probabilidade P(θ):", round(valor1$probabilidade, 2)*100,"%"),
    showarrow = TRUE,
    arrowhead = 7,
    arrowwidth = 2,
    ax = valor1$theta - 100,
    ay = -100, 
    arrowcolor="#636363",
    bordercolor="#c7c7c7",
    bgcolor="#2CA02C",
    font = list(color = "White", weight = "bold")
    
  )
  
  return(Scatter)
}

generate_CCI <- function(area_conhecimento, estado, item, dados_aluno) {
  theta <- seq(-5, 5, .0001)
  
  prob_path = glue("../codigos_R/LTM_3PL/probabilidades/df_prob_3PL_LTM_{area_conhecimento}_{estado}.csv")
  df_probabilidade <- read.table(prob_path, header = TRUE, sep = ",")
  
  cci <- scatter_plot(df_probabilidade, c(item), dados_aluno, "Examinando", "CCI")
  return(cci)
}

main <- function(matricula, theta, prob_acerto, area_conhecimento, estado, item) {
  dados_aluno <- data.frame(theta = theta, 
                            probabilidade = prob_acerto)
  
  cci <- generate_CCI(area_conhecimento, estado, item, dados_aluno)
  
  plot_path <- glue("plots/{matricula}_{estado}_{area_conhecimento}_{item}.html")
  
  saveWidget(cci, plot_path, selfcontained = TRUE)
}
