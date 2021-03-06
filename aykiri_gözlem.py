import pandas as pd
import seaborn as sns
df = pd.read_csv('diamond.csv')
df = df.select_dtypes(include=['float64','int64']) #sadece numeric degerler secildi
df=df.dropna()
df.head()
df_table= df["table"]
sns.boxplot(x=df["table"])
Q1= df_table.quantile(0.25) 
Q3= df_table.quantile(0.75) 
IQR = Q3-Q1
alt_sinir = Q1-1.5*IQR
ust_sinir = Q1+1.5*IQR
aykiri_tf = df_table <alt_sinir
df_table[aykiri_tf]
df_table[aykiri_tf].index #aykiri degerin indexine ulasildi
