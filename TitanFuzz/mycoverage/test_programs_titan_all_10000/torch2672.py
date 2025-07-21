import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(2, 3, 4, 5)
other = torch.randn(2, 3, 2, 2)
torch.kron(input, other)