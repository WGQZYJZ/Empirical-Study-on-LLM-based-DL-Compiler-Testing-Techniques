import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4, 5)
other = torch.randn(2, 3, 4, 5)
torch.Tensor.igammac_(input_tensor, other)