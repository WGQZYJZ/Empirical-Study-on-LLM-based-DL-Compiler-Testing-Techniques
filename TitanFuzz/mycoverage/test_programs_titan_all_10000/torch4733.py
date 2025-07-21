import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(start=0, end=16, dtype=torch.float32).view(4, 4)
output = torch.vsplit(input_data, 2)