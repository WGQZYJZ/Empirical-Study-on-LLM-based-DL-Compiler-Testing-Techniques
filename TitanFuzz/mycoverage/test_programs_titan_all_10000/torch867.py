import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(3, 3)
res = torch.resolve_neg(input)