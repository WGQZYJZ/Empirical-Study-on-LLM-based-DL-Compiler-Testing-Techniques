import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(24)
input = input.view(2, 3, 4)
output = torch.roll(input, shifts=1, dims=1)