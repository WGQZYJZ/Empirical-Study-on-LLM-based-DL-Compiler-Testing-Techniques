import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 3, 4)
output = torch.flatten(input)