import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 4)
min_index = torch.argmin(input, dim=1, keepdim=True)
min_index = torch.argmin(input, dim=1, keepdim=False)