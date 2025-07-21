import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4, 5)
output = torch.swapdims(input, dim0=1, dim1=2)
output = torch.swapdims(input, dim0=0, dim1=2)