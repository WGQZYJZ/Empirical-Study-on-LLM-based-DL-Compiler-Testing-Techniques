import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.roll(input, shifts=2, dims=1)
input = torch.randn(4, 4)
output = torch.roll(input, shifts=2, dims=1)
input = torch.randn(4, 4)
output = torch.roll(input, shifts=2, dims=1)