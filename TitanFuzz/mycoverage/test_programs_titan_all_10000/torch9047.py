import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
other_data = torch.randn(10, 10)
output = torch.floor_divide(input_data, other_data)