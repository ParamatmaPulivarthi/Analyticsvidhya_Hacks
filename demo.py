#importing CSV,XLS and Tab files
import pandas as pd
def import_files(filename,extension):
    if extension=="csv":
        df=pd.read_csv(filename)
    elif extension=="xls":
        df=pd.read_excel(filename)
    elif extension=="tab":
        df=pd.read_csv(filename,sep='\t')
    print("----Top 5 Rows----",df.head(),
      "\n","-----Botom 5 Rows----",df.tail(),
     "\n","-----columns names----",df.columns)
    return df

