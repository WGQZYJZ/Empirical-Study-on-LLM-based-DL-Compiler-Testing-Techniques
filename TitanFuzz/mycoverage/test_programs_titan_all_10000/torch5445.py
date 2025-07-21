import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, requires_grad=True)
output = torch.square(input)