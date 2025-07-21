import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output_data = torch.fft.irfft2(input_data, s=None, dim=((- 2), (- 1)), norm=None)