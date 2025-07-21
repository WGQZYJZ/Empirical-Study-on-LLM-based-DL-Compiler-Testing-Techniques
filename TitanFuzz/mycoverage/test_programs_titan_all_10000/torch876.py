import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
output = torch.float_power(input_data, 3)