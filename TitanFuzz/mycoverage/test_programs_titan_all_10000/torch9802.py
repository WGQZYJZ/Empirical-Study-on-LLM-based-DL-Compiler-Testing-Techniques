import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(100)
output = torch.fft.rfftfreq(input_data.size(0), d=1)