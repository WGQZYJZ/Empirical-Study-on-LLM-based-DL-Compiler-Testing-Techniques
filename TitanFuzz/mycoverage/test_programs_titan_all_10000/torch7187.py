import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
result = torch.amax(input, dim=0)
result = torch.amax(input, dim=1)
result = torch.amax(input, dim=0, keepdim=True)
result = torch.amax(input, dim=1, keepdim=True)
result = torch.amax(input, dim=0, keepdim=False)
result = torch.amax(input, dim=1, keepdim=False)
result = torch.amax(input, dim=None)