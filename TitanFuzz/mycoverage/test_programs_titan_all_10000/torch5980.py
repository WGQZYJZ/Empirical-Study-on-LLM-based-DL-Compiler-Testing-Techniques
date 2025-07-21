import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(2, 3, 2)
output = torch.flip(input, [1])
output = torch.flip(input, [2])