import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 3)
output = torch.chunk(input, 3, dim=1)
output = torch.chunk(input, 2, dim=0)