import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
result = torch.fft.rfft2(input_data, s=None, dim=((- 2), (- 1)), norm=None)