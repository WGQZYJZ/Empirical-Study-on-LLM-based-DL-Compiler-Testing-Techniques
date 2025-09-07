import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
other = torch.randn(3, 3)
res = torch.gt(input, other)
input = torch.randn(3, 3)
other = torch.randn(3, 3)
out = torch.empty(3, 3)
torch.gt(input, other, out=out)