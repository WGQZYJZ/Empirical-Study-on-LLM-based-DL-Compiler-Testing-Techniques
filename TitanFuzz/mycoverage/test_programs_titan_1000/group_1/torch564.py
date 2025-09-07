import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4, 5)
torch.fft.fftn(input_data)