import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, 4)
input = Variable(input, requires_grad=True)
output = torch.fft.irfftn(input)
output.backward(torch.randn(output.size()))