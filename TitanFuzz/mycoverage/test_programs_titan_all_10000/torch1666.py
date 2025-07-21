import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 10)
output_data = torch.atanh(input_data)