import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 4, 5)
output = torch.Tensor.arccos_(input_data)