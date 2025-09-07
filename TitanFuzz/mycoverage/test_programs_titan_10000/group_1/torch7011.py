import torch
from torch import nn
from torch.autograd import Variable

input = torch.rand(3, 3)
out = torch.float_power(input, 3)