import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
torch.any(input, dim=1)