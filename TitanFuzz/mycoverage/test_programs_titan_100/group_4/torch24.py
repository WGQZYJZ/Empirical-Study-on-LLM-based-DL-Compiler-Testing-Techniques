import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 9).view(2, 4)
output = torch.diagonal(input, offset=0, dim1=0, dim2=1)