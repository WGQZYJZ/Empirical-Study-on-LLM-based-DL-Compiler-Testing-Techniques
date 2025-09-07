import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(20, 16, 50, 32)
output = torch.nn.GroupNorm(num_groups=4, num_channels=16)(input)