import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 4)
output = torch.fft.ihfft(input_data)