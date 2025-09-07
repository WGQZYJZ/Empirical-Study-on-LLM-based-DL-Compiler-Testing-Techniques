import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, requires_grad=True)
other = torch.randn(3, 4, requires_grad=True)
result = torch.matmul(input, other)