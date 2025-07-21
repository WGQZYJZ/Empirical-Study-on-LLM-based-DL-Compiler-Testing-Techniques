import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 3)
q = torch.tensor([0.1, 0.5, 0.9])
output = torch.nanquantile(input, q)