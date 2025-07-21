import torch
from torch import nn
from torch.autograd import Variable
inp = torch.randn(2, 3, 4, 5)
out = torch.fft.rfft2(inp)