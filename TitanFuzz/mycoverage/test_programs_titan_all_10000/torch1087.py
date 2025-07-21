import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
divisor = torch.rand(4, 4)
remainder = torch.Tensor.remainder_(input_tensor, divisor)