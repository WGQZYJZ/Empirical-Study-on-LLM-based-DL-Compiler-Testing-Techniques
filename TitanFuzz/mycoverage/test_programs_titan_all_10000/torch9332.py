import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 4)
output = torch.argsort(input, dim=(- 1), descending=False)