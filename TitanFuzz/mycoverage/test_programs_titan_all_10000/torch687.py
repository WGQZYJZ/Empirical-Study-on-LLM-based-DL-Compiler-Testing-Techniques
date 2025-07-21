import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
output = torch.fft.fftfreq(input_data.shape[(- 1)], d=1.0)
input_data = torch.randn(4, 4)