import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 5)
output_tensor = torch.Tensor.acosh_(input_tensor)
input_tensor = torch.randn(1, 3, 5)
output_tensor = torch.Tensor.asinh_(input_tensor)