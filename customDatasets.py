from torch.utils.data import Dataset
import torch

class MyDataset(Dataset):
  def __init__(self,df):
    x=df.iloc[:,0:-1].values
    y=df.iloc[:,-1].values.tolist()
    y=[int(i) for i in y]
 
    self.x_train=torch.tensor(x,dtype=torch.float32)
    self.y_train=torch.tensor(y,dtype=torch.float32)
 
  def __len__(self):
    return len(self.y_train)

  def __getitem__(self,idx):
    return self.x_train[idx],self.y_train[idx]
	
class MyDatasetCompress(Dataset):
  def __init__(self,df):
    x=transform(df.iloc[:,:-1].values)
    y=df.iloc[:,-1].values.tolist()
    y=[int(i) for i in y]
 
    self.x_train=torch.tensor(x,dtype=torch.float32)
    self.y_train=torch.tensor(y,dtype=torch.float32)
 
  def __len__(self):
    return len(self.y_train)

  def __getitem__(self,idx):
    return self.x_train[idx],self.y_train[idx]
