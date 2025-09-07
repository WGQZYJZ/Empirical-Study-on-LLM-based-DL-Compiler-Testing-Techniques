import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 5)
fft_input = torch.fft.rfft2(input)