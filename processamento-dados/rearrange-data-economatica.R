
# Functions
read_data <- function(path, sheet){
  readxl::read_xlsx(path = path, sheet = sheet, na = '-', skip = 3)
}


write_data <- function(data, path){
  write.csv2(x = data, file = path, row.names = FALSE, na = '')
}


# Read data
path_in <- "dados/Economatica-2009-2020.xlsx"
sheets <- readxl::excel_sheets(path_in)

data_ <- lapply(
  X = sheets,
  FUN = read_data,
  path = path_in
)

# Export data 
paths_out <- paste('resultados/', sheets, '.csv', sep = '')
mapply(
  FUN = write_data,
  data = data_,
  path = paths_out
)

