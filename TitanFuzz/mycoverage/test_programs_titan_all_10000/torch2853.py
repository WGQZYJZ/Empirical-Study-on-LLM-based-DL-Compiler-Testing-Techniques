import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(10, dtype=torch.float64)
other = torch.randn(10, dtype=torch.float64)
torch.Tensor.gcd_(input_tensor, other)