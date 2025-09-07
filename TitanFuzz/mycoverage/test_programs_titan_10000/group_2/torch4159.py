import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 5)
output = torch.fft.fftfreq(input_data.shape[(- 1)])