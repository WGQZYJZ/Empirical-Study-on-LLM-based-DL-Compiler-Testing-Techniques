import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3)
other = torch.randn(1, 3)
output_tensor = torch.Tensor.add_(input_tensor, other)