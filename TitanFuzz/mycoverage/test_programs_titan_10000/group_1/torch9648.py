import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.randn(4, 3)
other = torch.randn(3)
output_tensor = torch.Tensor.inner(input_tensor, other)