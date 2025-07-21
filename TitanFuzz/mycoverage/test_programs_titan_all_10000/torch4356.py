import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.special.gammainc(input, other)
torch.special.gammainc(input, other, out=None)
torch.special.gammainc(input, other, out=torch.empty(2, 3, 4))
input = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.special.gammaincc(input, other)
torch.special.gammaincc(input, other, out=None)
torch.special.gammaincc(input, other, out=torch.empty(2, 3, 4))