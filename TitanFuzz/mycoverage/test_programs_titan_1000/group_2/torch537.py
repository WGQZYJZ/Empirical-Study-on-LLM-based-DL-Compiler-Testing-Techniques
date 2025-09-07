import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(5, 3)
result = torch.argsort(input, dim=(- 1), descending=False)
result = torch.argsort(input, dim=(- 1), descending=True)
result = torch.argsort(input, dim=1, descending=False)
result = torch.argsort(input, dim=1, descending=True)