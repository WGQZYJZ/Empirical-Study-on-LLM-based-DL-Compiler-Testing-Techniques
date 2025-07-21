import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.cumsum_(input_tensor, dim=1, dtype=None)