import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3)
min_index = torch.argmin(input, dim=1)