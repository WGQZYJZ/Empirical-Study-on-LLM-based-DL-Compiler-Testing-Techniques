import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, dtype=torch.float)
output = torch.fft.rfft2(input)