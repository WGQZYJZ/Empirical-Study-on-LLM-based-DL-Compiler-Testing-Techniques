import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.index_select(input=input_data, dim=0, index=torch.tensor([0, 2]))