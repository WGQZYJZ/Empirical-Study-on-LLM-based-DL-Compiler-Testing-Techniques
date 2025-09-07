import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
b = torch.randn(4, 4)
torch.not_equal(a, b)
torch.not_equal(a, b).sum()