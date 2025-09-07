import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, dtype=torch.float32)
output = torch.special.i0(input)