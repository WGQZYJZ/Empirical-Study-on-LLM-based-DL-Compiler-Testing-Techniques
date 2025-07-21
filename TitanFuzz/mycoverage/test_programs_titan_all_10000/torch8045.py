import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(start=0, end=16, dtype=torch.float).view(4, 4)
output_data = torch.vsplit(input_data, 2)