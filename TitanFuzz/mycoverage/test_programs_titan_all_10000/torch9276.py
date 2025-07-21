import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, requires_grad=True)
output = torch.log1p(input)