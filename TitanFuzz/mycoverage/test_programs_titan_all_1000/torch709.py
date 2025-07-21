import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 2, 3, 4)
output_data = torch.fft.rfft2(input_data)