import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
dim = 0
result = torch.amin(input_data, dim)
dim = 1
result = torch.amin(input_data, dim)