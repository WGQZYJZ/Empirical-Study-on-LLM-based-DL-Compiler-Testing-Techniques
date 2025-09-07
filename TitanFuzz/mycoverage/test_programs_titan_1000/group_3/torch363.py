import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(0, 20)
input = input.view(5, 4)
size = (4, 4)
stride = (4, 1)
output = torch.as_strided(input, size, stride)