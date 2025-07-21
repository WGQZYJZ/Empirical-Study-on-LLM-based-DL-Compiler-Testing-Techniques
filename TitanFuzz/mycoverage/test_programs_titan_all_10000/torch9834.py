import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 4, 4, 4)
pad = torch.nn.ConstantPad3d((1, 2, 3, 4, 5, 6), 0)
output = pad(input_data)
input_data = torch.randn(1, 1, 4)
pad = torch.nn.ConstantPad1d((1, 2), 0)
output = pad(input_data)