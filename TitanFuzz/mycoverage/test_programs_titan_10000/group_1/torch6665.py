import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(1, 2, 3)
result = torch.is_floating_point(input)