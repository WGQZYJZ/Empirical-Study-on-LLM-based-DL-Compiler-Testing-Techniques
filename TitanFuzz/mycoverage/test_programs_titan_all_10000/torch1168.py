import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 4, dtype=torch.float32)
output = torch.fft.ifft(input)