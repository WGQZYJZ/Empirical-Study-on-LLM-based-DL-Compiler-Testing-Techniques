import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 2, requires_grad=True)
output = torch.matrix_power(input, 2)