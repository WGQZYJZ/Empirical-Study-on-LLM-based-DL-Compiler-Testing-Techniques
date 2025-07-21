import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3, 2)
fft_result = torch.fft.fft(input)