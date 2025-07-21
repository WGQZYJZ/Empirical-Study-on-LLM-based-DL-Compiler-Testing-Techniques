import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3)
other = torch.randn(4, 3)
torch.hypot(input, other)