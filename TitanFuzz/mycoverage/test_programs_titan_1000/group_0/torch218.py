import torch
from torch import nn
from torch.autograd import Variable
input = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.long)
output = torch.resolve_neg(input)