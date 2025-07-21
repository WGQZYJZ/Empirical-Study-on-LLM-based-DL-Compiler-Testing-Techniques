import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, requires_grad=True)
output = torch.sigmoid(input)
output.backward(torch.randn(1, 1))