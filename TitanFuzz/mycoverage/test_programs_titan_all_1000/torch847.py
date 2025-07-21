import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 9, dtype=torch.float).view(1, 1, 8)
pad = torch.nn.ReflectionPad1d(padding=2)
output = pad(input_data)