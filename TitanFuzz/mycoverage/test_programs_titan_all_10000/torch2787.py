import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.arccosh_(input_tensor)