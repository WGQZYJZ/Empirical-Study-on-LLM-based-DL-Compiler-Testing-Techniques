import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 2)
other = torch.rand(3, 2)
output_tensor = torch.Tensor.hypot_(input_tensor, other)