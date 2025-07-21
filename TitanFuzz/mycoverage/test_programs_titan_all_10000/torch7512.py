import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5, 7)
output = torch.flatten(input, start_dim=1)