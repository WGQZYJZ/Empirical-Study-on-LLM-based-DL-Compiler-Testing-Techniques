import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
output = torch.fft.ifftshift(input)
output = torch.fft.ifftshift(input, dim=0)
output = torch.fft.ifftshift(input, dim=1)