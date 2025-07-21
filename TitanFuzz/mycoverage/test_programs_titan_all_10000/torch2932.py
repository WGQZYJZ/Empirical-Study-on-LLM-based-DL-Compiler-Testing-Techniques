import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(10, 5, 4)
output = torch.fft.ifftshift(input, dim=None)