import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
k = 1
dims = (2, 3)
output = torch.rot90(input, k, dims)