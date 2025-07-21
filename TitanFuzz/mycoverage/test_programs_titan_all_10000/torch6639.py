import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, requires_grad=True)
other = torch.randn(1, 3)
output_tensor = torch.Tensor.ge_(input_tensor, other)