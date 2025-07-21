import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4, 4)
output = torch.fft.irfft2(input_data)