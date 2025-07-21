import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10)
output = torch.sort(input, dim=(- 1), descending=False, stable=False)