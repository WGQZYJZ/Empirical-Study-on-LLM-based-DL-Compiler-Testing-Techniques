import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(0, 60).view(3, 4, 5)
input = torch.arange(0, 60).view(3, 4, 5)
output = torch.rot90(input, 1, dims=(0, 1))