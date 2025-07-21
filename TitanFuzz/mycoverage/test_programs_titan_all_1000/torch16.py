import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4)
output = torch.fft.ihfft(input, 1, (- 1))