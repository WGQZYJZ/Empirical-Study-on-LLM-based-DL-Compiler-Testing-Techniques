import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, dtype=torch.float)
output = torch.log1p(input)