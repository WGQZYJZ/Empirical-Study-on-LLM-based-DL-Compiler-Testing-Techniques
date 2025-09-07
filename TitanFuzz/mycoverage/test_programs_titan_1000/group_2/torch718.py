import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3, 4, 5)
output = torch.fft.ifftshift(input, dim=None)