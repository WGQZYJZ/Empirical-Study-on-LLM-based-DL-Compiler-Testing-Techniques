import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 4, 4)
output_data = torch.fft.ihfft(input_data)