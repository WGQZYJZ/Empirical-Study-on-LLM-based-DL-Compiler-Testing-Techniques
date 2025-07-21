import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 10)
other = torch.randn(10, 10)
output_tensor = torch.Tensor.eq_(input_tensor, other)