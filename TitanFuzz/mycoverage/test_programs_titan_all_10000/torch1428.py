import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 4)
output_data = torch.arccosh(input_data)
torch.arccosh_(input_data)