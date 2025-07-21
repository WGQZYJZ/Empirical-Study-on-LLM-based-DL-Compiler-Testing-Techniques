import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, 20)
other = torch.randn(10, 20)
output_tensor = torch.Tensor.minimum(input_tensor, other)