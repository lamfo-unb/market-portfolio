
library(dplyr)
library(lubridate)

path_in <- 'resultados/AZUL4.csv'
dados <- data.table::fread(path_in, sep = ';', dec = ',', data.table = FALSE)

processada <- dados %>% 
  mutate(Data = lubridate::as_date(Data)) %>% 
  filter(year(Data) >= 2018)

colunas <- c(
  "data", "qtd_negociacoes", "qtd_titulos", "volume",
  "preco_fechamento", "preco_abertura", "preco_min", "preco_max",
  "preco_medio"
)

names(processada) <- colunas
