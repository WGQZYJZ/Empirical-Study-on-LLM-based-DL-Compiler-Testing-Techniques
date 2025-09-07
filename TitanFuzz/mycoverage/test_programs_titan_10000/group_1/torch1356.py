import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
output = torch.addr(input, vec1, vec2)