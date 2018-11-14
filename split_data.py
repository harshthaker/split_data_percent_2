import os
from shutil import copyfile
import argparse
import pandas as pd
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
parser.add_argument("path_to_csv")
args=parser.parse_args()


    
def gen_sample_data(input,output,label_data_path):
  
  files = os.listdir(input)
  data_dir = ['train','validation','test'] #array storing train, validation names
  data = pd.read_csv(label_data_path)
  
  train_size = 0.7 * len(data)
  val_size = 0.15 * len(data)
   
  #create folders with similar class names for both train and validation in output dir
  for dir_name in data_dir:
      output_path = os.path.join(output,dir_name)
      if not os.path.exists(output_path):
          os.makedirs(output_path)
  
  for i in tqdm(range(0,train_size)):
    input_path = os.path.join(input,data['Id'][i]+".png")
    output_path = os.path.join(output+"/train",data['Id'][i]+".png")
    copyfile(input_path,output_path)
  
  for i in tqdm(range(train_size,val_size)):
    input_path = os.path.join(input,data['Id'][i]+".png")
    output_path = os.path.join(output+"/validation",data['Id'][i]+".png")
    copyfile(input_path,output_path)
    
  for i in tqdm(range(train_size+val_size,len(data))):
    input_path = os.path.join(input,data['Id'][i]+".png")
    output_path = os.path.join(output+"/test",data['Id'][i]+".png")
    copyfile(input_path,output_path)


gen_sample_data(args.input,args.output,args.path_to_csv)
          
