import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
vec1 = torch.randn(4)
vec2 = torch.randn(4)
output = torch.addr(input, vec1, vec2)