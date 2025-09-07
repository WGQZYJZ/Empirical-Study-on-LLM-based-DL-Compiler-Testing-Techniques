import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
torch.inverse(input)
input = torch.randn(3, 3)
torch.inverse(input)