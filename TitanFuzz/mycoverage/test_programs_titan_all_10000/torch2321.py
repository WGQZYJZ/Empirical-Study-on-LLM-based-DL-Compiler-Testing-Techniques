import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
output = torch.Tensor.ne_(input_tensor, other)