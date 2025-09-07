import torch
from torch import nn
from torch.autograd import Variable

data = torch.rand(5, 3)
result = torch.Tensor.geometric_(data, 0.5)