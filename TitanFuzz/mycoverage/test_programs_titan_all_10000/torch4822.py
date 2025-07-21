import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10)
output = torch.arccosh(input_data)