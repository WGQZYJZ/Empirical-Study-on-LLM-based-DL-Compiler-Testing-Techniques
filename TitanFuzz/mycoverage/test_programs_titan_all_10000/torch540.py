import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.mul(input, other)
output = torch.empty(2, 3)
torch.mul(input, other, out=output)