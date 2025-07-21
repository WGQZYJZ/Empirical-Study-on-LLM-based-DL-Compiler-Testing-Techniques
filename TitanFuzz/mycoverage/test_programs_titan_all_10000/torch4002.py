import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5, 6)
output = torch.fft.ifft2(input)