import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.rand(1, 1)
other = torch.rand(1, 1)
torch.Tensor.igamma(input_tensor, other)