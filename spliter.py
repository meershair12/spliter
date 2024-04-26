import pandas as pd
from colorama import Fore
import argparse
# read text file into pandas DataFrame


print(Fore.RED+"--------------------------------------------------------")
print("////////////////////////////////////////////////////////")
print("")
print("--               SPLITER TEXT PARSER                 --\n")
print("////////////////////////////////////////////////////////")
print("--------------------------------------------------------")
print("------------- Developed by Shair Muhammad --------------")
print("--------------------------------------------------------")
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='path', type=str, help='i.e: /root/meershair/file.txt')
parser.add_argument('-d', dest='dest', type=str, help='i.e /root/result/output')
args = parser.parse_args()
file_path = args.path
result = args.dest
if args.path is None:
    file_path = input(Fore.WHITE+"Enter path of your file here: ")
if args.dest is None:
    result = input(Fore.WHITE+"Enter name of output file: ")
df = pd.read_csv(file_path, sep=" ")
print(Fore.GREEN+f"Your Uploaded File is {args.path}")
print(f"Output file is {args.dest}.xlsx")
# da

df = pd.DataFrame(df.columns, columns=["File"])
# 
df.to_excel(f"{result}.xlsx", index=False)

print(Fore.BLUE+"Your file has been parsed and split")
