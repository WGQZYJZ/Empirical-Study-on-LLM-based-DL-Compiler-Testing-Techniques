import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4)
other = torch.randn(4, 4)
torch.gt(input, other)
out = torch.empty(4, 4)
torch.gt(input, other, out=out)
out = torch.empty(4, 4)
torch.gt(input, other, out=out)