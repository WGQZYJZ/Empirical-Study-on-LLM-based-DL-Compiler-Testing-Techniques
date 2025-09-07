import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 3, requires_grad=True)
output = torch.rsqrt(input)