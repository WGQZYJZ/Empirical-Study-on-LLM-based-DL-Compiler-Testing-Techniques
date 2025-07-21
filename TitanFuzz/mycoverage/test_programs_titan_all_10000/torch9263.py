import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 10)
output = torch.atanh(input_data)