import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
other = 2
torch.Tensor.ldexp_(input_tensor, other)