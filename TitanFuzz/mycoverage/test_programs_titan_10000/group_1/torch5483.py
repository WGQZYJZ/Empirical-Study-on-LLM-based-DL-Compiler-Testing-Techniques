import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(4, 3)
b = torch.randn(3, 4)
torch.Tensor.inner(a, b)