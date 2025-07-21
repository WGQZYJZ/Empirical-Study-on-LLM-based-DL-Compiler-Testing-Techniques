import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(5, 5)
other = torch.rand(5, 5)
output_tensor = torch.Tensor.copysign_(input_tensor, other)