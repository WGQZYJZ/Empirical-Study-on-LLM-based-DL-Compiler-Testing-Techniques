import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
dim = 0
output = torch.amin(input, dim)
dim = 1
output = torch.amin(input, dim)