import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(1, 3, 3)
output = torch.resolve_neg(input)