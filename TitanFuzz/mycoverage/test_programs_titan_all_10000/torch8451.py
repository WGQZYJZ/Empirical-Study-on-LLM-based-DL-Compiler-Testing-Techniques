import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 2, 3, 4)
torch.fft.irfft(input_data)