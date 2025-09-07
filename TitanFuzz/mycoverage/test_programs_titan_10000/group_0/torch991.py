import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(1, 3)
output_data = torch.arctanh(input_data)
output_data = torch.arctanh_(input_data)