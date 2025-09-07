import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20)
output = torch.chunk(input, 4)