import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dim = 1
index = torch.tensor([[1, 1], [0, 2]])
output = torch.gather(input, dim, index)