
# Functions
read_data <- function(path, sheet){
  readxl::read_xlsx(path = path, sheet = sheet, na = '-', skip = 3)
}

write_data <- function(data, path){
  write.csv2(x = data, file = path, row.names = FALSE, na = '')
}


# Read data
path_in <- "dados/bruto/Economatica-2009-2020.xlsx"
path_out <- "dados/processado/"

# Nomes planilhas
sheets <- readxl::excel_sheets(path_in)

# Carregando dados planilhas
data_ <- lapply(
  X = sheets,
  FUN = read_data,
  path = path_in
)

# Export data para csv 
paths_out <- paste(path_out, sheets, '.csv', sep = '')
mapply(
  FUN = write_data,
  data = data_,
  path = paths_out
)

