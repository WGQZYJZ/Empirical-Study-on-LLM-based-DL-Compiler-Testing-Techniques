import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 2, 3)
min = 0.0
max = 1.0
output = torch.clip(input, min, max)