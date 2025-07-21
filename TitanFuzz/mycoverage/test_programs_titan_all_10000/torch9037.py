import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
other = torch.randn(5, 3)
torch.matmul(input, other)
input = torch.randn(3, 5)
other = torch.randn(5, 3)
torch.matmul(input, other)