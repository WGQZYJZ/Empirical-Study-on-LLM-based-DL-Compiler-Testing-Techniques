import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(10, 10)
b = torch.randn(10, 10)
c = torch.randn(10, 10)
d = torch.randn(10, 10)
e = torch.randn(10, 10)
torch.chain_matmul(a, b, c, d, e)