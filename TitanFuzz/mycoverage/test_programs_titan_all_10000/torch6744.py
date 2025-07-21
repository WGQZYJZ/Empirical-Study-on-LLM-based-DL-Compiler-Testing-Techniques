import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.special.gammainc(input, other)
input = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.special.gammaincc(input, other)