import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(10, 5)
torch.resolve_neg(input)