import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10)
output_data = torch.fft.fftfreq(10)