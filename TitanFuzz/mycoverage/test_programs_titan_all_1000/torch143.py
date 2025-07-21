import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(2, 2)
b = torch.randn(2, 2)
torch._assert((a.shape == b.shape), 'a and b must have the same shape')