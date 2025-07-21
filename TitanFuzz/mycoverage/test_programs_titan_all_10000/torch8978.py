import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3, dtype=torch.float64)
other = torch.randn(4, 3, dtype=torch.float64)
torch.cross(input, other, dim=1)