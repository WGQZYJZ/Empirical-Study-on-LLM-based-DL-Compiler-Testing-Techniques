import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(2, 3)
output = torch.sum(input, dim=1, keepdim=True)
output = torch.sum(input, dim=1, keepdim=False)
output = torch.sum(input, dim=0, keepdim=True)
output = torch.sum(input, dim=0, keepdim=False)