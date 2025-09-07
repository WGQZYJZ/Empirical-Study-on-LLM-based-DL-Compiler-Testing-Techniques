import torch
from torch import nn
from torch.autograd import Variable

input = torch.arange(1, 4)
output = torch.tile(input, (2, 2))