import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 10)
index = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
src = torch.randn(10, 1)
output = torch.scatter_add(input, 0, index.unsqueeze(1), src)