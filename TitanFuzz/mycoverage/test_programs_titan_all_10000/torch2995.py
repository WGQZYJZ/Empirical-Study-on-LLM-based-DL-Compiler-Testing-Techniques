import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 2, 4, 4)
output_data = torch.fft.fft2(input_data)
input_data = torch.rand(1, 2, 4, 4)
output_data = torch.fft.fftn(input_data)