import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 1)
result = torch.is_floating_point(input)