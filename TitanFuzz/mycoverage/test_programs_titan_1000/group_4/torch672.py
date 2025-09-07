import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(8, 8)
output_tensor = torch.Tensor.arccosh_(input_tensor)