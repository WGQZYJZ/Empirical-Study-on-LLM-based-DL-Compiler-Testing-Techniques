import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, 4)
output = torch.fft.rfft(input_data)
output = torch.fft.rfft(input_data, 2)
output = torch.fft.rfft(input_data, 2, 1)
output = torch.fft.rfft(input_data, 2, 1, norm='ortho')