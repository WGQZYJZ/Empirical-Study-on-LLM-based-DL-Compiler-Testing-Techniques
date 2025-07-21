import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 2, 4, 4)
output = torch.fft.fftshift(input_data, dim=2)