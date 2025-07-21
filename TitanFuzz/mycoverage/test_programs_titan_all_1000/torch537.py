import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 3)
output = torch.diagonal(input, offset=0, dim1=0, dim2=1)