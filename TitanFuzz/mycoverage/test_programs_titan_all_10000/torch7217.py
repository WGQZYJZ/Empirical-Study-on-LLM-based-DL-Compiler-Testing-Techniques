import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 5)
torch.nn.Hardshrink(lambd=0.5)
input_data = torch.rand(2, 3, 5)
torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0, inplace=False)