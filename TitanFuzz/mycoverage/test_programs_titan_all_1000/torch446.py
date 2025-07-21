import torch
from torch import nn
from torch.autograd import Variable
input = torch.arange(1, 5, dtype=torch.float).view(1, 1, 4)
pool = torch.nn.AdaptiveAvgPool1d(1)
output = pool(input)