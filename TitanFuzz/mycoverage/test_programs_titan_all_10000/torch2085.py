import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 16, 4, 4)
group_norm = torch.nn.GroupNorm(4, 16)
output = group_norm(input)