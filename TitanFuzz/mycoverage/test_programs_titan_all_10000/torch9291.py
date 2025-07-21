import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, dtype=torch.float32)
output = torch.special.digamma(input)