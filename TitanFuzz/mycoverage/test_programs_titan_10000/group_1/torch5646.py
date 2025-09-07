import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 3, 4, 5)
other = torch.rand(1, 3, 4, 5)
torch.Tensor.igammac_(input_tensor, other)