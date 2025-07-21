import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(8)
output_data = torch.Tensor.arccosh_(input_data)