import pandas as pd
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("column_idx", help="column index for sorting")
parser.add_argument("data_path", help="data")
args = parser.parse_args()
#print("positional arg:", type(args.column_idx), type(args.data_path))

data = pd.read_csv(args.data_path, header=None, sep=' ').dropna(axis=1)
data.columns = data.columns-1

column_idx = int(args.column_idx)
s = data[column_idx].round(3).sort_values(ascending=True)
#s.to_csv('ans1.txt', index=False)
#print(str(s.tolist())[1:-1])

# write to file 
out_filename = 'ans1.txt' 
with open(out_filename, 'a') as out_file:
  out_file.write(str(s.tolist())[1:-1])

