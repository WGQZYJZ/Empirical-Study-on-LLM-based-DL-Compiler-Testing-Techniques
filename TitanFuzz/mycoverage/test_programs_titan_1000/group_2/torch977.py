import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
tensor_split = torch.tensor_split(input_data, 5, dim=0)
for i in range(len(tensor_split)):
    print(tensor_split[i])