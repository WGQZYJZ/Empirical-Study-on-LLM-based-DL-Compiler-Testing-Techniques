import torch
from torch import nn
from torch.autograd import Variable

_input_tensor = torch.rand(10, 10)
output = torch.Tensor.ldexp(_input_tensor, 2)