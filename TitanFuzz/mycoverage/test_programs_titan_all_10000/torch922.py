import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
size = (2, 2)
stride = (2, 2)
output = torch.as_strided(input, size, stride)