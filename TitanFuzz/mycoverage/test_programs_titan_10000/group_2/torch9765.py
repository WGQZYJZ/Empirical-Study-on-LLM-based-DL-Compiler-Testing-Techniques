import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(3, 3)
output = torch.all(input, dim=0, keepdim=False)